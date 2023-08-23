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
    """This is a Robot class which can move around and do other things
    Attributes:
        name (str): name of the robot
        x (int): x coordinate of the robot
        y (int): y coordinate of the robot
        direction (str): direction of the robot
        battery (int): battery level of the robot
    Methods:
        print_status: prints current status of the robot
        move_north: moves the robot north
        move_south: moves the robot south
        move_east: moves the robot east
        move_west: moves the robot west
        dance: makes the robot dance
    """	

    # Robot will have a name, x and y coordinates, direction, battery level
    # we want to pass this data when we create the object
    # we can do that by using __init__ method
    # __init__ method is called when we create an object
    # __init__ method is called a constructor - technically it is not a constructor, it is called right after the object is created
    # __init__ method is called an initializer - more correct term

    # we can pass in data to __init__ method
    # methods with __ in front and back are called magic methods - dunder methods
    # doc on magic methods https://docs.python.org/3/reference/datamodel.html#special-method-names

    def __init__(self, name, x=0, y=0, direction="N", battery=100, quiet=False, secret="I am a robot"): 
        if not quiet:
            print("Creating a new Robot")
        # we can store the data in the object
        self.name = name # we store the name in the object
        self.x = x
        self.y = y
        self.direction = direction
        self.battery = battery
        # idea is to hide some data from the user
        self.__secret = secret # we can store the secret in the object
        # one use for secrets would be for information that is internal only to the class or object
        # it is not needed for the user of the class
        # now outsiders will not have easy access to the secret
        if not quiet:
            print("New Robot created")
            self.print_status() # we can call methods from inside other methods
        # we can call methods from inside other methods
        # we can call methods that we define later in the same class!

    # we could define our own __str__ method to print something more useful than memory address
    def __str__(self):
        # only requirement for __str__ method is that it returns a string
        # do not print anything in __str__ method!!
        return f"Robot {self.name} is at {self.x},{self.y} facing {self.direction}, battery: {self.battery}"
    
    # we could define our own + method to add two robots together
    def __add__(self, other_robot):
        # we could create a new robot and return it
        # we could also modify one of the robots and return it
        # we could even return something else
        # here we will create a new robot
        # of course what we do here is up to us
        x = (self.x + other_robot.x)//2
        y = (self.y + other_robot.y)//2
        battery = self.battery + other_robot.battery
        new_name = f"{self.name[:4]}_{other_robot.name[:4]}"
        new_robot = Robot(new_name,x, y, battery=battery, quiet=True)
        return new_robot
    
    

    # TODO add more methods to the Robot class
    def get_secret(self, debug=False):
        # we can access the secret from inside the class
        # we could add some validation here
        # also authorization checks
        if debug:
            print(f"Secret is {self.__secret}")
        # even better return
        return self.__secret
    
    # similarly I could control setting of the secret
    def set_secret(self, new_secret):
        # we could add some validation here
        # let's check if new_secret is a string of at least 8 characters
        if type(new_secret) != str:
            print("Secret must be a string")
            return # we could return None or False
        if len(new_secret) < 8:
            print("Secret must be at least 8 characters long")
            return # we could return None or False
        # also authorization checks
        self.__secret = new_secret
# not required but could be useful


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
    
    # let's make a generic move method 
    # it will use _move syntax to indicate that it is a private method
    # it is not really private but it is a convention to not call this method directly
    # we could call it directly but it is not recommended
    def _move(self, x=0, y=0, steps=1, battery_drain=1):
        self.x += x*steps
        self.y += y*steps
        self.battery -= battery_drain*steps
        return self

    # let's add some methods to move the robot
    def move_north(self, steps=1, battery_drain=1):
        # i could rewrite all the move methods to use _move method
        self._move(y=1, steps=steps, battery_drain=battery_drain)
        self.direction = "N"
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
    def distance_from(self, other_robot) -> float:
        """Calculates distance from another robot
        Args:
            other_robot (Robot): another robot object
        Returns:
            float: distance between the two robots
        """
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

# more on dunder methods
# let's print our two robots
print(robocop) # this will print the memory address of the object without __str__ method
print(terminator) 

robo_term = robocop + terminator # we can add two robots together
print(robo_term)

