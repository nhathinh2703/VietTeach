s = "81723"
skq = 0
for ch in s:
    if int(ch) % 2 != 0:
        skq = skq + int(ch)

print(skq)