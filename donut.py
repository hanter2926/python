
import math
import time
import os

A = 0
B = 0

while True:
    output = [" "] * 1760
    zbuffer = [0] * 1760

    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            c = math.cos(i / 100)
            d = math.sin(j / 100)
            e = math.sin(A)
            f = math.sin(j / 100)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            t = c * h * g - f * e

            x = int(40 + 30 * D * (math.cos(i / 100) * h * math.cos(B) - t * math.sin(B)))
            y = int(12 + 15 * D * (math.cos(i / 100) * h * math.sin(B) + t * math.cos(B)))

            o = x + 80 * y
            N = int(8 * ((f * e - c * d * g) * math.cos(B) - c * d * e - f * g - math.sin(i / 100) * math.sin(B)))

            if 0 <= x < 80 and 0 <= y < 22 and D > zbuffer[o]:
                zbuffer[o] = D
                output[o] = ".,-~:;=!*#$@"[max(0, min(11, N))]

    os.system("cls" if os.name == "nt" else "clear")
    for k in range(0, 1760, 80):
        print("".join(output[k:k + 80]))

    A += 0.07
    B += 0.03
    time.sleep(0.03)
