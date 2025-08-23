'''
The open-closed principle (OCP) for object-oriented design was originally introduced by Bertrand Meyer in 1988 and means that:

Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
'''
# shapes_ocp.py

from math import pi

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2
                                                                                              
>>> from shapes_ocp import Shape

>>> rectangle = Shape("rectangle", width=10, height=5)
>>> rectangle.calculate_area()
50
>>> circle = Shape("circle", radius=5)
>>> circle.calculate_area()
78.53981633974483
'''

The initializer of Shape takes a shape_type argument that can be either "rectangle" or "circle". 
It also takes a specific set of keyword arguments using the **kwargs syntax. If you set the shape type to "rectangle", then you should also pass the width and height keyword arguments so that you can construct a proper rectangle.

In contrast, if you set the shape type to "circle", then you must also pass a radius argument to construct a circle.
Imagine that you need to add a new shape, maybe a square.
How would you do that? Well, the option here is to add another elif clause to .__init__() and to .calculate_area() so that you can address the requirements of a square shape.

Having to make these changes to create new shapes means that your class is open to modification. That violates the open-closed principle.
'''
#solution
# shapes_ocp.py

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2
'''                                                                                           
In this code, you completely refactored the Shape class, turning it into an abstract base class (ABC). This class provides the required interface (API) for any shape that you’d like to define. 
That interface consists of a .shape_type attribute and a .calculate_area() method that you must override in all the subclasses.

Note: The example above and some examples in the next sections use Python’s ABCs to provide what’s called interface inheritance. In this type of inheritance, subclasses inherit interfaces rather than functionality. 
In contrast, when classes inherit functionality, then you’re presented with implementation inheritance.
This update closes the class to modifications. Now you can add new shapes to your class design without the need to modify Shape.
In every case, you’ll have to implement the required interface, which also makes your classes polymorphic.
'''

This update closes the class to modifications. Now you can add new shapes to your class design without the need to modify Shape.
