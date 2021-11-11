import pandas as p
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from decimal import Decimal

Salary = int(input("What is your yearly income?: "))
MonthlyIncome = int((Salary/12))
WeeklyIncome = int((MonthlyIncome/4))
print("Your monthly income is: $" + str(MonthlyIncome))
print("Your weekly income is: $" + str(WeeklyIncome))

Rent = int(input("What is your monthly rent?: "))
Gas = int(input("How much do you spend on gas per month?: "))
Food = int(input("How much do you spend on groceries and eating out?: "))
Insurance = int(input("How much do you spend on insurance and car payments?: "))
Misc = int(input("Input the total amount of any other subscriptions and expenses?: "))

MonthlyExpenses = str(Rent+Gas+Food+Insurance+Misc)
print("Your total montly expenses is: $"+MonthlyExpenses)

MonthlySavings = (MonthlyIncome-(int(MonthlyExpenses)))
print("Your total montly savings is: $"+str(MonthlySavings))

YearlySavings = MonthlySavings*12
print("Your total yearly savings is: $"+str(YearlySavings))

fig, (ax1,ax2) = plt.subplots(2,1)
MonthlyExpenses = int(MonthlyExpenses)
ExpensesList = [Rent,Gas,Food,Insurance,Misc]
PieSlice = []

for i in ExpensesList:
    PieSlice.append((i/MonthlyExpenses)*10)
    
labels = "Rent", "Gas", "Food", "Insurance & Car Payments", "Misc"
ax1.pie(PieSlice, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, wedgeprops={"edgecolor":"0","linewidth":1})
ax1.set_title("Monthly Expenses Allocation")
ax1.axis('equal')

MonthlySavings = MonthlyIncome-MonthlyExpenses
Barwid = ["Monthly Income", "Monthly Expenses","Monthly Savings"]
Barhig = [MonthlyIncome, MonthlyExpenses, MonthlySavings]
colors = [(0.6,1,0.6),(1,0.6,0.6),(1,1,0.6)]

p1 = ax2.bar(Barwid,Barhig,width=0.4,align="center",color = colors,linewidth=1,edgecolor="k")
ax2.bar_label(p1,labels = ["$"+str(MonthlyIncome),"$"+str(MonthlyExpenses), "$"+str(MonthlySavings)],label_type="center")

ax2.set_ylabel("Dollars")
ax2.set_title("Monthly Income vs. Monthly Expenses")
plt.show()



    

