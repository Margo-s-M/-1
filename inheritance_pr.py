class Money:
    def __init__(self,whole_money, coin_money,currency="USD"):
        self.whole_money = whole_money
        self.coin_money = coin_money
        if 0 <= coin_money < 100:
            self.coin_money = coin_money
            self.currency = currency
    def display(self):
        print(f"{self.whole_money}{self.currency} {self.coin_money} peny")

    def add_money(self,money,coins):
        oll_coins = self.coin_money + coins
        oll_money = self.whole_money +money
        if  oll_coins >=100:
            oll_money += oll_coins //100
            oll_coins = oll_coins % 100

        self.whole_money = oll_money
        self.coin_money = oll_coins

    def