from samples.revise_ecom.Generic import Util

class Product(Util):

    def __init__(self,pid,pnm,pcat,pprice,qty=5):
        self.productId=pid
        self.productName=pnm
        self.productPrice=pprice
        self.productCategory=pcat
        self.productQty=qty

    def __str__(self):
        return f'\n\n {self.__dict__}'

    def __repr__(self):
        return str(self)