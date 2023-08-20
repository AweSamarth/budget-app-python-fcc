import budget
from budget import create_spend_chart
from unittest import main


class Category:
    x=0
    categoryName=""
    def __init__(self, categoryName):
        self.categoryName=categoryName
    def newFunc(self):
        self.x=23
        print(self.x)
    print(x)

class LedgerClass:
    amount=0
    description=""
    def __init__(self, amount, description="okthen"):
        self.amount=amount
        self.description=description
        print(self.amount)
        print(self.description)

    def viewer(self):
        print(self.amount)
        print(self.description)
    

some = Category("huh")
ledgerCheck = LedgerClass(123)
ledgerCheck.viewer()
# some.newFunc()
# print(some.x)
# print(some.categoryName)