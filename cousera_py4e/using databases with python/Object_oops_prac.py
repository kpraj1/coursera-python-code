
#1. Inheritance – Reusing code from parent classes
# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Dog(Animal):  # Dog inherits from Animal
#     def bark(self):
#         print("Dog barks")
#
# d = Dog()
# d.speak()  # Inherited
# d.bark()   # Own method

#-----------------------------------------------------------------------------------------

#2. Method Overriding – Redefining a parent method in child class

# class Animal:
#         def speak(self):
#             print("Animal speaks")
#         def identity(self):
#             print("I belong to Animal class")
#
# class Dog(Animal):
#         def speak(self):  # Overrides base class method
#             print("Dog barks")
#         def identity(self):# Overrides but also includes parent's method
#             super().identity()
#             print("my sub class belong to canine")
#
#
# d = Dog()
# d.speak()  # Outputs: Dog barks
# d.identity()


#-----------------------------------------------------------------------------------------

# 3. Access Modifiers – Controlling access (Python uses naming conventions, not true enforcement)
# Public: No underscore prefix
#
# Protected: One underscore _var (convention)
#
# Private: Two underscores __var (name mangling)

# class Example:
#     def __init__(self):
#         self.public = "I'm public"
#         self._protected = "I'm protected"
#         self.__private = "I'm private"
#
# e = Example()
# print(e.public)       # ✅ Accessible
# print(e._protected)   # ⚠️ Conventionally not accessed directly
# # print(e.__private)  # ❌ AttributeError
# print(e._Example__private)  # ✅ Works due to name mangling

#-----------------------------------------------------------------------------------------

# 4. Encapsulation – Bundling data (attributes) and methods that operate on that data

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private variable
#
#     def deposit(self, amount):
#         self.__balance += amount
#
#     def get_balance(self):
#         return self.__balance
#
# acc = BankAccount(1000)
# acc.deposit(500)
# print(acc.get_balance())  # ✅ Outputs: 1500
# # print(acc.__balance)    # ❌ Will fail

#-----------------------------------------------------------------------------------------

# 5. Abstraction – Hiding implementation details, showing only the essential features
# Python achieves this via abstract base classes (ABC) from abc module:

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass  # Abstract method
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# # s = Shape()        # ❌ Can't instantiate abstract class
# c = Circle(5)
# print(c.area())      # ✅ Works


#-----------------------------------------------------------------------------------------

#6. Polymorphism – Same interface, different behavior

# class Dog:
#     def speak(self):
#         return "Woof"
#
# class Cat:
#     def speak(self):
#         return "Meow"
#
# # The animal in animal_sound(animal) is not a specific class — it's just a generic parameter that accepts any object as long as it has a .speak() method.
# # This is a key example of duck typing in Python — if an object behaves like a duck (i.e., has a .speak() method), Python doesn't care about its actual class.
#
# def animal_sound(animal):
#     print(animal.speak())
#
# dog = Dog()
# cat = Cat()
#
# animal_sound(dog)  # Woof
# animal_sound(cat)  # Meow

#-----------------------------------------------------------------------------------------

#7. Multiple Inheritance – A class inherits from more than one base class


# class A:
#     def show(self):
#         print("A")
#
#
# class B:
#     def show(self):
#         print("B")
#
#
# class C(A, B):
#     pass
#
# class D(B, A):
#     pass
#
#
# c = C()
# c.show()  # Will call A's show() due to Method Resolution Order (MRO)
# d = D()
# d.show() # Will call B's show() due to Mehtod Resolution Order (MRO)

#-----------------------------------------------------------------------------------------

#8. Mixins – A type of multiple inheritance used to add functionality

# class LogMixin:
#     def log(self, msg):
#         print(f"LOG: {msg}")
#
# class Processor(LogMixin):
#     def process(self):
#         self.log("Processing started...")
#
# p = Processor()
# p.process()

#-----------------------------------------------------------------------------------------
#@property: Turns the celsius() method into a getter.

#@celsius.setter: Defines the setter for celsius.

# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius
#
#     @property
#     def fahrenheit(self):
#         return (self._celsius * 9/5) + 32
#
#     @property
#     def celsius(self):
#         return self._celsius
#
#     @celsius.setter
#     def celsius(self, value):
#         if value < -273.15:
#             raise ValueError("Temperature can't go below absolute zero!")
#         self._celsius = value
#
# t = Temperature(2)
# print(t.fahrenheit,"f")
# t.celsius = 5
# print(t.fahrenheit,"f")