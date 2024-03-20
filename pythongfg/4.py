#Concatenate two lists element-wise

list1=["Gagan","is","for"]
list2=["Dash","preparing","armed forces"]

def concat(l1,l2):
    newlist=[]
    
    j=0
    while j < len(l1) :
        newlist.append(l1[j]+l2[j])
        j+=1
    return newlist

list3=concat(list1,list2)
print(list3)