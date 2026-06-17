import sys

qblock_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="100%" height="100%" shape-rendering="crispEdges">
"""
colors = {
    '#': 'black',
    'Y': '#FFD700',
    'O': '#DAA520'
}
qblock_art = [
    "################",
    "#YYYYYYYYYYYYYY#",
    "#YOOOOOOOOOOOOY#",
    "#YOYOOOOOOOOYOY#",
    "#YOOO####OOOOOY#",
    "#YOO##OO##OOOOY#",
    "#YOO##OO##OOOOY#",
    "#YOOOOOO##OOOOY#",
    "#YOOOOO##OOOOOY#",
    "#YOOOO##OOOOOOY#",
    "#YOOOO##OOOOOOY#",
    "#YOOOOOOOOOOOOY#",
    "#YOOOO##OOOOOOY#",
    "#YOOOO##OOOOOOY#",
    "#YOOOOOOOOOOOOY#",
    "################",
]
for y, row in enumerate(qblock_art):
    for x, char in enumerate(row):
        if char in colors:
            qblock_svg += f'<rect x="{x}" y="{y}" width="1" height="1" fill="{colors[char]}"/>\n'
qblock_svg += "</svg>"

mushroom_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="100%" height="100%" shape-rendering="crispEdges">
"""
m_colors = {
    '#': 'black',
    'R': '#E52521',
    'W': '#FFFFFF',
    'B': '#FBD0B0'
}
mushroom_art = [
    "      ####      ",
    "    ##RRRR##    ",
    "   #RRRRRRRR#   ",
    "  #RRRRRRRRRR#  ",
    " #RWWWRRRRRRWWR#",
    " #RWWWRRRRRRWWR#",
    "#RRRRRRRRRRRRRR#",
    "#RRRWWWRRRRRRRR#",
    "#RRRWWWRRRRRRRR#",
    " #RRRRRRRRRRRR# ",
    "  ##BBBBBBBB##  ",
    "  #BB#BBBB#BB#  ",
    "  #BBBBBBBBBB#  ",
    "   #BBBBBBBB#   ",
    "    ########    ",
    "                ",
]
for y, row in enumerate(mushroom_art):
    for x, char in enumerate(row):
        if char in m_colors:
            mushroom_svg += f'<rect x="{x}" y="{y}" width="1" height="1" fill="{m_colors[char]}"/>\n'
mushroom_svg += "</svg>"

html_injection = f'''
st.markdown("""
<div style="position: fixed; top: 10%; left: 5%; width: 100px; z-index: 0; opacity: 0.9; pointer-events: none; animation: float 3s ease-in-out infinite;">
    {qblock_svg}
</div>
<div style="position: fixed; top: 10%; right: 5%; width: 100px; z-index: 0; opacity: 0.9; pointer-events: none; animation: float 3s ease-in-out infinite reverse;">
    {mushroom_svg}
</div>
<style>
@keyframes float {{
    0% {{ transform: translateY(0px); }}
    50% {{ transform: translateY(-20px); }}
    100% {{ transform: translateY(0px); }}
}}
</style>
""", unsafe_allow_html=True)
'''

app_py = open('app.py', encoding='utf-8').read()

# We need to inject this alongside the Mario injection.
# Mario injection was a st.markdown block right at the end or near the end.
app_py += "\n" + html_injection

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_py)

print("Injected SVGs successfully!")
