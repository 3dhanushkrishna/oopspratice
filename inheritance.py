#multilevel inheritance
class Season1(object):
    def __init__(self,summer,winter):
        self.summer = summer
        self.winter = winter
    def getmonths(self):
        print("summer:",self.summer)
        print("winter: ",self.winter)
class Season2(Season1):
    def __init__(self,summer,winter,rainy):
        self.rainy = rainy
        Season1.__init__(self,summer,winter)
    def displaymonths(self):
        print("summer:", self.summer)
        print("winter: ", self.winter)
        print("rainy: ", self.rainy)
class Season3(Season2):
    def __init__(self,summer,winter,rainy,spring):
        self.spring = spring
        Season2.__init__(self,summer,winter,rainy)

    def months(self):
        print("summer:", self.summer)
        print("winter: ", self.winter)
        print("rainy: ", self.rainy)
        print("spring: ", self.spring)
season = Season3("4months","4months","4months","4months")
season.months()
season.displaymonths()
season.getmonths()


