
from samples.revise_ecom.Generic import Util
class Customer(Util):


    def __init__(self,custId,custName,custAccount):
        self.customerId=int(custId)
        self.customerName=custName
        self.customerAccount=custAccount
        self.customerProductList=[]



