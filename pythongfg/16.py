#possible Words using given characters in Python

def possiblewords(dict,arr):
    arr_set=set(arr)
    res=[]
    for char in dict:
        if set(char).issubset(arr_set):
            res.append(char)
    return res

dict= ["go", "bat", "me", "eat", "goal", "boy", "run"]
arr = ['e', 'o', 'b', 'a', 'm', 'g', 'l','y']

print(possiblewords(dict,arr))

#Create Nested Dictionary using given List

dict={'Hi':1,'this':2,'is':3,'python':4}
list=[10,20,30,40]

print("original dictionary is",dict)
print("original list is",list)

res={index:{key:dict[key]} for index ,key in zip(list,dict)}#zip() is used to combine multiple iterables(lists,tuples,etc)element-wise

print("nested dictionary is",res)
