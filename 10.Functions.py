# Function is used to make code dynamic where we can use function to do the same task one or more time
# Functions are reusable one
# we use parameter to make the code dynamic

# dir() # to see the available functions

# def f():
#     pass

# f()

# dir() # once a function is created it will be automaticly added in the directory

# def ping():
#     return "OK ok data!"

# x=ping()
# print(x)

# a=[1,23,4,33,5,66]

# def check_age(b):
#     if b<18:
#         print('Sorry Small Boy')
#     else:
#         print('Welcome dude')
        
# for aa in a:
#     print('age',aa)
#     check_age(aa)
    


# a=int(input('To check you are eligible for this event kindly enter your age:'))
# b=18
# def check_age(a):
#     if a<b:
#         print('Sorry Small Boy')
#     else:
#         print('Welcome dude')
  
# check_age(a)
        
# for aa in a:
#     print('age',aa)
#     check_age(aa)
    
#Volume of spear v=(4/3)pi*r^3 
import math
def volume(r):
    "Return the volume of the spear with radious r"
    v=(4.0/3.0)*math.pi*r**3
    return v

a=input('Enter the radious of the spear')
a=volume(int(a))
print(a)
