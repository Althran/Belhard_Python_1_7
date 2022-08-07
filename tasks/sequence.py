"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""
import random


class RandSequence:
    sequence = None

    def __init__(self, n):
        self.n = n
        self.sequence = self.generate(n)

    def generate(self, n=None):
        if not n:
            n = self.n
        return [random.randint(-n, n) for _ in range(n)]

    def __iter__(self):
        return self

    def print_seq(self):
        return f'{self.sequence}'


print(RandSequence(5))
