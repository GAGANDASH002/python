print("hello world")
name="Gagan"#python is implicit type language,datatype doesnt need to be defined
age=20


print("my name is",name,"my age is",age)
print(type(name))#type function returns datatype
print(type(age))

a=5
b=5
sum=a+b
print(sum)
#arithmetic op with int and float results in float
a=10
b=5.0
print(a*b)
#int divison with float and int will givr int displayed as float
a,b=20.5,3
print(a//b)#result is same as floor(a/b)

#expression execution
a,b=2,3  
txt="@"
print(2*txt*3)
#concatenation
a="2"
b=3
print((a+txt)*b)
