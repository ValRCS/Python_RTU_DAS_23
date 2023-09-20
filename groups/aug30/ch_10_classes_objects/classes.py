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
    def __init__(self, name="Robby", model="", battery_level=100, x=0, y=0, secret_key=None):
        print("Starting to create a robot")
        self.name = name
        self.model = model
        self.battery_level = battery_level
        self.x = x
        self.y = y
        # there is concept called information hiding - encapsulation
        # in OOP we want to hide some data from the user
        # let's create a self._nickname attribute
        # this is a convention to indicate that this attribute should not be accessed directly
        # but we can still access it if we want to
        self._nickname = self.name[:3] # this is a convention, not a requirement
        # we can also create a self.__secret_key attribute
        # this is a convention to indicate that this attribute should not be accessed directly
        # and we can not access it directly except by using some special methods
        self.__secret_api_key = secret_key # __secret_api_key is not accessible directly
        # we will create methods to access it so called setters and getters
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

    # let's createa our own __add__ method
    # this will allow us to use + operator on our objects
    # here it will create a new robot with name of both robots combined
    # and combine battery levels
    # and location will be average of both locations
    # this is just an example, you can do whatever you want
    def __add__(self, other):
        # new_robot = Robot()
        # new_robot.name = self.name + other.name
        # new_robot.battery_level = (self.battery_level + other.battery_level) / 2
        # new_robot.x = (self.x + other.x) / 2
        # new_robot.y = (self.y + other.y) / 2
        # first lets create the new attributes
        new_name = self.name + other.name
        new_model = self.model # we can use self.model or other.model, it does not matter
        new_battery_level = self.battery_level + other.battery_level
        new_x = (self.x + other.x) / 2
        new_y = (self.y + other.y) / 2
        # now let's create a new robot
        new_robot = Robot(new_name, new_model, new_battery_level, new_x, new_y)
        return new_robot # i could have returned some other object, but i chose to return a Robot object
    
    # there are many more dunder methods that we can create
    # -, *, /, //, %, **, <, >, <=, >=, ==, !=, etc.

    # let's create a method that returns secret_api_key
    def get_secret_api_key(self):
        # i could add some extra checks and validations here
        # could check if user is authorized to access this key
        return self.__secret_api_key
    
    # let's create a method that sets secret_api_key
    def set_secret_api_key(self, new_key):
        # i could add some extra checks and validations here
        # could check if user is authorized to access this key
        # simple check for length
        if len(new_key) < 8: # 8 should be a constant, but we will leave it for now
            # raise ValueError("Key must be at least 8 characters long")
            print("Key must be at least 8 characters long")
            return self # or return None
        self.__secret_api_key = new_key
        return self # optional for chaining

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
# so now I can create a new robot by adding robby and bb8
print(bb8)
# let's create a new robot by adding robby and bb8
robby_bb8 = robby + bb8  # techincally this is the same as robby.__add__(bb8)
print(robby_bb8) # prints Robot RobbyBB8

# now I can access nickname attribute of robby_bb8 just like regular attribute
print(robby_bb8._nickname) # prints Rob 

# so now I would like to print secret_api_key of say bb8
try:
    print(bb8.__secret_api_key) # this will not work
except AttributeError as e:
    print(e)

# now I get correct secret_api_key
print(bb8.get_secret_api_key()) # prints None
# let's try to set secret_api_key to say 123456 which is too short
bb8.set_secret_api_key("123456") # prints Key must be at least 8 characters long
# now let's try to set secret_api_key to say 123456789 which is long enough
bb8.set_secret_api_key("123456789")
# now I get correct secret_api_key
print(bb8.get_secret_api_key()) # prints 123456789

# now how could we create a flying Robot class that also has z coordinate
#  but otherwise is the same as Robot class

# we could write everything again using copy and paste
# or we could use a concept called inheritance - mantojamība Latviski

