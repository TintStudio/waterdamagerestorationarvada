import os
import re

def rewrite_emergency():
    path = 'emergency-restoration-service-arvada.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We will just rewrite the whole sections.
    # To keep CSS, we'll use regex to match the inner HTML of the sections.
    # 2. KNOW THE SIGNS
    signs_section_start = content.find('<!-- ==================== KNOW THE SIGNS SECTION ==================== -->')
    signs_section_end = content.find('<!-- ==================== HOW IT WORKS')
    s_content = content[signs_section_start:signs_section_end]
    
    titles = re.findall(r'<h3 class="font-extrabold text-white text-lg leading-snug group-hover:text-sky-400 transition-colors">\s*(.*?)\s*</h3>', s_content)
    descs = re.findall(r'<p class="text-slate-300 text-sm sm:text-base leading-relaxed pl-12">\s*(.*?)\s*</p>', s_content)
    
    signs = [
        ('Active Water Flowing', 'Gushing water from broken pipes or water mains requires immediate emergency shutoff.'),
        ('Visible Structural Damage', 'Fallen trees, shattered windows, or damaged roofs leave your home exposed.'),
        ('Smoke or Fire Residue', 'Soot, ash, and acidic smoke residue will permanently damage surfaces.'),
        ('Sewage Backup', 'Black water backups pose severe health hazards and require immediate biohazard cleanup.'),
        ('Ceiling Collapse', 'Sagging or ruptured ceilings from water weight can cause catastrophic collapse.'),
        ('Electrical Hazard', 'Exposed wires near water or gas odors mean the property is unsafe.')
    ]
    
    for i in range(6):
        if i < len(titles):
            s_content = s_content.replace(f'>{titles[i]}<', f'>{signs[i][0]}<')
            s_content = s_content.replace(f'>{descs[i]}<', f'>{signs[i][1]}<')
            
    content = content[:signs_section_start] + s_content + content[signs_section_end:]

    # 3. HOW IT WORKS
    how_section_start = content.find('<!-- ==================== HOW IT WORKS')
    how_section_end = content.find('<!-- ==================== WHY CHOOSE US')
    h_content = content[how_section_start:how_section_end]
    
    step_titles = re.findall(r'<h3 class="text-xl font-extrabold text-slate-900 group-hover:text-primary transition-colors mb-3">\s*(.*?)\s*</h3>', h_content)
    step_descs = re.findall(r'<p class="text-sm text-slate-600 leading-relaxed">\s*(.*?)\s*</p>', h_content)
    
    steps = [
        ('Emergency Call', 'Call our 24/7 hotline for immediate dispatch and scene assessment.'),
        ('Rapid Dispatch', 'Our team arrives typically within 1-2 hours to secure the site.'),
        ('Scene Assessment', 'We identify safety hazards and assess the extent of the damage.'),
        ('Immediate Mitigation', 'We perform emergency services like board-up, tarping, and water shutoff.'),
        ('Stabilization', 'We install commercial air movers and structural supports to stabilize.'),
        ('Transition to Full Restoration', 'Once stabilized, we begin the complete property restoration process.')
    ]
    
    for i in range(5):
        h_content = h_content.replace(f'>{step_titles[i]}<', f'>{steps[i][0]}<')
        h_content = h_content.replace(f'>{step_descs[i]}<', f'>{steps[i][1]}<')
        
    step_6_t = re.search(r'<span>(.*?)</span>', h_content[h_content.find('Final Step'):])
    if step_6_t:
        h_content = h_content.replace(f'<span>{step_6_t.group(1)}</span>', f'<span>{steps[5][0]}</span>')
    step_6_d = re.search(r'<p class="text-sm text-slate-200 leading-relaxed">\s*(.*?)\s*</p>', h_content)
    if step_6_d:
        h_content = h_content.replace(f'>{step_6_d.group(1)}<', f'>{steps[5][1]}<')

    content = content[:how_section_start] + h_content + content[how_section_end:]

    # Write back
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        
rewrite_emergency()
