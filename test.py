
# i=5
# j=1
# while i>=1:
#     print("hello");
#     while j<=4:
#         print("Four")
#         j=j+1
#     i=i-1
# x=["mukesh",25]
# for i in x :
#     print(i)
# for j in range(11,21,1):
#     print(j)
#x = int(input("Please entry numeric value "))
# i =1
# while i<x:
#     print("*", end ="")
#     i=i+1
# for i in range(x):
#     for j in range(i+1):
#         print("*", end="")
#     print()
# for i in range(x):
#     for j in range(x-i):
#         print("*", end="")
#     print()
# nums=[11,16,17,29,31,41]
# for i in nums:
#     if i % 3==0:
#         print(i)
#         break
# else:
#         print("bye")
#prime number not correct working
# num=20
# for i in range(2,num-1):
#     if num%i==0:
#         print("Not Prime")
# else :
#   print("Prime")

# from array import *
# arr= array('i',[])
# n =int(input("Enter the length of array"))
#
# for i in range(n):
#     x=int(input("enter the value"))
#     arr.append(x)
#
# print(arr)
#
# val =int(input("Enter the value for search"))
# k=0
# for x in arr:
#     if x==val:
#         print(k)
#     k+=1


# from numpy import *
# import numpy
# arr =array({1,2,3,4,5})
#
# arr=arr+5
# print(arr)

# def greet():
#     print("Hello")
#     print("Good Morning")
#
# def add(x,y):
#     c=x+y
#     d=x-y
#     return  c,d
# result1,result2=add(4,7)
# print(result1,result2)
# def update(x):
#     print(id(x))
#
#     x=8
#     print(id(x))
#     print(x)
#
# list =[12.22,43]
# print(id(list))
# update(list)
# print(list)
# print(list)

# def person(name,age):
#     print(name)
#     print(age)
#
# person(age=34,name='Mukesh')

# def sum(a,*b):
#     # c=a+b
#     c=a
#
#     for i in b:
#         c=c+i
#
#     print(c)
# sum(2,4,5,5)
# variable lenght arguments
# def person(name,**data):
#     print(name)
#     for i,j in data.items():
#         print(j)
#
# person("Mukesh",age=28,Gender="Male",MobileNo=38288)
# Golbal variable
# a=10
#
# def something():
#     # a=2
#     print(a)
#
#
# something();
# print(a)
#list pass metod
# def count(list):
#     even=0
#     odd=0
#     for i in list:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     return even,odd
# list=[20,13,34,45,85,65]
#
# even,odd=count(list)
# print("Even number count{}".format(even))
# print("Odd number count {}".format(odd))
# print("Even :{} and Odd {}".format(even,odd))
#fibonaio series
# def fib(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(a+b)
#         if c>100 and a <100:
#             print("less than 100 last number is {}".format(a))
# fib(14)

#lambda
# def square(a):
#     return a*a
# f=lambda a: a*a
# f=lambda a,b: a*b
# c=int(input("Enter any number "))
# b=int(input("Enter the second number"))
# result=f(c,b)
# print(result)




