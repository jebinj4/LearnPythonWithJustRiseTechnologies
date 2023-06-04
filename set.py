a=set()
a.add(55)
a.add(535)
a.add(5545)


help(a.add)
help(a.remove)
help(a.discard)


a.remove(55)
# if data is not thr it make some issue..for tht we can use discard.so even if the data is not thr it wont show any error
 
a.discard(55) 
len(a)

example2 = set([28, True, 2.71828, 'Helium'])
len(example2)

# to delete all the valus in the set
example2.clear()
len(example2)

# Union and intersection

odds=set([1,3,5,7,9])
even=set([2,4,6,8,10])
primes=set([2,3,5,7])
composites=set([4,6,8,9,10])

# Union
odds.union(even)
even.union(odds)

# Intersection
odds.intersection(even)

# to valide a data inside the set
# use in

2 in even
2 not in even
>> True