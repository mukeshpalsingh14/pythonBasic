#Netest Class
class macbook:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        # self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollno)


    class Laptop:
        def __init__(self):
            self.Brand="HP"
            self.Processor="i7"
            self.Ram="16GB"
            self.HardDisk="1TB"

        def show(self):
            print(self.Brand,self.Ram,self.Processor)

s1 =macbook("mukesh",2)
s2 =macbook("Inderpreet",4)

# print(s1.name,s1.rollno)

s1.show()
Lap1=macbook.Laptop()
# print(s1.lap.Brand)
print((Lap1.Brand))
Lap1.show()