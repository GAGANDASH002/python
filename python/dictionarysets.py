"""DICTIONARY
used for storing key value pairs
"""

info={
    "name":"Gagan",
    "marks":[90,20,30],
    "cgpa":8.6,
    "is male":True,
    1:"abcd"
}
print(info)

"""keys can be int,float,or string but not list or tuple,
whereas values can be anything"""
#unordered,mutable,no duplicate keys

print(info["name"])#accessing keys of a dict.
info["name"]="maverick"#reassigned values
info["callsign"]="dierra"#added new key value pair
print(info)

null_dict={}
print(null_dict)

#nested dictionaries
Fighters={"pilot":"pete",
          "aircraft":{
              "mig 21":"decomissioned",
              "Sukhoi":"flanker",
              "mig 29":"Fulcrum",
          },
         }

#methods

print(Fighters["aircraft"]["Sukhoi"])
print(Fighters.keys())#returns all keys in list form except nested keys
print(len(Fighters))#returns no of key value pairs
print(Fighters.values())#returns all values in list form  
print(Fighters.items())#returns all key value pairs in tuples
print(Fighters.get("pilot"))#returns value of the key
Fighters.update({"branch":"flying"})#adds and updates new key value to dict
print(Fighters)

"""Sets are collection of unordered items,unique items
and mutable elements"""

#we can store all values in a set except list and dict as they are mutable

set1={1,2,(2,3),"Gagan"}
print(set1)
print(type(set1))
print(len(set1))

set2={5,6,7,(1,2)}
collection=set()#empty set syntax
print(type(collection))

'''METHODS'''

set1.add(1)
set1.remove("Gagan")
print(set1.pop())#pops random element
set1.clear()#clears whole set
print(set1)
set1={1,2,("mav","whiteman"),"Gagan"}
print(set1.union(set2))
print(set1.intersection(set2))

"""wap to store the word meanings in a dict"""

dict1={ "table":["a piece of furniture",
    "list of facts and figures"],
    "cat": "a small animal"
    }
print(dict1)

"""wap to enter marks of 3 subjects and store in a dict
start with an empty dict and add one by one"""

report={}
x=int(input("enter marks"))
report.update({"science":x})

x=int(input("enter marks"))
report.update({"maths":x})

x=int(input("enter marks"))
report.update({"sst":x})

print(report)
