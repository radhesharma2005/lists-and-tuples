#list is a built-in datatype that stores set of values
#It can store different data types like(float,int,strings)
# marks=[5,4,7,3,2,8,1,6]
# marks[5]=23.1
# print(marks)
# print(len(marks))
# print(type(marks))
# print(marks[5])

#List slicing
"""Syntax
list_name[starting_ind:end_index]  #ending index is not included"""  #like string slicing

# print(marks[:6])


#list methods
"""list.append(4)           #add one element at the end
list.sort()                 #sort in ascending
list.sort(reverse=True)     #sort in descending
list.reverse()              #reverse the list
list.insert(indx,element)   #insert element at index
list.remove(1)              #removes 1st occurence of element
list.pop(idx)               #removes element at index"""
#Examples
marks=[5,4,7,3,2,8,1,3,6]
marks.append(10)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(8,23)
print(marks)
marks.remove(3)
print(marks)
marks.pop(2)
print(marks)
