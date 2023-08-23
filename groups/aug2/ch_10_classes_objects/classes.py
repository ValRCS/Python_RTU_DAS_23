# Let's talk about classes and objects in Python

# a class is a blueprint/template for an object
# then object is an instance of a class 
# object is a concrete thing/realization that is created from a class
# we uses classes and objects to model real world things
# we store data in objects and we can perform operations/functions/methods on objects
# so using classes we can store data and functions that work on this data together

# so first everything is an object in Python
# let's check the type of some objects
print(type(1))
print(type(3.141592653589793))
print(type("Valdis"))
print(type([1,2,3,4,5]))
print(type((1,2,3,4,5)))
print(type({"name":"Valdis", "age":99}))
print(type({"Valdis", "Voldemars", "Voldemārs"})) # this is a set
print(type(True)) # this is a bool

# official docs on classes https://docs.python.org/3/tutorial/classes.html

# first let's do some work without classes and objects
# let's say I want to make a robot that can move around

# I will need to store name, x and y coordinates, and direction
# also weight and height, and some other things

# we could use a list to store this information
robot1 = ["Robocop", 0, 0, "N", 100, 200, "red", "blue", "green"]
# it will be very awkward to work with this list
# we will need to remember what each index means
# we will need to remember what type of data is stored in each index
# we will need to remember what operations we can do with each index

# better approach would be to use a dictionary
robot2 = {"name":"Robocop", 
          "x":0, 
          "y":0, 
          "direction":"N", 
          "weight":100, 
          "height":200, 
          "colors":["red", "blue", "green"],
          "motto":"Serve the public trust, Protect the innocent, Uphold the law",
            "weapons":["machine gun", "rocket launcher", "taser", "flamethrower"],
            "battery":100
          
          }

# so what type will be robot2?
print(f"robot2 is of type {type(robot2)}")
# we can get the name of the robot
print(f"robot2 name is {robot2['name']}")
# we can get the x coordinate
print(f"robot2 x is {robot2['x']}")

# let's create a function to print status of the robot
def print_robot_status(robot):
    print(f"Robot {robot['name']} is at {robot['x']},{robot['y']} facing {robot['direction']}")
    print(f"Robot {robot['name']} has battery level {robot['battery']}")


# then we could create some functions to move the robot
def move_north(robot, steps=1, battery_drain=1):
    robot["y"] += steps
    robot["direction"] = "N"
    robot["battery"] -= battery_drain*steps  # could be a hardware call to check battery
    # we do not need to return anything since we are modifying the robot dictionary
    # so we are changing the state of the robot we passed in
    return robot # returns the same robot we passed in, but with some changes to state

def move_south(robot, steps=1, battery_drain=1):
    robot["y"] -= steps
    robot["direction"] = "S"
    robot["battery"] -= battery_drain*steps # right side will be evaluated first
    return robot

def move_east(robot, steps=1, battery_drain=1):
    robot["x"] += steps
    robot["direction"] = "E"
    robot["battery"] -= battery_drain*steps 
    return robot

def move_west(robot, steps=1, battery_drain=1):
    robot["x"] -= steps
    robot["direction"] = "W"
    robot["battery"] -= battery_drain*steps 
    return robot


# let's try to move our robot
# first let's print the status
print_robot_status(robot2)
# then let's move it 5 steps north
robot2 = move_north(robot2, 5)
# then let's print the status again
print_robot_status(robot2)
# lets go 3 steps east
robot2 = move_east(robot2, 3)
print_robot_status(robot2)

# we could create many more functions to move the robot, to turn the robot, to shoot, etc.
# to ask the robot to do something we would need to call a function

# the issue is that all these functions are not connected to the robot

# so it is very hard for someone to start using our robot
# even ourselves we would need to remember all the functions and what they do
# it is not easy after a while to remember what each function does

# with classes we could store all the data and functions together

# lets's start with an empty class

class EmptyRobot:
    pass # this is a placeholder for now so empty template/class is valid

# now we could use it to store data but first we need to create an instance of the class
# we can create an instance of a class by calling the class name with ()

robot3 = EmptyRobot() # we create a new object of type EmptyRobot
robot3.name = "Robocop" 
robot3.x = 0
robot3.y = 0
robot3.direction = "N"
# we could even attach functions to this object but it is not recommended at beginner level

# now we can print the status of the robot
print(robot3.name, robot3.x, robot3.y, robot3.direction)
print(f"robot3 is of type {type(robot3)}")
print(robot3) # prints the memory address of the object - we can change this with __str__ method

# so empty class provided us with a way to store data but not very convenient

