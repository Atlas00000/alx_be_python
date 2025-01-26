import math

class Shape:
    def area(self):
        """Base method to calculate the area. Should be overridden in subclasses."""
        raise NotImplementedError("Subclasses must override the area method")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle: length × width."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle: π × radius²."""
        return math.pi * (self.radius ** 2)
