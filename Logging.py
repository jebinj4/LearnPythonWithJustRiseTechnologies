#record the log values in python


# Levels
# Debug, info, Warning, error , Criticals

import logging
import math

# dir(logging)
# # UpperCase datas in this directory are constants
# # CamelCase are Classes
# # lower case are methods


#Create a logging file in a directory

log_for="%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename='pylog.log',
                    level=logging.DEBUG,
                    format=log_for,
                    filemode='w')

# file mode w with overwrite all the datts in the file 
log=logging.getLogger()

# test
log.info("File Created and Running succesfuly. Kindly contact admin for more details")

print(log.level)
# output: 30

# logging will print only if the numerical value is less than or equal to the set level
# Level       Numeric Value
# NOTSET      0
# DEBUG       10
# INFO        20
# WARNING     30 -basicConfig are also know as Root its value is  30
# ERROR       40
# CRITICAL    50

# log autribiutes  need to refer in python website

# Testing
# log.debug('This is a harmless debug message.')
# log.info('Just some useful info')
# log.warning("""I‘m sorry, but I can't do that, Dave.""")
# log.error("Did you just try to divide by zero?")
# log.critical("The entire internet is down!!")


# Quadratic Formula

# The solution to ax^2+bx+c=0 are
# x=((-b+-**(b^2-4ac))/2a)

def Qyad_for(a,b,c):
    'Return the solutionj to the equation ax^2+bx+x=0'
    log.debug('Qyad_for({0},{1},{2})'.format(a,b,c))
    
    # Compute the discrimination
    log.debug('# Compute the discrimination')
    disc=b**2-4*a*c
    
    log.debug('# Compute the roots')
    root1=(-b+math.sqrt(disc))/(2*a)
    root2=(-b-math.sqrt(disc))/(2*a)

    log.debug('# Return the root value')
    return(root1,root2)

roots=Qyad_for(1,0,-4)
print(roots)