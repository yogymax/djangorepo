from abc import ABC,abstractmethod
from samples.revise_ecom.VendorInfo import vendorInfo
from samples.revise_ecom.CustomerInfo import Customer
from samples.revise_ecom.AccountInfo import Account
from samples.revise_ecom.ProductInfo import Product
class VendorServices(ABC):

    @abstractmethod
    def purchase_product(self):#avlbl qty cqty*pric<cust.acc.balance# - in + clist balance-cust + ven
        pass

    @abstractmethod
    def refund_product(self):
        pass



class FlipkartServices(VendorServices):

    def purchase_product(self,pname,qty,pcat,cust):
        inventoryProducts = vendorInfo['inventory'] #all products from ven -- 8
        print('Customer {} requested for'.format(cust.customerName), pname,qty,pcat,cust.customerAccount.accountBalance)

        qty_ablb =False
        cust_balance =False
        is_product_avlb = False
        is_category_avlv=False


        for product in inventoryProducts:  #8
            #if product.productName==pname: and product.productCategory==pcat and product.productQty>=qty:
            if product.productName == pname:
                #print('product available with name',product.productName)
                is_product_avlb=True
                if product.productCategory==pcat:
                    #print('product categories avaible', product.productCategory)
                    is_category_avlv=True
                    if product.productQty>=qty:
                        print('product Available')
                        qty_ablb=True
                        totalbill = product.productPrice * qty
                        if cust.customerAccount.accountBalance>=totalbill:
                            cust_balance=True
                            cust.customerAccount.accountBalance-=totalbill
                            vendorInfo['Account'].accountBalance+=totalbill
                            print('Customer needs to Pay',totalbill)
                            product.productQty-=qty
                            prod = Product(pid=product.productId, pnm=product.productName,
                                    pcat=product.productCategory, pprice=product.productPrice,
                                           qty=qty)
                            cust.customerProductList.append(prod)

                            print('trascantion succesful...')
                        else:
                            print('trascantion not succesful...')
                            break

        if qty_ablb==False:
            if is_category_avlv==True:
                print('quanties not avaible')
            elif is_product_avlb==True:
                print('Categories not avaible')
            else:
                print('Not available')

        if cust_balance==False and qty_ablb==True:
            print('insufficient balance')



    def refund_product(self,prodId,qty):
        pass


