# def div(a,b):
#     return  a/b
#
# def smartFun(func):
#     def innerFun(a,b):
#         if a<b:
#             a=a+b
#             b=a-b
#             a=a-b
#             return  func(a,b)
#     return  innerFun
# # print(div(4,2))
# div=smartFun(div)
def div(a,b):
    print(a/b)

def smart(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return  inner

div = smart(div)

div(2,4)

# import  Calc
from Calc import *
a=9
b=3

c=add(a,b)
print(c)