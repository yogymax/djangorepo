
from samples.bdir.newfile import m1,m2

class Student:

    def __init__(self,sid,snm,age):
        self.studId = sid
        self.studName=snm
        self.studAge=age

    def __str__(self):
        return '\n Id : {}, Name : {}, Age :{}'.format(self.studId,self.studName,self.studAge)


