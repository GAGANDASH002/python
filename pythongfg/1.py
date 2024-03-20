#Given a list, write a Python program to swap first and last element of the list.
list=[]
i=0
size=int(input("enter size of list"))
while i < size :
    val = int(input("enter value"))
    list.append(val)
    i+=1
print(list)

def swap(list):
    size=len(list)
    temp=list[0]
    list[0]=list[size-1]
    list[size-1]=temp
    return list

print("list after swap",swap(list))
