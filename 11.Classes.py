#properties and Behaviours (Behaviour is a function)
#colour and size / can call, can take pic

#class is men
#object is Jebin
#class contain set of objects


# class should always starts with a CapitaL Letter
# Need more video to understand class and objects

# I think class is a customized data type

class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
    def walk(self):
        print(self.name+' is walking')
        
    def speak(self):
        print('Hello my name is '+ self.name +' and my age is '+ str(self.age))
        
name1=person('Jose',55) #OBJ 1
name2=person('Jebin',20) #OBJ 2
name3=person('Priya',60) #OBJ 3

print(name1.name+str(name1.age))
name1.walk()
name1.speak()