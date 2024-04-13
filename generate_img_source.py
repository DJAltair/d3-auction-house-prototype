import os
import sys
from pathlib import Path

rootdir = os.path.dirname(sys.argv[0])

print(rootdir)

f = open("out.md", mode = "w+")

for root, sub_folders, files in os.walk("."):
    if root.startswith(".\\diagrams\\") == False:
        continue
    
    for file in files:
        fp = root.replace("\\", "/") + "/" + file.replace("\\", "/")
        n = Path(os.path.basename(file)).stem
        
        f.write("<details>\n")
        f.write(f"<summary>{n}</summary>\n")
        f.write("<p align=\"center\">\n")
        f.write(f"<img src=\"{fp}?raw=true\" width=\"*\"/>\n")
        f.write("</p>\n")
        f.write("</details>\n\n\n")
        print(f"{root}/{file}\n")
        
f.close()