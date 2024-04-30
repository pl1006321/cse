class RetailItem:
    def __init__(self, desc, inv, price):
        self.__desc = desc
        self.__inv = int(inv)
        self.__price = float(price)

    def get_desc(self):
        return self.__desc

    def get_inv(self):
        return self.__inv

    def get_price(self):
        return self.__price

    def set_desc(self,desc):
        self.__desc = desc

    def set_inv(self,inv):
        self.__inv = int(inv)

    def set_price(self,price):
        self.__price = int(price)

    def __str__(self):
        return(f"{self.__desc} / Inventory: {self.__inv} Price: {self.__price}")

