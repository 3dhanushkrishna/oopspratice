def addtion(sum):
    print("execute these 1st")
    def variables(a, b):
        print(a)
        print(b)
        return sum(a, b)
    return variables
@addtion
def plus(a, b):
    print(a + b)
plus(23 , 1)