#Sum the elements of a Tuple in Python

tup=(1,2,3,4,5,4,6,)
sum=0
for i in tup:
    sum+=i
print(sum)

#Repeating tuples N times

tuple=(1,2)
n=int(input("enter number of times you want tuple to be repeated\n"))

new_tup=((tuple,)*n)
print(new_tup)

#| Join tuple elements in a list

list=[("Ronaldo","and","Virat"),("are","the","goats")]
new_list=[''.join(i) for i in list]
print(new_list)