# Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе два аргумента
# a и f – последовательность и функцию, и позволяет проитерироваться только по таким элементам x из
# последовательности a, что f(x) равно True. Будем говорить, что в этом случае функция f допускает элемент x,
# а элемент x является допущенным.
# В данной задаче мы просим вас реализовать класс Multifilter, который будет выполнять ту же функцию,
# что и стандартный класс filter, но будет использовать не одну функцию, а несколько.
# Решение о допуске элемента будет приниматься на основании того, сколько функций допускают этот элемент,
# и сколько не допускают. Обозначим эти количества за pos и neg.
# Введем понятие решающей функции – это функция, которая принимает два аргумента – количества pos и neg, и возвращает
# True, если элемент допущен, и False иначе.

class Multifilter:
    def judge_half(self, i):
        pos, neg = self.count_res(i)
        return pos >= neg

    def judge_any(self, i):
        pos, neg = self.count_res(i)
        return pos >= 1

    def judge_all(self, i):
        pos, neg = self.count_res(i)
        return neg == 0

    def count_res(self, x):
        res = [f(x) for f in self.funcs]
        return res.count(True), res.count(False)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for i in self.iterable:
            if self.judge(self, i):
                yield i


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(42)]
print(list(Multifilter(a, mul2, mul3, mul5)))
print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_half)))
print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_all)))
