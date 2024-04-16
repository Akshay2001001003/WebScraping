from pickle import TRUE
import random
print("hello")
# a,b=3,'3'
#this is the implementation of the if else
# if a>2:
#  print("new")
#  print("hello2")
#  print(type(a))

# if str(a)==b:
#  print(b)
# a=('hello','yellow','blue')
# x,y,z=a
# print(x,y+' '+z)
# global a
# a=3
# a="21"
# b=float(a)
# def func(a):
# #  global b
# #  b=4
#  print(complex(a))

# func(a)
# print(b)
# a=f"hello,     world     "
# for x in a:
#     print(x)

# if not 'z' in a:
#     print(a[-4:-1])
# else:
#     print("o is not present")
# print(a.strip())
# print(a)
# name=input("enter your name? ")
# age=input("enter your age ")
# b=-int(age)+2020
# print(b)
# weight=float(input("what is your weight? "))
# x=input("(k)kg or (l)lbs ")
# if str(x).upper()=='K':
#     b=weight/0.45
#     print("weigth is "+ str(b)+"lbs")
# else:
#     b=float(weight)*0.45359237
#     print("weight is "+str(b)+"kg")
# a=["  akshay","chetan","chitanya","mahesh"]
# a.append("happy")
# a.insert(1,"chirag")
# print(a[0].upper().strip())
# print(a)
# a.remove("chetan")
# print('a' in a[0])


#####main program for tuples######
a=('a','b','c','e','d')
b=('p','q','r')
a+=b
#tuples are unchangable ordered and immutable
print(a)

###main program for list###
p=['a','b','c']
q=('n','m','n')
p.extend(q)
print(p)
p.remove('a')
print(p)
p.pop()
p.sort(reverse=True)
[print(x) for x in p]
r=[]
r=['hello' for x in p]
print(r)