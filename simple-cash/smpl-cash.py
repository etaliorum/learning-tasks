# Посути простое кеширование значений которые мы уже считали, и что бы не считать еще раз выводим из словаря

def f(x):
    return x ** 2


n = int(input())
s = {}
cash = 0

for i in range(n):
    x = int(input())
    if x not in s:
        cash = f(x)
        print(cash)  # from new
        s[x] = cash
    else:
        print(s[x])  # from cash
