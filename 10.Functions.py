# Function is used to make code dynamic where we can use function to do the same task one or more time
# we use parameter to make the code dynamic



# a=[1,23,4,33,5,66]

# def check_age(b):
#     if b<18:
#         print('Sorry Small Boy')
#     else:
#         print('Welcome dude')
        
# for aa in a:
#     print('age',aa)
#     check_age(aa)
    


a=int(input('To check you are eligible for this event kindly enter your age:'))
b=18
def check_age(a):
    if a<b:
        print('Sorry Small Boy')
    else:
        print('Welcome dude')
  
check_age(a)
        
# for aa in a:
#     print('age',aa)
#     check_age(aa)
    

