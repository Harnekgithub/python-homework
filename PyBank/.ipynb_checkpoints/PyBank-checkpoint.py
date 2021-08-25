#import csv library and OS libraries for dependencies
import csv
import os

#Declare the list variables for reading the csv file columns to do analysis
months = []
monthly_pnl = []
change_in_profit = []

#Declare the variables for data analysis
max_profit_month = 0
max_loss_decrease = 0
num_of_months = 0
profit_loss = 0
average_pnl = 0
max_profit_change = 0
least_loss_change = 0

#Declare the String variables for data analysis
max_profit_month = ""
max_loss_month = ""

#Set the name of the output file for financial analysis report
outputfile = "Financial Analysis.txt"

# Set the path for the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the csv
with open(csvpath, newline="") as csvfile:
    
    reader = csv.reader(csvfile, delimiter = ",")
#    csvrow = next(csvfile)
    print(csvrow)
    for row in reader:
        # Creating list of months
        months.append(row[0])
        
        # Creating list of monthly profit/loss
        monthly_pnl.append(int(row[1]))
           
    #Total of profit or loss use the sun function on the list to calculate the total profit or loss
    profit_loss = sum(monthly_pnl)

    #calculating num of months in the data set
    num_of_months = len(monthly_pnl)
  
    #Create the a list to store month over month change 
    for i in range(num_of_months - 1):
        change_in_profit.append(monthly_pnl[i+1] - monthly_pnl[i])
    
    #Use max() function to find the max value in the list
    max_profit_change = max(change_in_profit)
    
    #Use min() function to find the min value in the list
    max_loss_decrease = min(change_in_profit)
    
    #Populate the month for max change in profit +1 is used as the it is next month's data
    max_profit_month_index = change_in_profit.index(max(change_in_profit)) +1
    max_profit_month = months[max_profit_month_index]
    
    #Populate the month for max change in loss +1 is used as the it is next month's data
    max_loss_month_index = change_in_profit.index(min(change_in_profit)) +1
    max_loss_month = months[max_loss_month_index]
    
    #Calculating the average change in the profit by dividing total change 
    #in profit divided by number of months to two decimal places
    average_pnl = round(sum(change_in_profit)/len(change_in_profit), 2)
    
    #print the report in a text file
    print("Financial Analysis")
    print("---------------------------------------------------")
    print(f"Total number of months is the data set: {num_of_months}")
    print()
    print(f"Net profit over {num_of_months} months is ${profit_loss}")
    print()
    print(f"Average change over {num_of_months} months is ${average_pnl}")
    print()
    print(f"Greatest Increase in Profits: {max_profit_month} ${max_profit_change}")
    print()
    print(f"Greatest Decrease in Profits: {max_loss_month} ${max_loss_decrease}" )
    
    #Generate the report in a text file named "Financial_Analysis;txt"
    with open(outputfile, 'w') as file:
        file.write("\n")
        file.write("Financial_Analysis\n")
        file.write("---------------------------------------------------\n\n")
        file.write(f"Total number of months is the data set: {num_of_months}\n\n")
        file.write(f"Net profit over {num_of_months} months is ${profit_loss}\n\n")
        file.write(f"Average change over {num_of_months} months is ${average_pnl}\n\n")
        file.write(f"Greatest Increase in Profits: {max_profit_month} ${max_profit_change}\n\n")
        file.write(f"Greatest Decrease in Profits: {max_loss_month} ${max_loss_decrease}" )
   
    