# better idea would be to create a class which already has some data and functions
# let's make a simple robot class
class SimpleRobot: #note that we use CamelCase for class names not snake_case as for functions
    name = "Robocop" # this is a class variable, it is shared by all instances of the class
    x = 0 # these are also class variables
    y = 0
    direction = "N"
    battery = 100

    # we can also add functions to the class
    # functions defined inside a class are called methods in Python
    def print_status(self): # note that we need to pass self as first argument
        # self refers to particular instance/object of the class
        print(f"Robot {self.name} is at {self.x},{self.y} facing {self.direction}")
        print(f"Robot {self.name} has battery level {self.battery}")

simple_robot1 = SimpleRobot() # we create a new object of type SimpleRobot
simple_robot1.print_status() # we can call the method on the object
# note how we do not need to pass any arguments to the method , self is automatically passed

another_simple_robot = SimpleRobot() # we create another object of type SimpleRobot
# this object is completely separate from the first object - simple_robot1
another_simple_robot.print_status() # we can call the method on the object
another_simple_robot.name = "Terminator" # we can change the name of this object
another_simple_robot.print_status() # we can call the method on the object

# even better would be if we could pass in some data when we create the object
# for that we will create a Robot class which will have an __init__ method which will be called when we create an object

class Robot:
    # Robot will have a name, x and y coordinates, direction, battery level
    # we want to pass this data when we create the object
    # we can do that by using __init__ method
    # __init__ method is called when we create an object
    # __init__ method is called a constructor - technically it is not a constructor, it is called right after the object is created
    # __init__ method is called an initializer - more correct term

    # we can pass in data to __init__ method
    # methods with __ in front and back are called magic methods - dunder methods
    # doc on magic methods https://docs.python.org/3/reference/datamodel.html#special-method-names

    def __init__(self, name, x=0, y=0, direction="N", battery=100, quiet=False): 
        if not quiet:
            print("Creating a new Robot")
        # we can store the data in the object
        self.name = name # we store the name in the object
        self.x = x
        self.y = y
        self.direction = direction
        self.battery = battery
        if not quiet:
            print("New Robot created")
            self.print_status() # we can call methods from inside other methods
        # we can call methods from inside other methods
        # we can call methods that we define later in the same class!
    

    # TODO add more methods to the Robot class
    # let's print current status of the robot
    def print_status(self): # note that we need to pass self as first argument
        # print_status is arbitrary name, we could call it anything
        # self refers to particular instance/object of the class
        print(f"Robot {self.name} is at {self.x},{self.y} facing {self.direction}")
        print(f"Robot {self.name} has battery level {self.battery}")
        # it could be useful to return some data from the method
        # if we do not have any data to return we can return None by default
        # or we could return self 
        return self # returns reference to the object itself

    # let's add some methods to move the robot
    def move_north(self, steps=1, battery_drain=1):
        self.y += steps
        self.direction = "N"
        self.battery -= battery_drain*steps
        # here again we could return self or None
        return self 

    def move_south(self, steps=1, battery_drain=1):
        self.y -= steps
        self.direction = "S"
        self.battery -= battery_drain*steps
        return self
    
    def move_east(self, steps=1, battery_drain=1):
        self.x += steps
        self.direction = "E"
        self.battery -= battery_drain*steps
        return self
    
    def move_west(self, steps=1, battery_drain=1):
        self.x -= steps
        self.direction = "W"
        self.battery -= battery_drain*steps
        return self
    
    # lets make a dance method
    def dance(self):
        print(f"Robot {self.name} is dancing")
        return self
    
    # there could be methods which need to return something that is not self
    # for example method that returns distance from another robot
    def distance_from(self, other_robot):
        # we could use Pythagorean theorem to calculate Euclidean distance
        # https://en.wikipedia.org/wiki/Pythagorean_theorem
        # d = sqrt((x2-x1)^2 + (y2-y1)^2)
        # we can access other_robot data directly
        distance = ((other_robot.x - self.x)**2 + (other_robot.y - self.y)**2)**0.5
        return distance # so here self is not appropriate to return
    
# first let's create a new robot using our Robot class

robocop = Robot("Robocop") # we create a new object of type Robot
terminator = Robot("Terminator", 10, 10, "S", 200) # we create another object of type Robot

# we could even create a swarm of robots placed randomly on the map of 100x100
# import random # standard library for random numbers
# swarm = [] # we would store them in a list but could store in a dictionary or set or even another class instance
# for i in range(100):
#     swarm.append(Robot(f"Robot_{i}", random.randint(0,100), random.randint(0,100), quiet=True))

# # print first 5 robots
# for robot in swarm[:5]: # robot is just an arbitrary name for each element in the swarm list
#     robot.print_status()

# now we can move our robot
robocop.move_north(5)
robocop.print_status()

# if we return self on above methods we could chain the calls
# after each method call we still have a reference to the same object
robocop.move_north(5).move_east(3).print_status().move_south(2).print_status().dance().print_status()
terminator.print_status()
# we can also call methods on other robots
distance = robocop.distance_from(terminator) # this will return a number
print(f"Distance between {robocop.name} and {terminator.name} is {distance:.2f}")
