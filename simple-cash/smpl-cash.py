# Посути простое кеширование значений которые мы уже считали, и что бы не считать еще раз выводим из словаря

def f(x):
    return x ** 2


n = int(input())
s = {}

for i in range(n):
    x = int(input())
    if x not in s:
        s[x] = f(x)
        print(s[x])  # from new
    else:
        print(s[x])  # from cash
