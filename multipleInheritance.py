class first:
    def displayFirst(self):
        print("first")
    def display(self):
        print("display f")   
class second :        
    def displaysecond(self):
        print("second")    
    def display(self):
        print("display s")    
    
class third(first,second):
      print("third")


x= third();

x.display()

# look operator overloading