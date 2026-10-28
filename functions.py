def greet():
    print("Hello World")

greet()    


def info(name,age): 
    print("Name is " ,name, " and age is ", age)

# keyword arguments
info(age= 20,name = "Nilin")


# default argument
def getAge(age=10):
    print(age)

getAge()   


# multiple postion arguments

def languages(*values):
    print(values)


languages("malayalam","english","tamil")

# similar to rest operators. * converts all the args passed into tuples


# Force keyword argument

def details(name,*,age):
    print(name,age)

details("Nilin",age =20)    


# details("Nilin",20) wrong    
# Every parameter after * must be passed using its name.


# Multiple keyword arguments

# Here, Python collects the keyword arguments into a dictionary, similar to a JavaScript object.
# **kwargs
def information(**info):
    print(info)


information(name="Nilin", age=20, city="Palakkad")