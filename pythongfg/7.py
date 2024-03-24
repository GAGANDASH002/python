#Create a tuple from string and list – Python

list = ["Ronalo","Virat"]
s="best"
tup=tuple(list+[s])
print(tup)

#Access front and rear element of Python tuple

tuple=(1,2,3,4,5)
print(tuple[0])
print(tuple[-1])

#Unpacking a Tuple in Python
tuple=(1,"sukhoi","maverick",4,5)
(num1,plane,pilot,num2,num3)=tuple
print(num1)
print(plane)
print(pilot)
print(num2)
print(num3)

