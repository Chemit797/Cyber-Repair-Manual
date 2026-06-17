import re

text = open('网页3.txt', encoding='utf-8').read()
svgs = re.findall(r'<svg.*?</svg>', text, re.DOTALL)
svgs = [s.replace('&quot;', '"') for s in svgs]
svgs = sorted(svgs, key=len, reverse=True)

# svgs[0] and svgs[1] might be whole page backgrounds, let's take svgs[2] and svgs[3]
svg_left = svgs[2]
svg_right = svgs[3]

with open('left.svg', 'w', encoding='utf-8') as f:
    f.write(svg_left)
with open('right.svg', 'w', encoding='utf-8') as f:
    f.write(svg_right)
