from Person import *

class Customer(Person):
    def __init__(self,name,address,phone_num,customer_num,mailing_list):
        super().__init__(name,address,phone_num)
        self.__customer_num = customer_num
        self.__mailing_list = mailing_list

    def get_customer_num(self):
        return self.__customer_num

    def get_mailing_list(self):
        return self.__mailing_list

    def set_customer_num(self,customer_num):
        self.__customer_num = customer_num

    def set_mailing_list(self,mailing_list):
        self.__mailing_list = mailing_list

    def __str__(self):
        return(f'Name: {self.__name} \nAddress: {self.__address}\nPhone number: {self.__phone_num} \nCustomer number: {self.__customer_num} \nMailing list: {self.__mailing_list}')