class Income:
    def __init__(self,yincome):
        self.yincome=yincome
    def yearlyIncome(self):
        print('Your yearly income is $',self.yincome)

class Expense(Income):
    def __init__(self,yincome):
        super().__init__(yincome)
        self.dhukuti = 0.05 * self.yincome
        self.rent = 0.05 * self.yincome
        self.food = 0.05 * self.yincome
        self.transport = 0.05 * self.yincome
    def expenseOnRent(self):
        print("Your yearly expense on rent is $",self.rent)
    def expenseOnDhukuti(self):
        print("Your yearly expense on dunkuti is $",self.dhukuti)
    def expenseOnFood(self):
        print("Your yearly expense on food  is $",self.food)
    def expenseOnTransport(self):
        print("Your yearly expense on transportaion is $",self.transport)
    def totalExpesnseYearly(self):
        totalexpense=self.rent+self.dhukuti+self.food+self.transport
        print("total expense yearly is $",totalexpense)


class Saving(Income):
    def __init__(self,yincome):
        super().__init__(yincome)
        self.vacation=0.1 * self.yincome
        self.backup=0.15 * self.yincome
        self.health=0.05 * self.yincome
        self.insurence=0.05 * self.yincome
    def savingForVacation(self):
        print("total saving yearly  for vaccation is $", self.vacation)
    def savingForBackUp(self):
        print("total saving yearly  for backup is $", self.backup)
    def savingForHealth(self):
        print("total saving yearly  for health is $", self.health)
    def savingForInsurence(self):
        print("total saving yearly  for insurence is $", self.insurence)

    def totalYearlySaving(self):
        totalsaving=self.vacation+self.backup+self.health+self.insurence
        print("total saving yearly  is $",totalsaving)

class Tax(Income):
    def __init__(self,yincome):
        super().__init__(yincome)

    def totalYearlyTax(self):
        totaltax=0.35 * self.yincome
        print("total  yearly tax  is $", totaltax)

if __name__ == '__main__':
    name=input("Enter your name:")
    income=float(input("Enter ur yearly Income:"))
    print("Income Management structure==>",name)
    print("")
    print("......Income.......")
    objIncome=Income(income)
    objIncome.yearlyIncome()
    print("")

    print("......Tax.......")
    objtax=Tax(income)
    objtax.totalYearlyTax()
    print("")

    print("......Saving.......")
    objSaving=Saving(income)
    objSaving.totalYearlySaving()
    objSaving.savingForInsurence()
    objSaving.savingForHealth()
    objSaving.savingForBackUp()
    objSaving.savingForVacation()
    print("")

    print("..........Expenses.........")
    objExpense=Expense(income)
    objExpense.totalExpesnseYearly()
    objExpense.expenseOnTransport()
    objExpense.expenseOnRent()
    objExpense.expenseOnDhukuti()
    objExpense.expenseOnFood()

    print("")
    print("")
    print("........","Thankyou!!","........")