class sampleClass:
    def greet(self,name):
        self.name=name
        print("Hello",name)
        print("self",self)

greetEdith = sampleClass()
greetNilin = sampleClass()


greetEdith.greet("Edith")
greetNilin.greet("Nilin")
               