
# Objects in the OOP sense are conglomerates of data
# (instance variables) and behavior (methods). 
# A sort method on a list class makes sense, because the
# elements in the list (the data) are being sorted (the behavior). 
# A method in a list class which adds two numbers you provide to 
# it doesn't belong in that class, since it has nothing to do with
# the list data. It should be a standalone function. 
# The whole point of putting a method in a class is to give 
# it access to a particular instance's variables. 
# If it doesn't need that access, 
# it should generally be a standalone function, not a method.






#Основные понятия объектно-ориентированного программирования
#Объектно-ориентированное программирование (ООП) является 
#методологией разработки программного обеспечения, 
#в основе которой лежит понятие класса и объекта, при этом 
#сама программа создается как некоторая совокупность объектов,
# которые взаимодействую друг с другом и с внешним миром. 
#Каждый объект является экземпляром некоторого класса. 
#Классы образуют иерархии. Более подробно о понятии ООП можно прочитать на википедии.

#Выделяют три основных “столпа” ООП- это инкапсуляция, наследование и полиморфизм.

#Инкапсуляция
#Под инкапсуляцией понимается объединение в рамках одной сущности (класса) 
#определенных данных и методов для работы с ними (и не только). 
#Например, можно определить класс “холодильник”, который будет
#содержать следующие данные: производитель, объем, количество камер хранения,
#потребляемая мощность и т.п., и методы: открыть/закрыть холодильник,
#включить/выключить. 
#При этом класс становится новым типом данных в рамках 
#разрабатываемой программы. Можно создавать переменные этого нового типа,
#такие переменные называются объекты.

#Наследование
#Под наследованием понимается возможность создания нового класса на базе существующего.
#Наследование предполагает наличие отношения “является” между классом наследником
#и классом родителем.
#При этом класс потомок будет содержать те же атрибуты и методы,
#что и базовый класс, но при этом его можно (и нужно) расширять
#через добавление новых методов и атрибутов.

#Примером базового класса, демонстрирующего наследование, 
#можно определить класс “автомобиль”, имеющий атрибуты: масса,
#мощность двигателя, объем топливного бака и методы: завести и заглушить.
#У такого класса может быть потомок – “грузовой автомобиль”, 
#он будет содержать те же атрибуты и методы, что и класс “автомобиль”,
#и дополнительные свойства: количество осей, мощность компрессора и т.п..

#Полиморфизм
#Полиморфизм позволяет одинаково обращаться с объектами, 
#имеющими однотипный интерфейс, независимо от внутренней реализации объекта.
#Например с объектом класса “грузовой автомобиль” можно производить те же операции,
#что и с объектом класса “автомобиль”, т.к. первый является наследником второго, при этом обратное утверждение неверно (во всяком случае не всегда). Другими словами полиморфизм предполагает разную реализацию методов с одинаковыми именами. Это очень полезно при наследовании, когда в классе наследнике можно переопределить методы класса родителя.

#Классы в Python
#Создание классов и объектов
#Создание класса в Python начинается с инструкции class. Вот так будет выглядеть минимальный класс.

class C:
#Класс состоит из объявления (инструкция class), 
#имени класса (нашем случае это имя C) и тела класса, 
#которое содержит атрибуты и методы (в нашем минимальном классе есть только одна инструкция pass).

#Для того чтобы создать объект класса необходимо воспользоваться следующим синтаксисом:
имя_объекта = имя_класса()

#Класс может содержать аттрибуты и методы. 
#Ниже представлен класс, содержащий атрибуты color (цвет), width (ширина), height (высота).
class Rectangle:
	color = “green”
	width = 100
	height = 100

#Доступ к аттрибуту класса можно получить следующим образом.
имя_объекта.атрибут
rect1 = Rectangle()
print(rect1.color)

