import csv
import os


# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

#Path to collect data from Resources folder
budget_data_csv = os.path.join('Resources' , budget_data.csv')

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

def print_Financial Analysis():
    print(f"Financial Analysis")

# Declare file location through pathlib

input_file = Path("python-challenge", "PyBank", "budget_data.csv")

# Create empty lists to iterate through specific rows for the following variables

total_months = []

total_profit = []

monthly_profit_change = []

# Open csv in default read mode with context manager

with open(input_file,newline="") as budget:

# Store the contents of budget_data.csv in the variable csvreader

    csvreader = csv.reader(budget,delimiter=",") 

# Skip the header labels to iterate with the values

header = next(csvreader)  

# Iterate through the rows in the stored file contents

    for row in csvreader: 



        # Append the total months and total profit to their corresponding lists

        total_months.append(row[0])

        total_profit.append(int(row[1]))



    # Iterate through the profits in order to get the monthly change in profits

    for i in range(len(total_profit)-1):

        

        # Take the difference between two months and append to monthly profit change

        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

        

# Obtain the max and min of the the montly profit change list

max_increase_value = max(monthly_profit_change)

max_decrease_value = min(monthly_profit_change)



# Correlate max and min to the proper month using month list and index from max and min

#We use the plus 1 at the end since month associated with change is the + 1 month or next month

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1

max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements


print("Financial Analysis")

print("----------------------------")

print(f"Total Months: {len(total_months)}")

print(f"Total: ${sum(total_profit)}")

print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")

print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")

print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")



# Output files

output_file = Path("python-challenge", "PyBank", "Financial_Analysis_Summary.txt")



with open(output_file,"w") as file:

    

# Write methods to print to Financial_Analysis_Summary 

    file.write("Financial Analysis")

    file.write("\n")

    file.write("----------------------------")

    file.write("\n")

    file.write(f"Total Months: {len(total_months)}")

    file.write("\n")

    file.write(f"Total: ${sum(total_profit)}")

    file.write("\n")

    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")

    file.write("\n")

    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")

    file.write("\n")

    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
# Lists
#The total number of months included in the dataset
end_date = datetime. datetime(2017,2)
start_date = datetime. datetime(2010, 1)
num_months = (end_date. year - start_date. year) * 12 + (end_date. month - start_date. month)


The net total amount of "Profit/Losses" over the entire period


The average of the changes in "Profit/Losses" over the entire period


The greatest increase in profits (date and amount) over the entire period


The greatest decrease in losses (date and amount) over the entire period


Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
