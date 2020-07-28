class Tax:
    def __init__(self,name,income):
        self.name=name
        self.income=income

    def tax_per_annum(self):
        yearly_income=self.income
        yearly_tax=0
        if yearly_income in range(18201):
            return yearly_tax
        elif yearly_income in range(18201,37001):
            yearly_tax=(yearly_income-18200)*0.19
            return yearly_tax
        elif yearly_income in range(37001, 80001):
            yearly_tax = 3572+(yearly_income - 80000) * 0.325
            return yearly_tax
        elif yearly_income in range(80001, 180001):
            yearly_tax = 17547+(yearly_income - 17547) * 0.37
            return yearly_tax
        else:
            yearly_tax=54547+(yearly_income-18200)*0.45
            return yearly_tax

name=input("Enter your name")
salary=int(input("Enter your Yearly Income"))
tax=Tax(name,salary)
print(tax.name," pays ",tax.tax_per_annum(),"as yearly IncomeTax")