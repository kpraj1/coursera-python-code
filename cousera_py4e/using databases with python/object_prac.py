

'''
__init__(self): equivalent to constructor and self is equivalent to this,
if you want to initialize or do something when object was created, you can do inside this function
'''
#constructor without any arguments but initializing a variable on object creation
# class PartyAnimal:
#     def __init__(self):
#         self.x=2
#
#     def party(self):
#         self.x = self.x +1
#         print("so far with 2 initial value, x value is",self.x)
#
# an = PartyAnimal()
# y = an.x
# print("x value initial is ",y)
#
# an.party()
# an.party()
# an.party()

# ✅ Demonstrating constructor behavior, class variables, instance methods, class methods, static methods,
# object destruction (__del__), and Python’s dynamic typing

class Person:
    # ✅ Class variable (shared across all instances; accessed via class or instances)
    animal_type = "homo sapiens"

    # ✅ Constructor (__init__) with one required argument (age) and one optional argument (name)
    def __init__(self, age, name="xxx"):
        # Instance variables (unique to each object)
        self.name = name
        self.age = age
        print(f"I am constructed with name: {self.name} and age: {self.age}")

    # ✅ Instance method: accesses instance data using 'self'
    def say_hello(self):
        print(f"Hi, I am {self.name}, and I am {self.age} years old.")

    # ✅ Class method: receives the class (not an instance) as 'cls'
    @classmethod
    def cls_method(cls):
        print(f"Hi, I am accessing class variable animal_type = {cls.animal_type} from a class method.")

    # ✅ Static method: receives neither class nor instance by default
    # Acts like a utility/helper function tied to the class's namespace
    @staticmethod
    def is_adult(age):
        return age >= 18

    # ✅ Destructor method: called when the object is about to be destroyed
    def __del__(self):
        print('I am destructed -', self.name)

# ✅ Creating instances using various argument styles

# Keyword arguments: Order doesn't matter
p = Person(name="Alice", age=24)

# Positional arguments: Order matters; demonstrates dynamic typing (age as string)
q = Person("century", "stark lord")

# One argument only: 'age' gets value "2", default value "xxx" is used for name
r = Person("2")

# ✅ Calling instance methods the usual way
p.say_hello()
q.say_hello()
r.say_hello()

# ✅ Calling instance methods using class name by passing the instance manually
# Demonstrates that methods are just functions with the instance as the first argument
print("\nCalling instance method using the class name and passing the instance explicitly:")
Person.say_hello(p)
Person.say_hello(q)
Person.say_hello(r)

# ✅ Accessing class variable from instances
print(f"\np is a {p.animal_type}, q is a {q.animal_type}, r is a {r.animal_type}")

# ✅ Accessing class variable directly from the class
print(f"Accessing class variable directly: {Person.animal_type}")

# ✅ Class method can be called from the class or from an instance
Person.cls_method()
p.cls_method()

# ✅ Static method behaves the same whether called on class or instance
print("Is 24 an adult?", Person.is_adult(24))
print("Is 16 an adult?", p.is_adult(16))

# 🔍 Uncomment these lines to inspect class internals
# print(type(Person))         # Shows that 'Person' is of type 'type'
# print(dir(Person))          # Lists all attributes/methods of the Person class
#print(type(p))              # Will now show <class '__main__.Person'>
#print(type(p.age))          # Will show <class 'int'>



# ✅ Demonstrating Python's dynamic typing
# Now 'p' is no longer a Person object — it is reassigned to an int
p = 42
print(f"\nVoilà! Now 'p' is not a Person object, but holds the value {p} (type: {type(p)})")




