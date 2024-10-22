# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
changes_net = []
months = []
profit_losses = []
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
   
    # Skip the header row
    header = next(reader)

     # Extract first row to avoid appending to net_change_list
    for row in reader:
     
    # Track the total and net change
    
        months.append(row[0])
        profit_losses.append(int(row[1]))

 


        # Track the total
        total_months = len(months)
        # Track the net change
    for net_row in range(1, total_months):
            change_net = profit_losses[net_row] - profit_losses[net_row-1]
            changes_net.append(change_net)
            net_total = sum(profit_losses)
        # Calculate the greatest increase in profits (month and amount)
greatest_increase = max(changes_net)
greatest_increase_date = months[changes_net.index(greatest_increase) + 1]
        # Calculate the greatest decrease in losses (month and amount)

greatest_decrease = min(changes_net)
greatest_decrease_date = months[changes_net.index(greatest_decrease) + 1]

# Calculate the average net change across the months
average_change = sum(changes_net) / len(changes_net)


# Generate the output summary
# Print the output
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
output = f"""Financial Analysis
-----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
"""

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
