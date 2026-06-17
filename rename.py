import os
import glob

replacements = {
    "家电故障排查助手": "nlp-Repair-Assistant",
    "维修助手": "nlp-Repair-Assistant"
}

md_files = glob.glob(r"D:\Project\xmum-2604\nlp\*.md")
for file_path in md_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
        
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file_path)}")
