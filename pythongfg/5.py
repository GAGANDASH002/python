#Repeat Alternate Elements in list

list=[1,2,3,4,5]
def alternate(list): 
    newlist=[]  
    i=0 
    while i < len(list):
        for item in list:
            if(i%2==0):
                newlist.append(item)
                newlist.append(item)
                i+=1
        
            else:
                newlist.append(item)
                i+=1
    return newlist
list2=alternate(list)
print("original list is",list)
print("alternated list is",list2)
            

