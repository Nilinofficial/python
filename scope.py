
def outer() : 
    name ="abc"

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



# nonlocal = It searches outward for the
# nearest enclosing function scope where that variable is defined.