import math

class Shape:
    def area(self):
        """Base method for area calculation. Must be overridden by subclasses."""
        raise NotImplementedError("The area() method must be overridden in a subclass.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
from polymorphism_demo import Shape, Rectangle, Circle

def main():
    # Create a list of shapes
    shapes = [
        Rectangle(10, 5),  # Rectangle with length=10, width=5
        Circle(7)          # Circle with radius=7
    ]

    # Demonstrate polymorphism by calling area() on different shapes
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
