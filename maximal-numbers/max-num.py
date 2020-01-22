"""
a = int(input())
b = int(input())
c = int(input())

max = max(a, b)
min = min(a, b)

if max >= c:
    if c >= min:
        print(max, c, min)
    else:
        min, c = c, min
        print(max, c, min)
else:
    max, c = c, max
    print(max, c, min)
"""

a = int(input())
b = int(input())
c = int(input())

max = max(a, b)
min = min(a, b)

if max <= c:
    max, c = c, max
    print(1)
    print(max, min, c)
elif min >= c:
    print(2)
    min, c = c, min
    print(max, min, c)
else:
    print(3)
    print(max, min, c)
