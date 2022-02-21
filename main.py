from PIL import Image
from time import sleep
import pyautogui as pya
from collections import defaultdict

pya.PAUSE = 0
pya.MINIMUM_SLEEP = 0 
pya.MINIMUM_DURATION = 0

im = Image.open("si.jpg")
rgb_im = im.convert("RGB")

def transform(b):
    ll = []
    l = []
    for i in b:
        if len(l) == 0:
            l.append(i)
        else:
            if l[-1] + 1 == i:
                l.append(i)
            else:
                ll.append(l)
                l = [i]
    ll.append(l)
    return ll

P = []
for y in range(im.size[1]):
    for x in range(im.size[0]):
        r, g, b = rgb_im.getpixel((x, y))
        Y = 0.2126 * r + 0.7152 * g + 0.0722 * b
        if Y <= 128:
            P.append((x,y))

Y = defaultdict(list)

for p in P:
    Y[p[1]].append(p[0])

B = {}

for x in Y:
    B[x] = (transform(Y[x]))

print("Place mouse on left corner of sketch")
sleep(3)
xoff, yoff = pya.position()

for k in B:
    for b in B[k]:
        pya.moveTo(min(b)+xoff, k+yoff)
        pya.dragTo(max(b)+xoff, k+yoff)

#second pass
#for k in reversed(B.keys()):
#    for b in B[k]:
#        pya.moveTo(min(b)+xoff, k+yoff)
#        pya.dragTo(max(b)+xoff, k+yoff)

