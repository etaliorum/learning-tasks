s = input()
len = len(s)
s_compres = ''
count = 1

for i in range(1, len):
    if s[i] == s[i-1]:
        count += 1
    else:
        s_compres += s[i-1] + str(count)
        count = 1
s_compres += s[len-1] + str(count)
print(s_compres)