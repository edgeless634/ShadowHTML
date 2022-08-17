import math
import cv2
from Crypto.Util.number import long_to_bytes, bytes_to_long
import base64


def bitspoper(b, size):
    for i in b:
        s = bin(i)[2:].zfill(8)
        while s:
            yield int(s[:size], 2)
            s = s[size:]


with open("target.html", "rb") as f:
    b = f.read()

size = 2

# b = base64.b64encode(b)

b = len(b).to_bytes(4, byteorder="big") + b

source_img = cv2.imread("source.png")

source_img = cv2.cvtColor(source_img, cv2.COLOR_BGR2RGB)

for i in range(source_img.shape[0]):
    for j in range(source_img.shape[1]):
        for k in range(3):
            source_img[i][j][k] = source_img[i][j][k] - (source_img[i][j][k] % (1 << size))


g = bitspoper(b, size)

should_break = False

l = []

for i in range(source_img.shape[0]):
    if should_break:
        break
    for j in range(source_img.shape[1]):
        if should_break:
            break
        for k in range(3):
            try:

                nxt = next(g)

                if i == 0 and j < 6:
                    l.append(nxt)

                source_img[i][j][k] += nxt

            except StopIteration:
                should_break = True
                break


source_img = cv2.cvtColor(source_img, cv2.COLOR_RGB2BGR)


cv2.imwrite("output.png", source_img, )