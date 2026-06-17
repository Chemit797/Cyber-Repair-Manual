import sys

left_svg = open('left.svg', encoding='utf-8').read()
right_svg = open('right.svg', encoding='utf-8').read()

app_py = open('app.py', encoding='utf-8').read()

html_injection = f'''
st.markdown("""
<div style="position: fixed; top: 10%; left: 2%; width: 300px; z-index: 0; opacity: 0.9; pointer-events: none;">
    {left_svg}
</div>
<div style="position: fixed; bottom: 5%; right: 2%; width: 300px; z-index: 0; opacity: 0.9; pointer-events: none;">
    {right_svg}
</div>
""", unsafe_allow_html=True)
'''

if 'pointer-events: none' not in app_py:
    app_py = app_py.replace('st.markdown(custom_css, unsafe_allow_html=True)', 'st.markdown(custom_css, unsafe_allow_html=True)\n' + html_injection)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_py)
