#Join Tuples if similar initial element
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
res=[]
for tup in test_list:
    key=tup[0]
    if key in res:
        res[key]+= tup[1:]
    else:
        res[key]=list(tup)

print(res.values)
