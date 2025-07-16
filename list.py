#list is a built-in datatype that stores set of values
#It can store different data types like(float,int,strings)
marks=[23.54,22,23.5,23.6,23.7,23.8,23.9,24.0]
marks[5]=23.1
print(marks)
print(len(marks))
print(type(marks))
print(marks[5])

#List slicing
"""Syntax
list_name[starting_ind:end_index]  #ending index is not included"""  #like string slicing

print(marks[:6])


#list methods
"""list.append(4)           #add one element at the end
list.sort()                 #sort in ascending
list.sort(reverse=True)     #sort in descending
list.reverse()              #reverse the list
list.insert(indx,element)   #insert element at index"""
#Examples
marks.append(6)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(10,21)
print(marks)
