class Person:
    def  __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display_info(self):
        return f"Hi my name is {self.name} and my age is {self.age}"
        
