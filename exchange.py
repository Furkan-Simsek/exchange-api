## Exchange JSON API

import requests

class RealTimeCurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount

        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

            # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount

url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = RealTimeCurrencyConverter(url)
#print(converter.convert('TRY','USD',100))
def welcome():
    print("-*- Welcome Exchanger -*-")
    print("Please enter only 3 Letter International currency code \n \n")
    print("Q -> Exit\n1 -> Convert")
    answer= input(">: ")
    if answer.lower() == "q": exit()
    elif answer == "1": convert()
    else: print("Wrong input try again...")
def convert():
    amount = int(input("Enter the amount to be converted: "))
    firstMoneyC = input("Enter the currency to be converted: ")
    twoMoneyC = input("Enter the converted currency: ")
    print(f"{converter.convert(firstMoneyC, twoMoneyC, amount)} Amount converted from {firstMoneyC} to {twoMoneyC}")
    print("\n\n")
while 1:
    welcome()

