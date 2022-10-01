"""
Write a program that defines a shape class with two properties, 
width and height. Then define two sub-classes triangle and rectangle, 
that calculate the area of the shape. 
"""

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
class Triangle(Shape):
    
    def area(self):
        return 0.5 * self.width * self.height
        
class Rectangle(Shape):
    
    def area(self):
        return self.width * self.height
