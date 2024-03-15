#functions are used to invoke a task multiple time

#Syntax
def calc_sum(a,b):
    return a+b
print(calc_sum(4,5))

#avg of 3 numbers

def avg(a,b,c):
    avg = (a+b+c)/3
    return avg

a=int(input("enter 1st num"))
b=int(input("enter 2nd num"))
c=int(input("enter 3rd num"))

average=avg(a,b,c)
print("average of the numbers is",average)

#WAF to print length of a list
l=[1,2,3,4,5]
def length(list):
    return len(list)
 
print(length(l))

#WAF to print elements of a list in single line

def show(list):
    i=0
    for i in list:
        print(i,end=" ")

print(show(l))

#WAF to find factorial

def find_fact(n):
    fact=1
    for i in range(1,n+1):
       fact *=i
    return fact
        
print(find_fact(5))

'''RECuRSION'''

def show(n):
    if(n==0):#base case
        return
    print(n)
    show(n-1)
num=int(input("enter num to show sequence"))
show(num)

#Waf using recursion to print factorial of a number

def fact(n):
    if(n==0 or n==1):
        return 1
    factorial= n * fact(n-1)
    return factorial
n=int(input("enter a number to find its factorial"))
print(fact(n))

#waf using recurison to calculate sum of n natural numbers
def find_sum(n):
    sum=0
    if (n==0):
        return 0
    return find_sum(n-1)+n
print(find_sum(5))

#waf using recursion to print all elements of a list

def print_List(List,i=0):
   if(i==len(List)):
        return
   print(List[i])
   print_List(List,i+1)

List=["Gagan",2,0,"great"]
print_List(List)
