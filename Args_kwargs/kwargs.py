## 1
def student(**kwargs):
    print(kwargs)

student(name="Raj", age=22, city="Indore")
print("-----------------------")
##2
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Raj", age=22, city="Indore")

print("-----------------------")

##3 Both args and kwargs with real life example.
def create_user(name, *skills, **details):
    print("Name:", name)
    print("Skills:", skills)
    print("Details:", details)

create_user(
    "Raj",
    "Python",
    "Django",
    "SQL",
    age=22,
    city="Indore",
    experience="Fresher"
)
