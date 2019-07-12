
from abc import ABC,abstractmethod

class StudService(ABC): #cannot be instantiated

    @abstractmethod
    def add_student(self):
        pass


    @abstractmethod
    def get_student(self):
        pass



    def get__all_students(self):
        pass

class NewServiceImpl(StudService):

    def get_student(self,a,b):
        pass