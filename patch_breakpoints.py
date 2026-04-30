import os
import glob

html_files = glob.glob("/home/kali/Documents/crooksec/*.html")

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Navbar breakpoint: shift from md to lg to fix tablet overflow
    content = content.replace('hidden md:flex gap-8 text-sm', 'hidden lg:flex gap-8 text-sm')
    content = content.replace('class="md:hidden text-white text-2xl focus:outline-none"', 'class="lg:hidden text-white text-2xl focus:outline-none"')
    content = content.replace('class="hidden md:hidden fixed top-20', 'class="hidden lg:hidden fixed top-20')
    
    # Also fix the urgent button in nav if needed
    content = content.replace('hidden md:inline-flex px-4 py-2 border border-red-500', 'hidden lg:inline-flex px-4 py-2 border border-red-500')
    
    # 2. Footer grid breakpoint: fix tablet squishing
    content = content.replace('grid-cols-1 md:grid-cols-4 gap-12', 'grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12')
    
    # 3. Service page sidebar layout: shift to lg
    if "service.html" in filepath:
        content = content.replace('md:grid-cols-[300px_1fr]', 'lg:grid-cols-[300px_1fr]')
        content = content.replace('md:sticky', 'lg:sticky')
        
    # 4. About Us grids: shift from md:grid-cols-3 to md:grid-cols-2 lg:grid-cols-3
    if "aboutus.html" in filepath:
        content = content.replace('md:grid-cols-3 gap-8', 'md:grid-cols-2 lg:grid-cols-3 gap-8')
        content = content.replace('md:grid-cols-3 gap-12', 'md:grid-cols-2 lg:grid-cols-3 gap-12')
        
    # 5. Partner grid
    if "patner.html" in filepath:
        content = content.replace('md:grid-cols-3 gap-8', 'md:grid-cols-2 lg:grid-cols-3 gap-8')

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Patched breakpoints in {os.path.basename(filepath)}")