# let's create a FlyingRobot class that inherits from Robot class
class FlyingRobot(Robot):
    # i will want to create a custom __init__ method since I have z coordinate
    def __init__(self, name="Robby", model="", battery_level=100, x=0, y=0, z=0, secret_key=None):
        # i could copy and paste everything from Robot class
        # but I will use a concept called super()
        # super() is a reference to the parent class
        # super() is a special method name
        # docs: https://docs.python.org/3/library/functions.html#super
        # super() will run __init__ method of the parent class
        super().__init__(name, model, battery_level, x, y, secret_key)
        # now I can add my own attributes
        self.z = z

    def fly_up(self, distance=1):
        self.z += distance
        self.battery_level -= (distance * 1)

    # let's override print_status method
    def print_status(self):
        # return super().print_status() + f" and z:{self.z}"
        # or easier would be 
        print(f"Robot {self.name} is at {self.x},{self.y},{self.z} with battery level {self.battery_level}")
        return self

# let's create an instance of this class
flying_robot = FlyingRobot("R2D2","A100",50,0,0) # will run __init__ method if it exists
# notice I did not need to pass self parameter, it is automatically passed
print(flying_robot) # prints Robot R2D2 is at 0,0 with battery level 50

flying_robot.fly_up(10)
flying_robot.print_status() # prints Robot R2D2 is at 0,0,10 with battery level 40

# there is another approach as an alternative to inheritance
# it is called composition - kompozīcija Latviski
# idea we create an object of another class inside our class

# let's create a Battery class
class Battery:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.remaining = capacity
    
    def get_capacity(self):
        return self.capacity
    
    def get_remaining(self):
        return self.remaining
    
    def set_remaining(self, new_remaining):
        self.remaining = new_remaining
        return self
    
# let's create an engine class
class Engine:
    def __init__(self, power=100):
        self.power = power
    
    def get_power(self):
        return self.power
    
    def set_power(self, new_power):
        self.power = new_power
        return self
    
class Wheel:
    def __init__(self, size=10):
        self.size = size
    
    def get_size(self):
        return self.size
    
    def set_size(self, new_size):
        self.size = new_size
        return self
    
# let's create a ComposableRobot class that will utilize Battery and Engine and Wheel classes
# Wheels will be passed as a list or tuple

class ComposableRobot:
    def __init__(self, name="Robby", model="", battery=None, engine=None, wheels=None):
        self.name = name
        self.model = model
        self.battery = battery
        self.engine = engine
        self.wheels = wheels
    
    def get_name(self):
        return self.name
    
    def get_model(self):
        return self.model
    
    def get_battery(self):
        return self.battery
    
    def get_engine(self):
        return self.engine
    
    def get_wheels(self):
        return self.wheels
    
    def set_name(self, new_name):
        self.name = new_name
        return self
    
    def set_model(self, new_model):
        self.model = new_model
        return self
    
    def set_battery(self, new_battery):
        self.battery = new_battery
        return self
    
    def set_engine(self, new_engine):
        self.engine = new_engine
        return self
    
    def set_wheels(self, new_wheels):
        self.wheels = new_wheels
        return self
    
    def print_status(self):
        print(f"Robot {self.name} has {self.battery.get_remaining()} battery remaining and {self.engine.get_power()} power")
        print(f"Robot has {len(self.wheels)} wheels of size {self.wheels[0].get_size()}")
        return self
    
# let's make our composable robot instance but first we need some components

# let's create a battery
battery = Battery(100)
# let's create an engine
engine = Engine(100)
# let's create some wheels using list comprehension
wheels = [Wheel(10) for _ in range(4)] # _ is a throwaway variable, we don't care about it

# now we can create our composable robot
composable_robot = ComposableRobot("Robby", "A100", battery, engine, wheels)
composable_robot.print_status() # prints Robot Robby has 100 battery remaining and 100 power
# i can also access battery directly
print(composable_robot.battery.get_remaining()) # prints 100

# another composable robot but we would want new components else they will be sharing same components!!
battery_2 = Battery(50)
engine_2 = Engine(50)
wheels_2 = [Wheel(20) for _ in range(4)] # _ is a throwaway variable, we don't care about it
composable_robot_2 = ComposableRobot("C3PO", "B100", battery_2, engine_2, wheels_2)
# let's print status of both robots
composable_robot.print_status() # prints Robot Robby has 100 battery remaining and 100 power
composable_robot_2.print_status() # prints Robot C3PO has 50 battery remaining and 50 power
