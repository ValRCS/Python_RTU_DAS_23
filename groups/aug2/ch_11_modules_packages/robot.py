# pep recommends modules to be lowercase
# pep 008 - style guide for python code
# docs: https://www.python.org/dev/peps/pep-0008/

# so could put Robot class here

class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"Hello, I am {self.name}")

    def say_bye(self):
        print(f"Bye, I am {self.name}")

# i could store more classes here say Cyborg, Android, etc.

# let's make a Cyborg class that inherits from Robot

class Cyborg(Robot):
    def __init__(self, name, model):
        # super calls the parent class constructor
        super().__init__(name)
        # instead of super we could have done this
        # Robot.__init__(self, name)
        # here even I could have skipped this and done this
        # self.name = name
        self.model = model

    # we can override methods
    def say_hi(self):
        print(f"Hello, I am {self.name} and my model is {self.model}")

    # or define new methods
    def say_model(self):
        print(f"My model is {self.model}")

# i could run this file directly by using __name__ == "__main__"

if __name__ == "__main__": # only if this file is run directly
    # lets make some robots and cyborgs
    r1 = Robot("Wall-E")
    r1.say_hi()
    r1.say_bye()
    # anoher robot instance - new object
    r2 = Robot("Eva")
    r2.say_hi()
# else: # very rarely done - means this file is imported
#     print("I am being imported")
    