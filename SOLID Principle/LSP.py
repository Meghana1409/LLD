'''
The Liskov substitution principle (LSP) was introduced by Barbara Liskov at an OOPSLA conference in 1987. Since then, this principle has been a fundamental part of object-oriented programming. 

The principle states that: Subtypes must be substitutable for their base types.

this principle is about making your subclasses behave like their base classes without breaking anyone’s expectations when they call the same methods. 
'''

# shapes_lsp.py

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value

'''
In this snippet of code, you’ve defined Square as a subclass of Rectangle. 
As a user might expect, the class constructor takes only the side of the square as an argument. Internally, the .__init__() method initializes the parent’s attributes, .width and .height, with the side argument.

You’ve also defined a special method, .__setattr__(), to hook into Python’s attribute-setting mechanism and intercept the assignment of a new value to either the .width or .height attribute. 
Specifically, when you set one of those attributes, the other attribute is also set to the same value,  this violates the Liskov substitution principle because you can’t replace instances of Rectangle with their Square counterparts.

When someone expects a rectangle object in their code, they might assume that it’ll behave like one by exposing two independent .width and .height attributes. 
Meanwhile, your Square class breaks that assumption by changing the behavior promised by the object’s interface. That could have surprising and unwanted consequences, which would likely be hard to debug.

While a square is a specific type of rectangle in mathematics, the classes that represent those shapes shouldn’t be in a parent-child relationship if you want them to comply with the Liskov substitution principle.
'''

#solution
# shapes_lsp.py

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

'''
Shape becomes the type that you can substitute through polymorphism with either Rectangle or Square, which are now siblings rather than a parent and a child. 
Notice that both concrete shape types have distinct sets of attributes, different initializer methods, and could potentially implement even more separate behaviors. 
The only thing that they have in common is the ability to calculate their area.

'''
