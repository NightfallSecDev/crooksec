import os
import glob

html_files = glob.glob("/home/kali/Documents/crooksec/*.html")

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Cache bust main.js and style.css
    content = content.replace('src="main.js"', 'src="main.js?v=3"')
    content = content.replace('href="style.css"', 'href="style.css?v=3"')

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Cache busted {os.path.basename(filepath)}")
