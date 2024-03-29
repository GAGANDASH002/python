# Find all duplicate characters in string

def duplicate(s):
    res=[]
    repeat=[]
    for char in s:
        if char not in res:
            res.append(char)
        elif char in repeat:
            continue
        else :
            repeat.append(char)
    return repeat

print("duplicate charachters in the string are",str(duplicate("geeksforgeeks")))
        
# kth non repeating charachter

def findKth(s,k):
    res=[]
    repeat=[]
    for char in s:
        if char not in res:
            res.append(char)
        elif char in repeat:
            continue
        else :
            repeat.append(char)

    non_repeat=[char for char in s if char not in repeat]
    if k<=len(non_repeat):
        return non_repeat[k-1]
    else:
        print("no such string")

print(findKth("geeksforgeeks",0))
        