class Object:
    def __init__(self, name, price, inv, amt_sold):
            self.__name = name
            self.__price = price
            self.__inv = inv
            self.__amt_sold = amt_sold

    def get_name(self):
            return self.__name

    def get_price(self):
            return self.__price

    def get_inv(self):
            return self.__inv

    def get_amt_sold(self):
            return self.__amt_sold

    def set_name(self,name):
            self.__name = name

    def set_price(self, price):
            self.__price = price

    def set_inv(self, inv):
            self.__inv = inv

    def set_amt_sold(self, amt_sold):
            self.__amt_sold = amt_sold

    def display(self):
            print(f'Name: {self.__name} || Price: {self.__price} || Amount in Inventory: {self.__inv} || Amount Sold: {self.__amt_sold}')