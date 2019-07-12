from samples.revise_ecom.AccountInfo import Account
from samples.revise_ecom.ProductInfo import Product

p1 = Product(pid=11223,pnm='Mobile1',pcat='E',pprice=3932.2,qty=10)
p2 = Product(pid=12335,pnm='Mobile2',pcat='A',pprice=73932.2)
p3 = Product(pid=15233,pnm='Mobile3',pcat='E',pprice=932.2)
p4 = Product(pid=18233,pnm='Mobile4',pcat='C',pprice=83932.2,qty=23)
p5 = Product(pid=19233,pnm='Mobile5',pcat='R',pprice=3332.2)
p6 = Product(pid=712235,pnm='Mobile6',pcat='E',pprice=93932.2,qty=7)
p7 = Product(pid=67236,pnm='Mobile7',pcat='Y',pprice=3332.2,qty=9)
p8 = Product(pid=22339,pnm='Mobile8',pcat='E',pprice=13932.2)


listOfProducts = [p1,p2,p3,p4,p5,p6,p7,p8]
venAcct = Account(accNo=11223344,balance=12943.33,type='Current')
vendorInfo = {
    "Id" : "FLIP28384X",
    "Name": "Flipkart",
    "Account":venAcct,
    "inventory":listOfProducts
}




#print(vendorInfo)
