#Python can be used to perform operations on a file.(read & write data)
'''open,read and close file'''

#syntax f=open("file_name","mode")

f=open("demo.txt","r")# r i used to read the file
data = f.read()
print(data)
print(type(data))

line1=f.readline()#reads 1 line at a time
print(line1)#prints empty next line as we have already read the file

f.close()

'''Writing'''

f=open("demo.txt","w")# w is used for writing
f.write("I am learning python")#overwrites the data
f.close()

f=open("demo.txt","a")# a appends data to end of the file
f.write("\nand also learning C and Java")
f.close()

f=open("Sample.txt","a")#creates non existing file
f.close()

f=open("demo.txt","r+")#pointer at beginning of file
f.write("yo")#overwrites at beginning of file

# w+ opens the file in truncated mode
#similarly a+ mode points at the end of file

'''with keyword'''
with open("demo.txt","r") as f:
    data =f.read()
    print(data)#automatically closes file

'''deletion'''

'''using os module:
module is a file by another coder that has in-built 
functions to use'''

import os
os.remove("sample.txt")

"""practice questions"""

#create a new file "practice.txt" and add data

with open("practice.txt","w") as file:
    file.write("hi everyone \nwe are learning python I/O\n"
           "using python\n i like programming in python")
file.close()

#replace all occurences of "python" with "java"
with open ("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("python","java")#replaces the occurences
print(new_data)

with open ("practice.txt","w") as f:
    f.write(new_data)
f.close()

#search if the word "learning" exists in the file or not
word="learning"
with open ("practice.txt","r") as f:
    data=f.read() 
    if(data.find(word) != -1):#find() returns valid index of any item
        print("found")
    else:
        print("not found")
    f.close()

# return the line in which the word learning exists

def check_line():
    word="learning"
    data=True
    line_no=1
    with open ("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
            line_no+=1
    return -1
check_line()

#from a file containing numbers separated by comma , print the count of even numbers

count=0
with open ("num.txt","r") as f:
    data=f.read()
    nums=data.split(",")# return a list of substrings based on separator ","
    print(nums)
    for val in nums:
        if(int(val)%2==0):
            count+=1
        
print(count)
