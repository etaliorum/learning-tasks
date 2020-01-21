a = float(input())
b = float(input())
operand = input()

if (operand == '+'):
    print(a + b)
if (operand == '-'):
    print(a - b)
if (operand == '/'):
    if b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
if (operand == '*'):
    print(a * b)
if (operand == 'mod'):
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
if operand == 'pow':
    print(a ** b)
if operand == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)
