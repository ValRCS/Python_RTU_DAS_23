# we can create a class that has class methods and static methods
# idea we can use the class to group functions together that are related

class MyMath:
    PI = 3.1415926
    # class method for area of circle
    @classmethod
    def area_of_circle(cls, radius):
        return cls.PI * radius * radius

    # static method
    @staticmethod
    def add(a, b): # notice NO SELF needed
        return a + b

    # static method
    @staticmethod
    def subtract(a, b):
        return a - b
    
# these are usable immediately without any object creation

print(MyMath.PI)
print(MyMath.area_of_circle(5))
print(MyMath.add(5, 6))
print(MyMath.subtract(5, 6))

# i could create an object if I needed to
m = MyMath()
print(m.PI)
print(m.area_of_circle(5))
# not much point unless there is some data to keep inside
# and also if we need some methods to change that data