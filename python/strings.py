#escape sequence charachters
str="hello\nWorld"
print(str)
#\t is used for space

"""len(str) returns length of a string
'+' is used for concatenation"""
print(len(str))
print(str[0])#indexing

#slicing-accessing parts of a string
ch=str[1:4]#note that ending index is not included
print(ch)
print(str[:4],str[4:])
'''NEGATIVE INDEX SLICING'''
print(str[-3:-1])
print(str.endswith("d"))
print(str.capitalize())
print(str.replace("hello","welcome"))
print(str.find("l")) #returns index of 1st occurence
print(str.count("l"))#returns number of occurences of the string

"""find length of ur name
find number of ocurrences of s """
ch=input("name:")
print(len(ch))
print(ch.count("s")) 

