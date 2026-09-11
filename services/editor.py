import os
import re

def rewrite_emergency():
    path = 'emergency-restoration-service-arvada.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Trust Features Bar
    trust_bar = '''  <!-- ==================== TRUST FEATURES BAR ==================== -->
  <section class="bg-neutral-950 border-t-2 border-orange-500 border-b border-neutral-800 py-6 text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6 sm:gap-4 items-center">
        <div class="flex items-center gap-3.5">
          <div class="w-12 h-12 rounded-full bg-orange-500 text-neutral-950 flex items-center justify-center shrink-0 text-xl font-bold shadow-md">??</div>
          <div>
            <div class="text-sm font-extrabold text-white leading-tight">Industry Certified</div>
            <div class="text-xs text-neutral-400 font-medium mt-0.5">Trained technicians</div>
          </div>
        </div>
        <div class="flex items-center gap-3.5">
          <div class="w-12 h-12 rounded-full bg-orange-500 text-neutral-950 flex items-center justify-center shrink-0 text-lg font-bold shadow-md"><i class="fa-solid fa-check"></i></div>
          <div>
            <div class="text-sm font-extrabold text-white leading-tight">Fully Insured</div>
            <div class="text-xs text-neutral-400 font-medium mt-0.5">Completely covered</div>
          </div>
        </div>
        <div class="flex items-center gap-3.5">
          <div class="w-12 h-12 rounded-full bg-orange-500 text-neutral-950 flex items-center justify-center shrink-0 text-lg font-bold shadow-md"><i class="fa-solid fa-bolt"></i></div>
          <div>
            <div class="text-sm font-extrabold text-white leading-tight">24/7 Emergency</div>
            <div class="text-xs text-neutral-400 font-medium mt-0.5">Day or night</div>
          </div>
        </div>
        <div class="flex items-center gap-3.5">
          <div class="w-12 h-12 rounded-full bg-orange-500 text-neutral-950 flex items-center justify-center shrink-0 text-lg font-bold shadow-md"><i class="fa-solid fa-magnifying-glass"></i></div>
          <div>
            <div class="text-sm font-extrabold text-white leading-tight">Free Inspection</div>
            <div class="text-xs text-neutral-400 font-medium mt-0.5">No cost assessment</div>
          </div>
        </div>
        <div class="flex items-center gap-3.5 col-span-2 md:col-span-1">
          <div class="w-12 h-12 rounded-full bg-orange-500 text-neutral-950 flex items-center justify-center shrink-0 text-base font-bold shadow-md"><span class="bg-emerald-500 text-white rounded p-0.5 text-xs inline-flex items-center justify-center leading-none"><i class="fa-solid fa-check"></i></span></div>
          <div>
            <div class="text-sm font-extrabold text-white leading-tight">100% Guaranteed</div>
            <div class="text-xs text-neutral-400 font-medium mt-0.5">Results in writing</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ==================== KNOW THE SIGNS SECTION ==================== -->'''
    
    content = content.replace('  <!-- ==================== KNOW THE SIGNS SECTION ==================== -->', trust_bar)

    # 2. KNOW THE SIGNS
    # We will regex replace the text in the cards
    signs = [
        ('Active Water Flowing Into Your Property', 'Gushing water from broken pipes or water mains requires immediate emergency shutoff and extraction.'),
        ('Visible Structural Damage After a Storm', 'Fallen trees, shattered windows, or damaged roofs leave your home exposed to the elements and need board-up.'),
        ('Smoke or Fire Residue Still Present', 'Soot, ash, and acidic smoke residue will permanently damage surfaces if not mitigated quickly.'),
        ('Sewage or Contaminated Water Backup', 'Black water backups pose severe health hazards and require immediate professional biohazard cleanup.'),
        ('Ceiling Collapse or Imminent Structural Failure', 'Sagging or ruptured ceilings from water weight can cause catastrophic collapse and injury.'),
        ('Gas Leak or Electrical Hazard', 'Exposed wires near water or gas odors mean the property is unsafe and needs immediate hazard stabilization.')
    ]
    
    # Let's replace the card titles and descriptions
    # Find all h3 tags inside KNOW THE SIGNS section
    signs_section_start = content.find('<!-- ==================== KNOW THE SIGNS SECTION ==================== -->')
    signs_section_end = content.find('<!-- ==================== HOW IT WORKS / RESTORATION PROCESS SECTION ==================== -->')
    signs_content = content[signs_section_start:signs_section_end]
    
    titles = re.findall(r'<h3 class="font-extrabold text-white text-lg leading-snug group-hover:text-sky-400 transition-colors">\s*(.*?)\s*</h3>', signs_content)
    descs = re.findall(r'<p class="text-slate-300 text-sm sm:text-base leading-relaxed pl-12">\s*(.*?)\s*</p>', signs_content)
    
    for i, (old_t, old_d) in enumerate(zip(titles, descs)):
        signs_content = signs_content.replace(old_t, signs[i][0])
        signs_content = signs_content.replace(old_d, signs[i][1])
        
    content = content[:signs_section_start] + signs_content + content[signs_section_end:]

    # 3. HOW IT WORKS
    how_section_start = content.find('<!-- ==================== HOW IT WORKS / RESTORATION PROCESS SECTION ==================== -->')
    how_section_end = content.find('<!-- ==================== WHY CHOOSE US')
    how_content = content[how_section_start:how_section_end]
    
    steps = [
        ('Emergency Call', 'Call (720) 735-8908. Our live dispatcher gathers critical information about your emergency and initiates an immediate response.'),
        ('Rapid Dispatch', 'Our fully equipped emergency response team is dispatched and typically arrives at your Arvada property within 1-2 hours.'),
        ('Scene Assessment', 'We secure the site, identify safety hazards, and quickly assess the extent of the damage to create an action plan.'),
        ('Immediate Mitigation', 'We perform emergency services like board-up, tarping, water extraction, or shutting off mains to prevent further damage.'),
        ('Stabilization', 'We install commercial air movers, dehumidifiers, or structural supports to stabilize the environment.'),
        ('Transition to Full Restoration', 'Once the emergency is contained and stabilized, we prepare a detailed plan and begin the complete restoration process.')
    ]
    
    step_titles = re.findall(r'<h3 class="text-xl font-extrabold text-slate-900 group-hover:text-primary transition-colors mb-3">\s*(.*?)\s*</h3>', how_content)
    # The 6th step has different HTML
    step_6_title_match = re.search(r'<span>(.*?)</span>\s*<i class="fa-solid fa-circle-check', how_content)
    if step_6_title_match:
        step_titles.append(step_6_title_match.group(1))
        
    step_descs = re.findall(r'<p class="text-sm text-slate-600 leading-relaxed">\s*(.*?)\s*</p>', how_content)
    step_6_desc_match = re.search(r'<p class="text-sm text-slate-200 leading-relaxed">\s*(.*?)\s*</p>', how_content)
    if step_6_desc_match:
        step_descs.append(step_6_desc_match.group(1))
        
    for i in range(5):
        how_content = how_content.replace(step_titles[i], steps[i][0])
        how_content = how_content.replace(step_descs[i], steps[i][1])
    
    if len(step_titles) == 6:
        how_content = how_content.replace(step_titles[5], steps[5][0])
        how_content = how_content.replace(step_descs[5], steps[5][1])
        
    content = content[:how_section_start] + how_content + content[how_section_end:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

rewrite_emergency()
