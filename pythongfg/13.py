# Insertion at the beginning in OrderedDict

from collections import OrderedDict

dict=OrderedDict([('akshat', '1'), ('nikhil', '2')])
dict.update({"manjeet":"3"})
dict.move_to_end("manjeet",last=False)#Move an existing element to the end (or beginning if last is false).

print(dict)

#Check order of character in string using OrderedDict( )


def checkorder(string,pattern):
    i,j=0,0 #initializing two pointers
    for char in string:
        if char == pattern[j]:
            j+=1
        if j == len(pattern):
            return True
    return False

string="Fighters rock"
pattern="er"
print(checkorder(string,pattern))

