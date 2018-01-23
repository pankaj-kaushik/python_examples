class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

class Cat(Animal):
    
    def speak(self):
        print "meow"
        
    def __str__(self):
        return "cat: " + str(self.name) + ":" + str(self.age)