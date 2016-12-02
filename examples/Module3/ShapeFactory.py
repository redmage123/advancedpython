#!/usr/bin/python3

# This is an example of the factory design pattern. 

class ShapeFactory(object):

    def __init__(self):
        pass

# We create a shape based upon what type of shape is passed into the method.

    def createShape(self,shapeType):
        if  shapeType == 'circle':
            return Circle.create(self)
        elif shapeType == 'Rectangle':
            return Rectangle.create(self)
        else:
            return Square.create(self)

# The base Shape class
class Shape(object):
    def __init__(self):
        pass
    def draw(self):
        pass

# Circle class derived from Shape
class Circle(Shape):
    def __init__(self):
        pass
    def create(self):
        return Circle
    def draw(self):
        print ("Inside circle draw")

# Rectangle class derived from Shape
class Rectangle(Shape):
    def __init__(self):
        pass
    def create(self):
        return Rectangle
    def draw(self):
        print ("Inside rectangle draw")

# Square class derived from Shape
class Square(Shape):
    def __init__(self):
        pass
    def create(self):
        return Square
    def draw(self):
        print ("Inside square draw")

sf = ShapeFactory()
s1 = sf.createShape('Circle')
s2 = sf.createShape('Square')
s3 = sf.createShape('Rectangle')

print (s1.draw(s1))
print (s2.draw(s2))
print (s3.draw(s3))




























