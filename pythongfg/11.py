#sorting a dictionary

dict= {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

mykeys=list(dict.keys())
mykeys.sort()
print(mykeys)
new_dict={i:dict[i] for i in mykeys}
print(new_dict)

#Ways to sort list of dictionaries by values in Python – Using itemgetter

from operator import itemgetter
list=[{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

print(sorted(list,key=itemgetter('age')))

#merging two dictionaries

def merge(dict1,dict2):
        return (dict1.update(dict2))


 
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(merge(dict1,dict2))

print(dict1)