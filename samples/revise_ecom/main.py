from samples.revise_ecom.AccountInfo import *
from samples.revise_ecom.CustomerInfo import *
from samples.revise_ecom.ecomService import FlipkartServices
from samples.revise_ecom.VendorInfo import vendorInfo



if __name__ == '__main__':
    custAcc = Account(accNo=99111555, balance=15000, type='Saving')
    cust = Customer(custId="101", custName="AAAA", custAccount=custAcc)

    services = FlipkartServices() #Mobile7
    services.purchase_product('Mobile7', 19, 'Y', cust)

    print('-----------------------------')
    print(cust)

    print(vendorInfo)