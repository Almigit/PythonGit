"""
Так как в пайтон любой класс может наследовать от нескольких классов, то возникла
проблема, как искать атрибуты и методы родительских классов
в этих сложных зависмостях. Это проблема называется diamond problem

MRO - method resolution ordering

Жесткий порядок решения этих зависимостей

MRO это список зависимостей, его можно получить методом .mro()

MRO2 - python 2, использует глубинный алгоритм
MRO3 - python 3, использует алгоритм в ширину
"""

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(C, B):
    pass

print(D.mro()) # показывает все зависимости