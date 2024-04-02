#Convert numeric words to numbers

dict={
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    'zero':'0'
}

str="zero one five seven"
res=' '.join(dict[ele] for ele in str.split())
print(res)

#find position of word in string

str="Hey its Maverick reporting on duty"

word="Maverick"

new=str.split()
pos=new.index(word)+1

print("position of word in string is",pos)