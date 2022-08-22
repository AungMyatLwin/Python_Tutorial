import math

class TestInterface:
    def __init__(self):
        pass

    def interface1(self):
        pass
    def pows(self):
        return math.ceil(-40)


class Testing(TestInterface):
    def __init__(self):
        super().__init__()
    def interface1(self):
         print("Overrided the class method")


t=TestInterface()
t.interface1()
print(t.pows())

ti=Testing()
ti.interface1()