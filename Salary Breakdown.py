import pandas as p
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from decimal import Decimal

#Salary = int(input("What is your yearly income?: "))
Salary = 80000
MonthlyIncome = int((Salary/12))
WeeklyIncome = int((MonthlyIncome/4))
print("Your monthly income is: $" + str(MonthlyIncome))
print("Your weekly income is: $" + str(WeeklyIncome))

#Rent = int(input("What is your monthly rent?: "))
#Gas = int(input("How much do you spend on gas per month?: "))
#Food = int(input("How much do you spend on groceries and eating out?: "))
#Insurance = int(input("How much do you spend on insurance and car payments?: "))
#Misc = int(input("Input the total amount of any other subscriptions and expenses?: "))
Rent = 1200
Gas = 200
Food = 400
Insurance = 800
Misc = 400

MonthlyExpenses = str(Rent+Gas+Food+Insurance+Misc)
print("Your total montly expenses is: $"+MonthlyExpenses)

MonthlySavings = (MonthlyIncome-(int(MonthlyExpenses)))
print("Your total montly savings is: $"+str(MonthlySavings))

YearlySavings = MonthlySavings*12
print("Your total yearly savings is: $"+str(YearlySavings))

fig, (ax1,ax2,ax3) = plt.subplots(1,3)
fig.set_facecolor((0.87,0.87,0.87))
fig.suptitle("The Allocation of an $"+str(Salary)+" Salary",fontsize=16)

MonthlyExpenses = int(MonthlyExpenses)
MonthlySavings = MonthlyIncome-MonthlyExpenses
Barwid = ["Monthly Income", "Monthly Expenses","Monthly Savings"]
Barhig = [MonthlyIncome, MonthlyExpenses, MonthlySavings]
colors = [(0.6,1,0.6),(1,0.6,0.6),(1,1,0.6)]

p1 = ax1.bar(Barwid,Barhig,width=0.4,align="center",color = colors,linewidth=1,edgecolor="k")
ax1.bar_label(p1,labels = ["$"+str(MonthlyIncome),"$"+str(MonthlyExpenses), "$"+str(MonthlySavings)],label_type="edge")
ax1.set_title("Monthly Income vs. Monthly Expenses")
ax1.set_facecolor((0.87,0.87,0.87))
ax1.set_xlim([-0.5,3])
xtick_loc = [0.1,1.15,2.2]
ax1.set_xticks([])
ax1.legend(iter(p1), ('Income', 'Expenses', 'Savings'))

MonthlyExpenses = int(MonthlyExpenses)
ExpensesList = [Rent,Gas,Food,Insurance,Misc]
PieSlice = []

for i in ExpensesList:
    PieSlice.append((i/MonthlyExpenses)*10)
    
labels = "Rent", "Gas", "Food", "Insurance/Car", "Misc"
textprops = {"fontsize":9}
colorlist = [(0.6,1,1),(1,1,0.6),(0.6,1,0.6),(1,0.6,0.6),(1,0.6,1)]
ax2.pie(PieSlice, labels=labels, explode=[0.15,0,0,0,0],autopct='%1.1f%%',colors=colorlist,pctdistance=0.7,shadow=True, startangle=90, wedgeprops={"edgecolor":"0","linewidth":1},textprops=textprops)
ax2.set_title("Monthly Expenses Allocation") 
ax2.axis('equal')


Barticks = ["Rent", "Gas", "Food", "Insurance & Car Payments", "Misc"]
colorlist = [(0.6,1,1),(1,1,0.6),(0.6,1,0.6),(1,0.6,0.6),(1,0.6,1)]
Barvalue = [Rent,Gas,Food,Insurance,Misc]
p2 = ax3.bar(Barticks,Barvalue,width=0.8,align="center",color=colorlist,linewidth=1,edgecolor="k")
ax3.bar_label(p2,labels = ["Rent", "Gas", "Food", "Insurance/Car", "Misc"])
ax3.set_xticks([])
ax3.set_ylabel("Dollars")
ax3.set_xlim([-1,5])
ax3.set_title("Expense Allocation")
ax3.set_facecolor((0.87,0.87,0.87))

plt.subplots_adjust(wspace=1)
plt.show()



    

