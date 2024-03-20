#Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

list=[]
i=0
size=int(input("enter size of list"))
while i < size :
    val = int(input("enter value"))
    list.append(val)
    i+=1
print(list)

def swap(list):
    i=int(input("enter position to swap"))
    j=int(input("enter position to swap"))
    temp=list[i]
    list[i]=list[j]
    list[j]=temp
    return list

print("list after swap",swap(list))
