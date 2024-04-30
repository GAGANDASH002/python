marks=[94.4,95.2,96,92]
name=["Sakshi"]
print(name)
print(marks)
#can be accesed using index and length using len() function
print(len(marks))#returns number of elements in a list
print(marks[2])
#strings are immutable whereas lists are mutable
#slicing rules are same as string
print(marks[:2])

"""list methods/functions"""
marks.append(4)#adds 4 at last of list 
marks.sort()#ascending order
marks.sort(reverse=True)#descending order
marks.reverse()#reverses the original list
marks.insert( 2, "Gagan")#adds element at specified index
print(marks) 
marks.remove("Gagan")#removes first occurence
print(marks)
marks.pop(2)#removes element at index
print(marks)

"""TUPLES"""

tup=(10,20,"GAGAN",10,40)
print(tup)
#slicing rules are same as lists and strings
"""TUPLE METHODS"""
print(tup.index(10))#returns 1st occurence index of element
print(tup.count(10))#counts total occurences

'''wap to enter names of 3 movies and 
store in a list'''

mov1=input("enter movie 1\n")
mov2=input("enter movie 2\n")
mov3=input("enter movie 3\n")
mov_list=[mov1,mov2,mov3]
print(mov_list)

'''wap to check if a list contains a palindrome
of elements'''

list1=[1,2,34,5,1]
list2=list1.copy()#returns a shallow copy of the list
list2.reverse()
if(list2==list1):
    print("PALINDROME")
else:
    print("NOT A PALINDROME")
