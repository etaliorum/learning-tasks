# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно
# положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность
# добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее
# вместимость.

class MoneyBox:
    def __init__(self, capacity):
        self.v = 0
        self.capacity = capacity

    def can_add(self, v):
        if v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.v += v


mb = MoneyBox(10)
print(mb.capacity, mb.v)
mb.add(5)
print(mb.v)
mb.add(5)
print(mb.v)
mb.add(1)
print(mb.v)