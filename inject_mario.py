import urllib.request
import base64
import sys

urls = [
    "https://media.tenor.com/P1i1uY0pGEoAAAAi/mario-run.gif", # A known tenor gif
    "https://media3.giphy.com/media/SPB2DnJt1oB8c/giphy.gif", # Mario jump
    "https://upload.wikimedia.org/wikipedia/en/a/a9/MarioNSMBUDeluxe.png", # Fallback static transparent PNG
]

gif_b64 = ""
for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = response.read()
            gif_b64 = base64.b64encode(data).decode('utf-8')
            mime_type = "image/png" if url.endswith(".png") else "image/gif"
            break
    except Exception as e:
        print(f"Failed {url}: {e}")

if not gif_b64:
    print("Failed to download any image.")
    sys.exit(1)

# Now inject it into app.py
app_py = open('app.py', encoding='utf-8').read()

html_injection = f'''
<img src="data:{mime_type};base64,{gif_b64}" style="position: fixed; bottom: 5%; left: 5%; width: 150px; z-index: 0; opacity: 0.9; pointer-events: none;" />
<img src="data:{mime_type};base64,{gif_b64}" style="position: fixed; bottom: 5%; right: 5%; width: 150px; z-index: 0; opacity: 0.9; transform: scaleX(-1); pointer-events: none;" />
'''

# We will replace the previous SVG injection with this Mario one.
import re
# The old injection was wrapped in st.markdown(""" ... """, unsafe_allow_html=True)
# Let's just find the custom_css markdown and replace anything after it if it was our injection.
# Or just replace the old html_injection.
# Since we know the previous one had `<div style="position: fixed; top: 10%; left: 2%;`
app_py = re.sub(r'<div style="position: fixed; top: 10%; left: 2%;.*?</div>\s*<div style="position: fixed; bottom: 5%; right: 2%;.*?</div>', html_injection, app_py, flags=re.DOTALL)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_py)

print("Injected Mario successfully!")
