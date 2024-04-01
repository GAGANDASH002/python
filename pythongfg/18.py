#Maximum record value key in dictionary

test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
             'is' : {'Manjeet' : 8, 'Himani' : 9},
             'best' : {'Manjeet' : 10, 'Himani' : 15}}

key='Manjeet'

res_max=0
res=None

for sub in test_dict:
    if test_dict[sub][key]>res_max:
        res_max=test_dict[sub][key]
        res=sub
print(res)

# Keys associated with Values in Dictionary

test_dict = {'abc' : [10, 30], 'bcd' : [30, 40, 10]}

res={}

for key , val in test_dict.items():
    for ele in val:
        if ele in res:
            res[ele].append(key)
        else:
            res[ele]=[key]

print(res)