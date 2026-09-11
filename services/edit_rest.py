import re

def edit_emergency():
    path = 'emergency-restoration-service-arvada.html'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 4. WHY CHOOSE US
    start = c.find('<!-- ==================== WHY CHOOSE US')
    end = c.find('<!-- ==================== WHAT')
    sub = c[start:end]

    t_re = r'<h3 class="text-xl font-extrabold text-white group-hover:text-.*? transition-colors mb-2\.5">\s*(.*?)\s*</h3>'
    d_re = r'<p class="text-sm text-slate-300 leading-relaxed">\s*(.*?)\s*</p>'
    
    titles = re.findall(t_re, sub)
    descs = re.findall(d_re, sub)
    
    replacements = [
        ('Speed & Efficiency', 'Rapid response is critical in emergencies to minimize property damage and mitigate loss.'),
        ('24/7 Availability', 'Disasters do not wait for business hours. Our emergency response team is available 24/7/365.'),
        ('Multi-Disaster Capability', 'We handle water, fire, storm damage, and biohazard emergencies with comprehensive solutions.'),
        ('Insurance Coordination', 'We work directly with your insurance company to streamline the emergency claims process.')
    ]
    
    for i in range(4):
        if i < len(titles):
            sub = sub.replace(f'>{titles[i]}<', f'>{replacements[i][0]}<')
            sub = sub.replace(f'>{descs[i]}<', f'>{replacements[i][1]}<')
            
    c = c[:start] + sub + c[end:]

    # 5. WHAT'S INCLUDED
    start = c.find('<!-- ==================== WHAT')
    end = c.find('<!-- ==================== TRANSPARENT PRICING')
    if end == -1: end = c.find('<!-- ==================== PRICING')
    sub = c[start:end]

    i_re = r'<span class="text-sm sm:text-base text-slate-800 font-semibold leading-snug">(.*?)</span>'
    items = re.findall(i_re, sub)
    
    new_items = [
        '24/7 immediate dispatch and scene assessment',
        'Emergency board-up and structural stabilization',
        'Tarping and roof protection against the elements',
        'Emergency water shutoff and leak containment',
        'Rapid water extraction using truck-mounted equipment',
        'Hazardous material and biohazard isolation',
        'Temporary power and lighting setup',
        'Debris removal and site cleanup',
        'Seamless transition to full restoration services'
    ]
    
    for i in range(min(len(items), 9)):
        sub = sub.replace(f'>{items[i]}<', f'>{new_items[i]}<')
        
    sub = re.sub(r'When Do You Need Full Restoration\?', 'When Do You Need Emergency Restoration?', sub)
    sub = re.sub(r'Where Water Damage Hides', 'What Emergencies We Respond To', sub)
    
    c = c[:start] + sub + c[end:]

    # 6. PRICING
    start = c.find('<!-- ==================== PRICING')
    if start == -1: start = c.find('<!-- ==================== TRANSPARENT PRICING')
    end = c.find('<!-- ==================== RELATED SERVICES')
    sub = c[start:end]

    rows = re.findall(r'<td class="p-4 sm:p-5 text-sm sm:text-base text-slate-800 font-semibold">\s*(.*?)\s*</td>', sub)
    costs = re.findall(r'<div class="text-base sm:text-lg font-bold text-slate-900">\s*(.*?)\s*</div>', sub)
    
    new_rows = [
        'Emergency Board-Up',
        'Roof Tarping',
        'Emergency Water Shutoff',
        'Emergency Extraction',
        'Storm Damage Mitigation',
        'After-Hours Emergency Callout'
    ]
    new_costs = [' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
    
    for i in range(min(len(rows), 6)):
        sub = sub.replace(f'>{rows[i]}<', f'>{new_rows[i]}<')
        sub = sub.replace(f'>{costs[i]}<', f'>{new_costs[i]}<')

    c = c[:start] + sub + c[end:]

    # 7. RELATED SERVICES
    start = c.find('<!-- ==================== RELATED SERVICES')
    end = c.find('<!-- ==================== FAQ')
    sub = c[start:end]
    
    titles = re.findall(r'<h3 class="text-xl font-extrabold text-slate-900 group-hover:text-primary transition-colors mb-3">\s*(.*?)\s*</h3>', sub)
    new_rel = [
        'Water Damage Restoration',
        'Fire Damage Restoration',
        'Flood Damage Restoration'
    ]
    
    for i in range(3):
        if i < len(titles):
            sub = sub.replace(f'>{titles[i]}<', f'>{new_rel[i]}<')
            
    c = c[:start] + sub + c[end:]

    # Write back
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

edit_emergency()
