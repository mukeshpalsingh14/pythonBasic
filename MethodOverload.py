#MethodOverload
# class student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#
#     def sum(self, a=None,b=None,c=None):
#         s=0
#         if a!=None and b!=None and c!=None :
#             s=a+b+c
#         elif a!=None and b!=None:
#             s=a+b
#         else:
#             s=a
#         return s
#
#
# s1=student(20,30)
# print(s1.sum(4,5))
##MethodOverWriting
class A:
    def show(self):
        print("in A Show")

class B(A):
    def show(self):
        print("in B Show")

Aobj=B()
Aobj.show()

nums=[23,16,83,53]
it=iter(nums)
print(it.__next__())
print(next(it))