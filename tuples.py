#Tuples is a built-in datatype that lets us create immutable sequence of value
tup=(34,56,23,78,12,90,23)     #tup[0],tup[1]...
# tup[0]=43                   #NOT allowed in python
print(type(tup))
print(tup[0])
print(tup[1])
#tup=(1)              #<class "int">
#tup=(1,)             #<class "tuple">    comma after the number is imp for creating a single element tuple

#slicing in tuple
print(tup[2:4])         #prints number 23,78

#Tuple methods
print(tup.index(23))      #returns index of first occurence  tup.index(23) is 2
print(tup.count(23))       #Count total occurence 