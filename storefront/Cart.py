from Object import *

class Cart_Item(Object):
    def __init__(self, name, price, inv, amt_sold, amt_in_cart):
        super().__init__(name, price, inv, amt_sold)
        self.__amt_in_cart = int(amt_in_cart)

    def get_amt(self):
        return self.__amt_in_cart

    def set_amt(self,amt_in_cart):
        self.__amt_in_cart = amt_in_cart

    def display(self):
        print(f'Name: {self.get_name()} || Price: {self.get_price()} || Amount in Inventory: {self.get_inv()} || Amount in Cart: {self.__amt_in_cart}')

