#Extract Unique values dictionary values

test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}

x=(test_dict.values())
res=[]
for list in x:
    for item in list:
        if item not in res:
            res.append(item)
res.sort()
print(res)

#Remove keys with Values Greater than K ( Including mixed values )
# initializing dictionary

test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'} 
 

test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'} 
k=6

#The isinstance() function in Python is a built-in function used for type checking. It verifies if an object is of a specified type, returning True if it is, and False otherwise
res={key : val for key,val in test_dict.items()  if not (isinstance(val,int) and val>k) }
print(res)