# we can create a class that is composed of other classes

# let's make Mr.PotatoHead
# he has a body, eyes, nose, mouth, and ears

class Body:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Body: {self.color}"
    
class Eyes:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Eyes: {self.color}"
    
class Nose:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Nose: {self.color}"
    
class Mouth:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Mouth: {self.color}"
    
class Ears:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Ears: {self.color}"
    
    def wiggle(self):
        print("I am wiggling")
    
class MrPotatoHead:
    def __init__(self, body, eyes, nose, mouth, ears):
        self.body = body
        self.eyes = eyes
        self.nose = nose
        self.mouth = mouth
        self.ears = ears

    def __str__(self):
        return f"{self.body}\n{self.eyes}\n{self.nose}\n{self.mouth}\n{self.ears}"
    
body = Body("brown")
eyes = Eyes("blue")
nose = Nose("orange")
mouth = Mouth("red")
ears = Ears("pink")

mr_potato_head = MrPotatoHead(body, eyes, nose, mouth, ears)

print(mr_potato_head)
# i can wiggle his ears
mr_potato_head.ears.wiggle()

# with this example we might have a problem if ears have to communicate with the body