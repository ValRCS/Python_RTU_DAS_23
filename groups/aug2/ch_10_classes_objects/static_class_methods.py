# we can define static and class methods that can be called without creating an instance of
#  the class

class Math:
    PI = 3.141592653589793

    # now I would like to create a class method that can be called without creating an instance
    #  of the class
    # we use so called "decorators" to define class methods

    @classmethod
    def circle_area(cls, radius): # note cls instead of self
        # cls is a reference to the class itself
        return cls.PI * radius ** 2
    # lets create a static add method
    # we use so called "decorators" to define static methods
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    # compare with regular method
    def multiply(self, x, y):
        return x * y # so self was not really needed here
    
    # i could add normal __init__ method if I plan to use this class as well
    #  as create instances of it



# i can use them immediately
print(Math.add(1, 2))
print(Math.subtract(1, 20))
# i can not use multiply without creating an instance of the class
try:
    print(Math.multiply(1, 2))
except Exception as e:
    print(e) # error message will indicate that multiply takes 3 arguments, but only 2 were given
    # because we are missing object reference

# i could use it for area of a circle
print(Math.circle_area(10))

# class and static methods can be used for utility functions for grouping functions

# of course i can create objects of this class
my_math = Math()
print(my_math.add(1, 2)) # will also work but not needed here
# now we can use multiply
print(my_math.multiply(10, 2))