# let's try to access the secret
# print(robocop.__secret) # this will not work
try:
    print(robocop.__secret) # this will not work
except AttributeError as e:
    print(f"AttributeError: {e}")

# instead we should provide a method to access the secret
# now we can just use the get_secret method
print(f"Secret is {robocop.get_secret()}")

# we can also change set a bad secret
robocop.set_secret("Valdis")
print(f"Secret is {robocop.get_secret()}")
# now let's set a longer one
robocop.set_secret("Robocop rules")
print(f"Secret is {robocop.get_secret()}")

# side note we can get hidden variables with _ClassName__variable
print(f"Secret is {robocop._Robot__secret}") # so called name mangling
# usually you have no need to do this

print(robocop)
# i could call _move directly
# again single _ indicates that this method is not meant to be called directly
robocop._move(x=1, y=1, steps=5, battery_drain=2)
print(robocop)

# so inhertiace is when we create a new class from an existing class

# let's make a new class which will inherit from Robot class
class FlyingRobot(Robot): # note I added Robot as an argument to the class
    # if we do not add __init__ method to our new class it will use the one from the parent class
    # we can add new __init__ method to our new class
    # for one we might want to have a z coordinate
    # also we might want to have a new battery_drain for flying

    def __init__(self, name, x=0, y=0, z=0, direction="N", battery=100, battery_drain=2, quiet=False):
        # we can call the __init__ method from the parent class
        # we can do that by using super() method
        # super() method returns a reference to the parent class
        # then we can call methods on the parent class
        super().__init__(name, x, y, direction, battery, quiet=quiet)
        # without above call I'd have to rewrite all the init code from the parent class
        # we can add new data to our new class
        self.z = z

    # for now we will just add fly method
    def fly(self):
        print(f"Robot {self.name} is flying")
        # TODO add some code to actually fly
        return self # again for chaining
    
    def raise_in_the_air(self, steps=1, battery_drain=1):
        self.z += steps
        self.battery -= battery_drain*steps
        return self
    
# now let's create our flying robot
drone = FlyingRobot("Drone", 10, 10, 30, "S", 200) # we create another object of type FlyingRobot

# now we can use any of Robot methods on our drone
# also we can use the new fly method
drone.fly().print_status()
drone.raise_in_the_air(10).print_status()

# now we would also have to overwrite print_status method to include z coordinate
# so in practice inheritance is not always the best solution

# alternative would be something like composition

# composition means we build our object from other objects

# so let's make a Robot_Warehouse class

class RobotWarehouse:
    # we will need to store our robots somewhere
    # we could use a list
    # also we will have methods to get stats on our robots

    def __init__(self, warehouse_name, robot_list=()): # note that we use () to indicate empty tuple
        # do not use [] as default argument since it will be shared by all instances of the class
        self.name = warehouse_name
        self.robot_list = list(robot_list)

    def __str__(self):
        return f"RobotWarehouse {self.name} has {self.get_robot_count()} robots"
        
    # get number of robots
    def get_robot_count(self):
        # there could be some extra logic here as well
        # also we could use it we decide to hide the robot_list with __robot_list
        return len(self.robot_list)
    
    # get total battery level of all robots
    def get_total_battery(self):
        total_battery = 0
        for robot in self.robot_list:
            total_battery += robot.battery
        return total_battery
    
    # add new robot
    def add_robot(self, robot):
        # idea is here to check if new robot is suitable for our warehouse
        # you could add extra logic say check for battery, weight, name , location, etc.
        self.robot_list.append(robot)
        return self
    
    # remove robot
    def remove_robot(self, robot):
        # we could check if robot is in our warehouse
        self.robot_list.remove(robot)
        return self
    
# lets create our warehouse
getlini = RobotWarehouse("Getliņi")  # i could have given a list of some robots here
print(getlini)
# let's add some robots
getlini.add_robot(robocop).add_robot(terminator).add_robot(drone)
# i could even add drone since it inherits from Robot
# print our warehouse
print(getlini)
# print battery level in our warehouse
print(f"Total battery level in {getlini.name} is {getlini.get_total_battery()}")

# now we could access our robots directly
# so first robot name
print(getlini.robot_list[0].name)
# check if first robot object is same as our robocop object
print("Robocop Objects are same?", getlini.robot_list[0] is robocop)

