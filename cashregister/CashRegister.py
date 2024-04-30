class CashRegister:
    def __init__(self):
        self.__item = []

    def purchase_item(self,retail_item):
        self.__item.append(retail_item)
        print(f"{retail_item.get_description()} has been added")

    def get_total(self):
        total = 0
        for x in self.__item:
            total = total + x.get_price()
        return total

    def show_item(self):
        print("The items in your cash register are:")
        for x in self.__item:
            print('\n'+str(x))

    def clear(self):
        self.__item = []