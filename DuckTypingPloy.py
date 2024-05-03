class Pycham:
    def execute(self):
        print("Compiling")
        print("Running")
class DuckType:
    def execute(self):
        print("Swimming Duck")
        print("Fly Duck")
class Laptop:

    def code(self,ide):
        ide.execute()

ide=Pycham()
red=DuckType()

Lap1=Laptop()
Lap1.code(ide)
Lap1.code(red)

