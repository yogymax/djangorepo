
num = 20

def f1():
    print('inside instance method')


class Student:
    collegeName = "PICT"

    def m1(self):
        print('inside instance method')

    @staticmethod
    def m2():
        print('inside static method')

    @classmethod
    def m3(cls):
        print('inside class method')


a = Student()
a.m1()
a.m2()
a.m3()


s1 = Student()
print(id(s1))
print(id(s1.m1))
print(id(Student.m2))
print(id(Student.m3))
print('---------------------')
s2 = Student()
print(id(s2))
print(id(s2.m1))
print(id(Student.m2))
print(id(Student.m3))

print(Student.__dict__)
print(s1.__dict__)
print(s2.__dict__)