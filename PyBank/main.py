import os
import csv

budget_data = os.path.join('02-Homework','03-Python','Instructions','PyBank', 'Resources', 'budget_data.csv')
#02-Homework\03-Python\Instructions\PyBank\Resources
budget_analysis = os.path.join('02-Homework','03-Python','Instructions','PyBank', 'analysis', 'budget_analysis.txt')

budgetdata_csv = "budget_data.csv"
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change = 0
profit_loss_change_list = []
month_change = []
greatest_increase = 0
greatest_decrease = 9999999999999999

with open(budget_data) as budget_data_csv:
   budget_data_csv_reader = csv.DictReader(budget_data_csv)
   # loop through the data
   #At initial stage you should take previousProfit_Losses as first row
   #So skip the first row
   index=0
   for row in budget_data_csv_reader:
       if(index==0):
           total_months+=1
           total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
           previous_profit_loss = int(row["Profit/Losses"])
           month_change = month_change + [row["Date"]]
           index+=1
           continue

       # The total number of months included in the dataset

       total_months = total_months + 1
       # The net total amount of "Profit/Losses" over the entire period
       total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
       profit_loss_change = int(row["Profit/Losses"]) - previous_profit_loss
       profit_loss_change_list.append(profit_loss_change)
       previous_profit_loss = int(row["Profit/Losses"])
       month_change = month_change + [row["Date"]]
      
   greatest_decrease=min(profit_loss_change_list)
   greatest_increase=max(profit_loss_change_list)
   #We have to add 1 because month associated with change is the next month
   greatest_decrease_month=profit_loss_change_list.index(greatest_decrease)+1
   greatest_increase_month=profit_loss_change_list.index(greatest_increase)+1
   output = (
   f"\nFinancial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total Profit/Losess: ${total_profit_loss}\n"
   f"Average Change: ${round(sum(profit_loss_change_list)/len(profit_loss_change_list),2)}\n"
   f"Greatest increase in Profits: {month_change[greatest_increase_month]} (${(str(greatest_increase))})\n"
   f"Greatest decrease in Profits: {month_change[greatest_decrease_month]} (${(str(greatest_decrease))})\n")
    
   # Print the output (to terminal)
   print(output)

   # Export the results to text file
   with open(budget_analysis, "w") as txt_file:
     txt_file.write(output)
  





