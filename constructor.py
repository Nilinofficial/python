class sampleClass:
    message = "welcome onboard"
    # class variable is common for everyone in python
    def __init__(self,name):
        self.name=name
    
    def greet(self):
        print("Hello",self.name)
        print("self",self)
        print(sampleClass.message)
    @classmethod
    def changeMessage(cls):
        cls.message = "Message Changed"    
# used to change class variable

# use static method when fn doesnt do operations
  

greetEdith = sampleClass("Edith")
greetNilin = sampleClass("Nilin")

greetEdith = greetNilin
# greetEdith points to greetNilin object now


sampleClass.changeMessage()


greetEdith.greet()
greetNilin.greet()

