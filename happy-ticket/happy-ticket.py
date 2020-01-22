# данное решение сделанно с набором минимальных функций
s, t, r, i, n, g = input()

left, right = int(s) + int(t) + int(r), int(i) + int(n) + int(g)

if left == right:
    print('Счастливый')
else: print('Обычный')