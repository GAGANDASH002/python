#Join Tuples if similar initial element
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
res={}
for tup in test_list:
    key=tup[0]
    if key in res:
        res[key]+= tup[1:]
    else:
        res[key]=list(tup)

print(list(res.values()))

#Removing duplicates from tuple

tup=(1,2,3,1,4,2,5,7)
x=[]

for i in tup:
    if i not in x:
        x.append(i)

new=tuple(x)

print(new)

#How to get unique elements in nested tuple

test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]

res=[]

for tup in test_list:
    for ele in tup:
        if ele not in res:
            res.append(ele)

res=tuple(res)
print(res)