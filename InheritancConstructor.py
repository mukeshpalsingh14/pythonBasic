class A:
    def __init__(self):
        print("In A Init")

    def feature(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B: # B(A):
    def __init__(self):
        # super().__init__()
        print("In B Init")
    def featur3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


class C(A,B):
    def __int__(self):
        super().__init__()
        print("In C init")

A1=C()
