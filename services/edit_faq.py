import re
import json

def edit_faq():
    path = 'emergency-restoration-service-arvada.html'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # FAQ Section
    start = c.find('<!-- ==================== FAQ SECTION ==================== -->')
    if start == -1: start = c.find('<!-- FAQ')
    if start == -1: start = c.find('<section class="py-16 sm:py-24 bg-slate-50') # Fallback
    
    end = c.find('<!-- ==================== CTA SECTION ==================== -->')
    if end == -1: end = c.find('<!-- CTA')
    
    if start != -1 and end != -1:
        sub = c[start:end]
        
        q_re = r'<span class="text-base sm:text-lg font-bold text-slate-900 group-hover:text-primary transition-colors text-left">\s*(.*?)\s*</span>'
        a_re = r'<div class="text-slate-600 text-sm sm:text-base leading-relaxed p-5 sm:p-6 pt-0">\s*(.*?)\s*</div>'
        
        questions = re.findall(q_re, sub)
        answers = re.findall(a_re, sub, re.DOTALL)
        
        faq_data = [
            ("How quickly can your emergency response team arrive?", "We guarantee a 1-2 hour response time for all emergencies in Arvada, CO. Our dispatch team is available 24/7."),
            ("What should I do while waiting for the emergency team?", "If it is safe, turn off the main water valve and electricity to affected areas. Do not enter standing water, and keep children and pets away."),
            ("Will you board up my windows and roof after a storm?", "Yes, we provide emergency board-up and tarping services to secure your property from further weather damage and unauthorized entry."),
            ("Do you handle both water and fire emergencies?", "Absolutely. We are fully equipped to handle water extraction, fire mitigation, smoke residue cleanup, and storm damage."),
            ("How is emergency restoration different from regular restoration?", "Emergency restoration focuses on immediate stabilization—like stopping a leak, boarding a window, or extracting standing water—to prevent further damage before full restoration begins."),
            ("Will my insurance cover emergency callouts?", "Most homeowner insurance policies cover emergency mitigation to prevent further loss. We can work directly with your adjuster and bill them for the emergency services.")
        ]
        
        for i in range(min(len(questions), 6)):
            sub = sub.replace(f'>{questions[i]}<', f'>{faq_data[i][0]}<')
            # For answer, we need to be careful with spaces
            a_clean = answers[i].strip()
            sub = sub.replace(a_clean, faq_data[i][1])
            
        c = c[:start] + sub + c[end:]

        # Now update FAQPage schema in the head
        schema_start = c.find('<script type="application/ld+json">')
        schema_end = c.find('</script>', schema_start)
        # Wait, there might be multiple script tags. Let's look for @type": "FAQPage"
        faq_schema_start = c.find('"@type": "FAQPage"')
        if faq_schema_start != -1:
            # find the enclosing script tag
            script_start = c.rfind('<script', 0, faq_schema_start)
            script_end = c.find('</script>', faq_schema_start) + 9
            
            schema_str = c[script_start:script_end]
            try:
                # Extract JSON
                json_str = schema_str[schema_str.find('{'):schema_str.rfind('}')+1]
                data = json.loads(json_str)
                
                # Update mainEntity
                main_entity = []
                for q, a in faq_data:
                    main_entity.append({
                        "@type": "Question",
                        "name": q,
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": a
                        }
                    })
                data['mainEntity'] = main_entity
                
                new_json_str = json.dumps(data, indent=4)
                new_schema_str = f'<script type="application/ld+json">\n{new_json_str}\n    </script>'
                c = c[:script_start] + new_schema_str + c[script_end:]
            except Exception as e:
                print("Error parsing schema:", e)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

edit_faq()
