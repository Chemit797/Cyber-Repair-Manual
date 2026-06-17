import os
import glob

replacements = {
    "nlp-Repair-Assistant": "Cyber-Repair-Manual"
}

md_files = glob.glob(r"D:\Project\xmum-2604\nlp\*.md")
py_files = glob.glob(r"D:\Project\xmum-2604\nlp\*.py")

for file_path in md_files + py_files:
    if os.path.basename(file_path) in ["rename.py", "rename_again.py"]:
        continue
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
            
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(file_path)}")
    except Exception as e:
        print(f"Skipped {os.path.basename(file_path)} due to error: {e}")
