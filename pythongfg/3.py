#Check if an element exists in a list in Python

l=[1,2,3,4,5]
def find(list):
    i=0
    val=int(input("enter element to find"))
    while i < len(list):
        if(list[i]==val):
            print("found the element at index ",i)
            break
        else:
            i+=1
print(find(l))