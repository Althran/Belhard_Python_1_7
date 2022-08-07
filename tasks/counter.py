"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты:

- value - текущее значение счетчика

Определить методы:

- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""


class Counter:

    def __init__(self, value=0):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > 100:
            raise StopIteration
        value = self.value
        self.value += 1
        return value

    def increase(self, num=1):
        self.value += num

    def decrease(self, num=1):
        self.value -= num
