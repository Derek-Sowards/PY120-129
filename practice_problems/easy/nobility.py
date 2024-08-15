class WalkMixin:
    def walk(self):
        return f"{self} {self.gait()} forward"

class Person(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"
    
    def __str__(self):
        return self.name

class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"
    
    def __str__(self):
        return self.name

class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
    
    def __str__(self):
        return self.name

class Noble(WalkMixin):
    def __init__(self, name, title):
        self.name= name
        self.title = title
    
    def gait(self):
        return "struts"
    
    def __str__(self):
        return f"{self.title} {self.name}"
    

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"