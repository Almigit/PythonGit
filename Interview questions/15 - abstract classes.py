"""
В пайтоне нет интерфейсов, поэтому если нужно создать некий контракт,
который будет обязывать все дочерние классы реализовывать некоторые методы,
используется абстрактный класс и абстрактные методы

абстрактный класс это класс, от которого нельзя создать объекты
"""

from abc import ABC, ABCMeta, abstractmethod

# такой класс еще не абстрактный, можно создать объект этого класса
class My_class(ABC):
    pass

a = My_class()

# чтобы создать абстрактный класс, нужно еще добавить метод с декоратором
# abstractmethod

class My_class_2(ABC):
    @abstractmethod
    def some_method():
        pass

# b = My_class_2() 
# этод код выдаст ошибку  
# Can't instantiate abstract class My_class_2 with abstract method some_method

"""
Классы дочки от абстрактного класса будут продолжать оставаться абстрактными
до тех пор, пока не реализуют все абстрактные методы
"""

class My_class_3(My_class_2):
    def some_method():
        pass

c = My_class_3() # теперь метод не абстрактный и мы можем создать объект

"""
Если мы хотим создать абстрактный класс от мета класса, то наследовать
метакласс надо не от ABC, а от ABCMeta
"""

class My_class_4(ABCMeta):
    pass