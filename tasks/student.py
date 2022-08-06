"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:

    def __init__(self, surname, name, group, average_score):
        self.name = name
        self.surname = surname
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other

    def __ne__(self, other):
        return self.average_score != other

    def __lt__(self, other):
        return self.average_score < other

    def __gt__(self, other):
        return self.average_score > other

    def __le__(self, other):
        return self.average_score <= other

    def __ge__(self, other):
        return self.average_score >= other

    def __repr__(self):
        return '{' + self.surname + ', ' + self.name + ', ' + str(self.group) + ', ' + str(self.average_score) + '}'


students = [Student(surname='VI', name='lui', group=1, average_score=6),
            Student(surname='VII', name='lu', group=1, average_score=4),
            Student(surname='VP', name='ui', group=1, average_score=7),
            Student(surname='VW', name='i', group=2, average_score=1),
            Student(surname='VQ', name='loop', group=3, average_score=5)]


students1 = sorted(students)
students_reverse = sorted(students, reverse=True)
print(students1)
print(students_reverse)
students2 = list(filter(lambda x: (x > 5), students1))
print(students2)
