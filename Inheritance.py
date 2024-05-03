class A:
    def feature(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B:
    def featur3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(B):
    def feature5(self):
        print("Feature 5 is working")




Aobj=A()

Aobj.feature()
Aobj.feature2()

Bobj=B()
Bobj.featur3()
Bobj.feature4()

Cobj=C()
Cobj.feature5()

class D(A,B):
    def feature6(self):
        print("Feature 6 is working")


Dobj=D()
Dobj.feature()
Dobj.feature2()
Dobj.featur3()