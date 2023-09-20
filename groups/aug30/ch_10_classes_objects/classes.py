# classes and objects in Python
# official documentation: https://docs.python.org/3/tutorial/classes.html

# a class is a blueprint/template for creating objects
# objects are instances of a class
# you can create many objects from a class definition
# with class we provide structure for combining data and functionality together

# let's check out some types
# turns out pretty much everything in Python is an object based on some class definition
print(type(9000))
print(type("hello"))
print(type([1,2,3]))
print(type((1,2,3)))
print(type({1,2,3}))
print(type({"a":1,"b":2,"c":3}))
print(type(range(10)))
print(type(print))

# so classes let us create our own types with our own attributes and methods
# attributes are variables that belong to a class
# methods are functions that belong to a class

# let's see why we would need a class
# we want to create many similar robots
# we want to store some data about each robot
# say battery level, name, model, x, y coordinates, etc.
# we have some actions that we want to perform on each robot
# how to store each robot's data and functionality in a single place?

# absolutely worst way to do it is to create a bunch of variables
# robot1_name = "R2D2"
# robot1_model = "A100"
# robot1_battery_level = 50
# robot1_x = 0
# robot1_y = 0
# def robot1_move_up():
#     global robot1_y
#     robot1_y += 1
# DO NOT DO THIS!

# slightly better would be a list of lists approach
# each inner list would be a single robot
# robots = [
#     ["R2D2","A100",50,0,0],
#     ["C3PO","B100",40,0,0],
#     ["BB8","A100",60,0,0],
# ]
# def move_up(robot):
#     robot[4] += 1 # see the issues here? we have to remember that y coordinate is at index 4

# finally a reasonable approach would be to use a dictionary
# each robot would be a dictionary
# robots = [
#     {"name":"R2D2","model":"A100","battery_level":50,"x":0,"y":0},
#     {"name":"C3PO","model":"B100","battery_level":40,"x":0,"y":0},
#     {"name":"BB8","model":"A100","battery_level":60,"x":0,"y":0},
# ]
# def move_up(robot):
#     robot["y"] += 1 # much better, but still not ideal

# we have a list of dictionary approach
# one problem is that our functions are not part of the robot
# for larger programs this can get messy
# in our example our function is called move_up and it is not clear who or what will be moved up

# let's see how we can use classes to solve this problem
# let's start with completely empty class
class EmptyClass:
    pass # pass is a keyword that does nothing, but it is required for an empty class

# let's create an instance of this class
empty_object = EmptyClass() # class names in Python are generally capitalized and use CamelCaseMyClass so on
print(empty_object) # prints some address in memory
# i can attach attributes to this object
empty_object.name = "R2D2"
empty_object.model = "A100"
another_empty_object = EmptyClass()
another_empty_object.name = "C3PO"
another_empty_object.model = "B100"
# and so on
# this is far from ideal because we have to attach attributes manually, defeats the purpose of a class
# still this shows that I can attach extra data to an object at any time

# now let's create a SimpleRobot class with some values already attached
class SimpleRobot:
    name = "R2D2"
    model = "A100"
    battery_level = 50
    x = 0
    y = 0

# above class is a template for creating objects

# let's create an instance of this class
robot1 = SimpleRobot()
print(robot1) # prints some address in memory
# print name
print(robot1.name) # prints R2D2
# another robot
robot2 = SimpleRobot()
print(robot2.name) # prints R2D2 again
# change name
robot2.name = "C3PO"
print(robot2.name) # prints C3PO
# but robot1 name is still R2D2
print(robot1.name) # prints R2D2

# so above is an improvement for creating objects
# still we would like to supply some data when creating an object

# let's create a Robot class with a constructor - technically in Python it runs after an object is created

class Robot:
    # let's create an init method
    # init method is a constructor that runs immediately after an object is created
    # self is a reference to the object itself
    # we can use self to attach attributes to the object
    # self is the first parameter of every method in a class
    # __init__ is a special method name
    # there are about 100 special method names in Python
    # they all start and end with double underscores
    # docs: https://docs.python.org/3/reference/datamodel.html#special-method-names
    def __init__(self, name="Robby", model="", battery_level=100, x=0, y=0):
        print("Starting to create a robot")
        self.name = name
        self.model = model
        self.battery_level = battery_level
        self.x = x
        self.y = y
        print(f"Robot named {self.name} created")

    # typically we will want to create a __str__ method
    # by default print object prints address in memory
    # we might want to print something more meaningful
    # __str__ is a special method name
    # docs: https://docs.python.org/3/reference/datamodel.html#object.__str__
    # only requirement is that we return a string
    def __str__(self):
        # i could do some stuff here - prepare a string
        return f"Robot {self.name} is at x:{self.x},y:{self.y} battery level:{self.battery_level}"

    # let's create our own method that prints status of the robot
    # name is up to us, but it is a good idea to use a verb at start
    def print_status(self): # again self is a reference to the object itself
        print(f"Robot {self.name} is at {self.x},{self.y} with battery level {self.battery_level}")
        return self # this is not required, but it is a good idea to return self if nothing else is returned

    # now let's create some movement methods
    # let's start with move up
    def move_up(self, distance=1):
        self.y += distance
        self.battery_level -= (distance * 0.5) # 0.5 should be a constant, but we will leave it for now
        return self

# we made a method that moves in any direction
    def move_robot(self, delta_x=0, delta_y=0, battery_drain_factor = 0.5):
        self.x += delta_x
        self.y += delta_y
        # simplified battery drain calculation
        self.battery_level -= (abs(delta_x) + abs(delta_y)) * battery_drain_factor
        return self

# let's create an instance of this class
r2d2 = Robot("R2D2","A100",50,0,0) # will run __init__ method if it exists
# notice I did not need to pass self parameter, it is automatically passed
c3p0 = Robot("C3PO","B100",40,0,0)
bb8 = Robot(name="BB8",
            model="A100",
            battery_level=60,
            x=0,
            y=0) # full syntax, but not required

# thus I have created 3 objects from the same Robot class
# each have their own attributes(data) and methods(functionality)
# each object is independent of each other

# let's print status of each robot
r2d2.print_status() # prints Robot R2D2 is at 0,0 with battery level 50
c3p0.print_status() # prints Robot C3PO is at 0,0 with battery level 40
bb8.print_status() # prints Robot BB8 is at 0,0 with battery level 60
bb8.move_up() # moves up by 1
bb8.print_status() # prints Robot BB8 is at 0,1 with battery level 59.5
bb8.move_up(5) # moves up by 5
bb8.print_status() # prints Robot BB8 is at 0,6 with battery level 56.5
# remember print object by default prints address in memory
print(bb8) # prints <__main__.Robot object at 0x7f8e2f0a7e80> by default
# if class has user defined __str__ method, it will be called instead

# let's move r2d2
r2d2.move_up(10)
r2d2.print_status() # prints Robot R2D2 is at 0,10 with battery level 45.0
r2d2.move_robot(delta_x=5, delta_y= -4)
r2d2.print_status() # prints Robot R2D2 is at 5,6 with battery level 42.0
# now I can create a robot with default values
robby = Robot() # prints Starting to create a robot, Robot named Robby created
print(robby) # prints Robot Robby is at 0,0 with battery level 100

# now with return self i can CHAIN methods
robby.move_up(5).move_up(13).move_robot(delta_x=5, delta_y= -4).print_status()