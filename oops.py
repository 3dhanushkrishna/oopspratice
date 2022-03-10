class Dog:
    def __init__(self,breed,region,price):
        self.breed = breed
        self.region = region
        self.price = price
    def getdetails(self):
        print(self.breed)
        print(self.region)
        print(self.price)
dog1 = Dog("germen shepherd","american","10000")
dog2 = Dog("pomeranian","indian","15000")

dog1.getdetails()
dog2.getdetails()