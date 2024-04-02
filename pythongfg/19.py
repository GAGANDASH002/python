#check string symmetry and palindrome

str="goodgood"

mid=int(len(str)/2)

first_str=str[:mid]
second_str=str[mid:]

if(first_str==second_str):
    print("string is symmetrical")
else:
    print("string is unsymmetrical")

if(first_str==second_str[::-1]):
    print("yes its a palindrome")
else:
    print("nope its not a palindrome")

#reverse words in a given string
    
str="Hey its Maverick reporting on duty"
s=str.split()[::-1]#reversing the string and splitting it
l=[]

for i in s:
    l.append(i)

print(" ".join(l))