
class Student:

    def __init__(self,sid,snm,age):
        self.studId = sid
        self.studName=snm
        self.studAge=age

    def __str__(self):
        return '\n Id : {}, Name : {}, Age :{}'.format(self.studId,self.studName,self.studAge)


s1 = Student(101,"AATT",22)
s2 = Student(102,"AAYY",32)
s3 = Student(103,"AAXX",52)
s4 = Student(104,"AANN",26)

print(s1) #student -- str

listOfStudents = [s1,s2,s3,s4]

for st in listOfStudents:
    print(st)
