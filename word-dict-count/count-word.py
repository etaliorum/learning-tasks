book = input().lower()
lst = book.split()
dict = {}
for word in lst:
    dict[word] = lst.count(word)
for key, value in dict.items():
    print(key, value)