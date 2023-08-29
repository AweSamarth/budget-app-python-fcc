class Category:

    def __init__(self, categoryName):
        self.categoryName=categoryName
        self.ledger=[]
        self.totalFunds=0
        self.takenOut=0
    
    def __str__(self):
        leftLength=(30-len(self.categoryName))//2
        rightLength = 30-leftLength-len(self.categoryName)
        theString=(("*")*leftLength) + self.categoryName + (("*")*rightLength)+"\n" 
        
        for i in (self.ledger):

            theString+=f"{i['description'][:23]:<23}"
            tempString="{:.2f}".format(float(i['amount']))
            # print(tempString, "oidsjf")
            theString+=f"{tempString[:7]:>7}\n"
        
        theString+="Total: "+ str(round(self.totalFunds, 2))


        return theString

    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount, "description":description})
        self.totalFunds+=amount

    def withdraw(self, amount, description=""):
        if (self.check_funds(amount)==False):
            # print(self.check_funds(amount))
            # print(amount)
            # print(self.totalFunds)
            return False
        else:
            self.ledger.append({"amount":-abs(amount), "description":description})
            self.totalFunds-=amount
            self.takenOut+=amount
            # print("ok this is ", self.takenOut)
            return True
    def get_balance(self):
        return self.totalFunds

    def transfer(self, amount, otherCat):
        if(self.check_funds(amount)==False):
            
            return False
        else:
            self.withdraw(amount, ("Transfer to " + otherCat.categoryName))
            otherCat.deposit(amount, ("Transfer from "+self.categoryName))
            return True
    
    def check_funds(self, needed):
        if (float(self.totalFunds)>=float(needed)):
            return True
        else:
            return False
        
    
     
def create_spend_chart(listOfCategories):
    theRequiredString="Percentage spent by category\n"
    dictionary = {}
    temparray=[]
    overallExpenditure=0
    length = len(listOfCategories)
    for i in listOfCategories:
       overallExpenditure+=i.takenOut
    for i in listOfCategories:
        dictionary[i.categoryName] = (i.takenOut*100/overallExpenditure)
    
    for i in dictionary.values():
        temparray.append(i)
    i=100
    while (i>=0):
        string=""

        for j in dictionary.values():
            
            if j>=i:
                string += " o "
            else:
                string +="   "
        if(i<100 and i>=10):
            theRequiredString+=" "
        if(i<10):
            theRequiredString+="  "
        theRequiredString+=str(i)+'|'+string+" \n"
        i-=10
        # theString+=f"{str(round(i['amount'],2))[:7]:>7}\n"
    theRequiredString+="    "
    theRequiredString+="-"*(length*3+1)
    theRequiredString+="\n     "

    categoryNameLengthsArray=[]
    categoryNamesArray=[]
    for i in listOfCategories:
        categoryNameLengthsArray.append(len(i.categoryName))
        categoryNamesArray.append(i.categoryName)
    maxLength=max(categoryNameLengthsArray)
    for i in range (maxLength):
        for j in categoryNamesArray:
            if(len(j)>i):
                theRequiredString+=str(j[i])+"  "
            else:
                theRequiredString+="   "
        theRequiredString+="\n     "
    
    theRequiredString=theRequiredString[:-6]


    return theRequiredString
    


# huh = Category("dalfm")
# helloThere = Category ("dsogija")
# okthen = Category("sdapfi")
# alright = Category("Deez")

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.deposit(900, "deposit")

business.withdraw(10.99)
food.withdraw(105.55)
entertainment.withdraw(33.40)

print(create_spend_chart([business, food, entertainment]))

# huh.deposit(120, "teri hi")
# helloThere.deposit(100, "ok then")
# huh.deposit(1222222300.23232213213123,"dghadsiophf")
# huh.deposit(111, "osmedfiajdisofjsdiopffsiodfthing that")
# helloThere.deposit(200)
# huh.withdraw(100)
# helloThere.withdraw(200)
# okthen.deposit(300, "lmaolmo")
# alright.deposit(200)
# okthen.withdraw(150)
# alright.withdraw(50)

# print(huh.ledger)
# print(huh)

# print(create_spend_chart([huh, helloThere, okthen, alright]))

# print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")