#Добавим к нашему классу метод. 
#Метод – это функция находящаяся внутри класса, 
#выполняющая определенную работу, которая, чаще всего, 
#предполагает доступ к атрибутам созданного объекта. 
#Например, нашему классу Rectangle, можно добавить метод, 
#считающий площадь прямоугольника. 
#Для того, чтобы метод в классе знал, с каким объектом он работает 
#(это нужно для того, чтобы получить доступ к атрибутам: 
#ширина (width) и высота (height)), первым аргументом ему следует 
#передать параметр self, через который он может получить доступ к своим данным.
class Rectangle:
   color = "green"
   width = 100
   height = 100
   def square(self):
	   return self.width * self.height

#Тогда, наша конечная программа, демонстрирующая работу 
#с атрибутами и методами, будет выглядеть так:
class Rectangle:
   color = "green"
   width = 100
   height = 100
   def square(self):
	   return self.width*self.height

rect1 = Rectangle()
print(rect1.color)
print(rect1.square())
rect2 = Rectangle()
rect2.width = 200
rect2.color = "brown"
print(rect2.color)
print(rect2.square())


#Конструктор класса
#Конструктор класса позволяет задать определенные параметры объекта при его создании. 
#Таким образом появляется возможность создавать объекты с уже заранее заданными атрибутами. 
#Конструктором класса является метод:
 __init__(self)

#Например, для того, чтобы иметь возможность задать цвет, 
#длину и ширину прямоугольника при его создании, добавим к классу 
#Rectangle следующий конструктор:
class Rectangle:
   def __init__(self, color="green", width=100, height=100):
	   self.color = color
	   self.width = width
	   self.height = height

   def square(self):
	   return self.width * self.height

rect1 = Rectangle()
print(rect1.color)
print(rect1.square())
rect1 = Rectangle("yellow", 23, 34)
print(rect1.color)
print(rect1.square())

#Наследование
#В организации наследования участвуют как минимум два класса: 
#класс родитель и класс потомок. 
#При этом возможно множественное наследование, 
#в этом случае у класса потомка есть несколько родителей. 
#Не все языки программирования поддерживают множественное наследование, 
#но в Python можно его использовать.

#Синтаксически создание класса с указанием его родителя/ей выглядит так:
class имя_класса(имя_родителя1, [имя_родителя2,…, имя_родителя_n])

#Доработаем наш пример так, чтобы в нем присутствовало наследование.
class Figure:
   def __init__(self, color):
	   self.color = color

   def get_color(self):
	   return self.color


class Rectangle(Figure):
   def __init__(self, color, width=100, height=100):
	   super().__init__(color)
	   self.width = width
	   self.height = height

   def square(self):
	   return self.width*self.height

rect1 = Rectangle("blue")
print(rect1.get_color())
print(rect1.square())
rect2 = Rectangle("red", 25, 70)
print(rect2.get_color())
print(rect2.square())

#Полиморфизм
#Как уже было сказано во введении в рамках ООП полиморфизм, 
#как правило, используется с позиции переопределения методов 
#базового класса в классе наследнике. 
#Проще всего это рассмотреть на примере. 
#Добавим в наш базовый класс метод info(), 
#который печатает сводную информацию по объекту класса 
#Figure и переопределим этот метод в классе Rectangle, 
#где добавим дополнительные данные и вывод.
class Figure:
   def __init__(self, color):
	   self.color = color
	  
   def get_color(self):
	   return self.color
	  
   def info(self):
	   print("Figure")
	   print("Color: " + self.color)


class Rectangle(Figure):
   def __init__(self, color, width=100, height=100):
	   super().__init__(color)
	   self.width = width
	   self.height = height

   def square(self):
	   return self.width * self.height

   def info(self):
	   print("Rectangle")
	   print("Color: " + self.color)
	   print("Width: " + str(self.width))
	   print("Height: " + str(self.height))
	   print("Square: " + str(self.square()))

fig1 = Figure("green")
print(fig1.info())
rect1 = Rectangle("red", 24, 45)
print(rect1.info())
#Таким образом наследник класса может расширять и модифицировать функционал класса родителя.