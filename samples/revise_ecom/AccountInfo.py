from samples.revise_ecom.Generic import Util

class Account:


    def __init__(self,accNo,balance,type):
        self.accountNo=accNo
        self.accountBalance=balance
        self.accountType=type

    def __str__(self):
        return f'\n\n {self.__dict__}'

    def __repr__(self):
        return str(self)
