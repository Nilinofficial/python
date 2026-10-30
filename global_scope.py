name ="abc"
def outer() : 
    

    def inner():
        name ="Nilin"

        def deep() :
               global name
               name="deep" 
        deep()       
        print(name)
  
    inner()    
    print(name)

outer()    



# global = It takes global variable and reassigns it.