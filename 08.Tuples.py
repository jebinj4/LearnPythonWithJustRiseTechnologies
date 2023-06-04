# #Tuple
# cars=('a','b','c')

# -------------------------------------
# list and tuple
# -List contain sequence of data surrended by square brackets 
# -tuple contain sequence of data surrended by Parantisis
# -List occoupy more memory than tuples
# import sys
# # `print(dir(sys))` will print out a list of all the attributes and methods available in the `sys`
# # module.
# # print(dir(sys))
# # print(help(sys.getsizeof))
# Cars_List=['a','b','c']
# Cars_Tuples=('a','b','c')
# print('List Memory Size:',sys.getsizeof(Cars_List))
# print('Tuples Memory Size:',sys.getsizeof(Cars_Tuples))

# - Datas can be add, removed and changed in list but in tuple those cannt be changed. Tuple is also known as immutable 
# - Tuple is more efficient than list

# import timeit

# list_test=timeit.timeit(stmt="['a','b','c']",number=100000000)
# tuple_test=timeit.timeit(stmt="('a','b','c')",number=100000000)

# print('List Test Duration:' , list_test,' sec')
# print('Tuple Test duration:', tuple_test,' sec')

#-tuple with one element will consider as string 

# test1=() #Empty tuple
# test2=('a')
# test3=('a','b')
# test4=('a','b','c')

# test5='a','b','c'

# print(test1)
# print(type(test1))
# print(test2)
# print(type(test2))
# print(test3)
# print(type(test3))
# print(test4)
# print(type(test4))
# print(test5)
# print(type(test5))

##-Tuple Assignment

# #(age,country,Known_Coding)
# #Tuple
# survey=(27,'India',True)

# age=survey[0]
# country=survey[1]
# Known_Coding=survey[2]

# print('Age:',age)
# print('Country:',country)
# print('Known_Coding:',Known_Coding)

# survey2=(25,'India',True)
# age,country,Known_Coding=survey2


# print('Age:',age)
# print('Country:',country)
# print('Known_Coding:',Known_Coding)

# -Must have equal number of variable and data or it will through error
## -age,country,Known_Coding=(27,'India',True)

