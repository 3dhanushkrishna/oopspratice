class Cryptocurrency:
    def __init__(self):
        self.__usdt = 80
    def viewprice(self):
        print(self.__usdt)
    def hikeprice(self,usdt):
        self.__usdt=usdt
market = Cryptocurrency()
market.viewprice()
market.__usdt = 85
market.viewprice()
market.hikeprice(76)
market.viewprice()




