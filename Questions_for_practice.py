#WAP to ask the user to enter their 3 favourite movies name and store them in list
movies=[]
mov1=input("Enter 1st movie name:")
mov2=input("Enter 2nd movie name:")
mov3=input("Enter 3rd movie name:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#Another way of writing this code
movies=[]
movies.append(input("Enter the 1st movie name:"))
movies.append(input("Enter the 2nd movie name:"))
movies.append(input("Enter the 3rd movie name:"))
print(movies)

#WAP to check if a list contains palindrome of elements 
#LOGIC
"""To check whether the list is palindrome or not we first make a copy of list and then reverse the copied 
list and if the copy copy list and reverse list is same
then we can say that the list is palindrome"""

list=[3,2,3]
list2=[1,2,3]
copy_list=list2.copy()    #copied list is assign to copy_list
copy_list.reverse()      #copy of list is reversed using list.reverse()
if(copy_list==list2):     #check for condition for whether the list is palindrome or not
    print("Palindrome")
else:
    print("NOT Palindrome")    


#WAP to count the number of students with the "A" grade in the following tuple
tup=("C","D","A","A","B","B","A")
print("The number of students who get grade A are:",tup.count("A"))

#WAP to store the above values in a list and sort them from "A"to"D
alphabets=["C","D","A","A","B","B","A"]
alphabets.sort()
print(alphabets)
