def greet():
    print("Hello, World!")
greet()


def add(a, b):
    return a + b
result = add(5, 3)
print(result)


def find_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
greatest = find_greatest(10, 20, 15)
print(greatest)


def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("racecar"))
print(is_palindrome("hello"))


def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
print(reverse_string("hello"))


def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total
print(sum_list([1, 2, 3, 4]))


add_ten = lambda x: x + 10
print(add_ten(5))


numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)


capitalize_words = lambda s: ' '.join(word.capitalize() for word in s.split())
print(capitalize_words("hello world"))


words = ["hello", "world", "python"]
lengths = list(map(len, words))
print(lengths)


words = ["a", "an", "the", "hello", "world"]
long_words = list(filter(lambda x: len(x) > 3, words))
print(long_words)


from functools import reduce
words = ["hello", "world"]
concatenated = reduce(lambda x, y: x + y, words)
print(concatenated)


numbers = [1, 2, 3, 4, 5, 6]
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(even_squares)


from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
sum_even_squares = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(sum_even_squares)


class MyClass:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print(self.name)
obj = MyClass("Example")
obj.display_name()


class MyClass:
    def my_method(self):
        print("Hello from method!")
obj = MyClass()
obj.my_method()


class MyClass:
    def __init__(self, name):
        self.name = name
obj = MyClass("Example")
print(obj.name) 
del obj.name
del obj


class SimpleClass:
    def __init__(self, value):
        self.value = value
    def display_value(self):
        print(self.value)
obj = SimpleClass(10)
obj.display_value()


class MyClass:
    def __init__(self, value):
        self.value = value
    def display_value(self):
        print(self.value)
obj = MyClass(20)
obj.display_value()


class ExampleClass:
    def __init__(self, text):
        self.text = text
    def show_text(self):
        print(self.text)
example = ExampleClass("Hello, Python!")
example.show_text()


class InstanceDemo:
    def __init__(self, num):
        self.num = num
    def increment_num(self):
        self.num += 1
demo = InstanceDemo(5)
demo.increment_num()
print(demo.num)


class ClassDemo:
    class_var = 0
    def __init__(self):
        ClassDemo.class_var += 1
    @classmethod
    def get_class_var(cls):
        return cls.class_var
demo1 = ClassDemo()
demo2 = ClassDemo()
print(ClassDemo.get_class_var())


class StaticDemo:
    @staticmethod
    def static_method():
        print("This is a static method")
StaticDemo.static_method()


class EncapsulationDemo:
    def __init__(self):
        self._protected_var = "I am protected"
        self.__private_var = "I am private"
    def get_private_var(self):
        return self.__private_var
demo = EncapsulationDemo()
print(demo._protected_var)
print(demo.get_private_var())


class Parent:
    def parent_method(self):
        print("Parent method")
class Child(Parent):
    def child_method(self):
        print("Child method")
child = Child()
child.parent_method()
child.child_method()


class Parent:
    def show(self):
        print("Parent show method")
class Child(Parent):
    def show(self):
        print("Child show method")
child = Child()
child.show() 


class Parent1:
    def parent1_method(self):
        print("Parent1 method")
class Parent2:
    def parent2_method(self):
        print("Parent2 method")
class Child(Parent1, Parent2):
    def child_method(self):
        print("Child method")
child = Child()
child.parent1_method()
child


class Grandparent:
    def grandparent_method(self):
        print("Grandparent method")
class Parent(Grandparent):
    def parent_method(self):
        print("Parent method")
class Child(Parent):
    def child_method(self):
        print("Child method")
child = Child()
child.grandparent_method()
child.parent_method()
child.child_method()


class Parent:
    def parent_method(self):
        print("Parent method")
class Child1(Parent):
    def child1_method(self):
        print("Child1 method")
class Child2(Parent):
    def child2_method(self):
        print("Child2 method")
child1 = Child1()
child2 = Child2()
child1.parent_method()
child1.child1_method() 
child2.parent_method()
child2.child2_method()


class Parent:
    def show(self):
        print("Parent show method")
class Child(Parent):
    def show(self):
        super().show()
        print("Child show method")
child = Child()
child.show()

