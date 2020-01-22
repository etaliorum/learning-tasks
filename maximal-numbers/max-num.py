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
