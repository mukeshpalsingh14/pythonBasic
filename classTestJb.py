# class Computer:
#
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#
#     def config(self):
#         print("Computer Configuartion is",self.cpu,self.ram)
#
# comp=Computer("i7", 16)
# print(type(comp))

#Computer.config(comp)
##Class and object example
# class Computer:
#     def __init__(self):
#         self.name="Inder"
#         self.age=34
#     def update(self):
#         self.age=20
#
# c1=Computer()
# c2=Computer()
#
# c2.name="Mukesh"
# c2.age=33
# c2.update()
# print(c1.name,c1.age)
# print(c2.name,c2.age)

# class car:
#     wheel=4 #class variable
#
#     def __init__(self):
#         self.mil=10  #instance variable
#         self.comp="BMW"
#
# c1=car()
# c2=car()
# c2.mil=8
# c2.comp="Toyota"
# car.wheel=5
# print(c1.mil,c1.comp,c1.wheel)
# print(c2.mil,c2.comp,c2.wheel)
##Method
class student:
    school='Govt Model High School'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avarage(self):
        return  (self.m1+self.m2+self.m3)/3

s1=student(12,37,56)
s2=student(11,53,83)

print(s1.avarage())
print(s2)



