# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и
# вывести получившуюся статистику.
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке
# число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода). Порядок вывода слов
# может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз. 

book = input().lower()
lst = book.split()
dict = {}
for word in lst:
    dict[word] = lst.count(word)
for key, value in dict.items():
    print(key, value)