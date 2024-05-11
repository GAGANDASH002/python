"""there are two loops in python 
i.e for and while"""

#while loops

count=0#iterator
while count<5:#iteration
    print("hello")
    count+=1

#print elements of the list using while loop
l=[1,2,3,4,100,45]
i=0
while(i<len(l)):
    print(l[i])
    i+=1

n=int(input("enter num"))
i=0
while(i<len(l)):
    if(l[i]==n):
        print("found at",i)
        break #similarly we can also use continue
    else:
        i+=1

#for loops
            
list=[10,20,30,40]
for i in list:
    print(i)
            
str= "top gun"
for i in str:
    print(i)
            
#search for num x in the tuple using loop
tup=(10,20,30,40,50,60)
num =int(input("enter number to search"))
for i in tup:
    if(i==num):
        print(i)
        break
else:
    print("FOUND FOUND FOUND")#used to print something outside loop

#range function - returns sequence of num(starts from default 0)
for el in range(5):
    print(el)

#range(start?,stop,step?)
for el in range(1,10,2):
    print(el)

#pass- used to leave the loop empty
for i in l:
    pass
print("some useful work")