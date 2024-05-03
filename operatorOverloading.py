class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3

    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return  True
        else:
            return  False

sobj=student(2,5)
s1obj=student(3,6)

s3=sobj +s1obj
if sobj > s1obj:
    print("S1 is win")
else:
    print("S2 is win")


print(s3.m1)