
num=0

try : 
     ans=5/num
     print("divided")
except ZeroDivisionError as error:
       print("not divisible")      
       print("err",error)