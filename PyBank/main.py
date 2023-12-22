
# Import modules
import os
import csv

# Refer to the file resources and budget_data file
csvpath = os.path.join(".", "Resources", "budget_data.csv") 

#Read the csv file using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (ie Mark the first row as a header , so that header is skipped in procedures)
    csv_header = next(csvreader)

    #Define variables
    Total_months = 0
    Total_Net = 0
    Profit_Loss = 0.00
    Prior_Profit_Loss = 0.00
    Net_change = 0.00
    Average_change= 0.00
    Lowest_Net_change = 0.00  
    Greatest_Net_change = 0.00
    Average_months = 0
    Net_change_list = []
    Greatest_month_index = []
    Lowest_month_index = []
    Month_List = []



    # Read each row of data after the header
    for row in csvreader:
        Total_months = Total_months + 1
        
        #Sums the 2nd column 
        Total_Net = Total_Net + int(row[1])   

        # Start if statement for when the row is greater than 1. Ignoring the header. 
        if Total_months > 1:
            Profit_Loss = int(row[1])
            
            #Calculate net change
            Net_change = Profit_Loss - Prior_Profit_Loss
            
            #Create a list for Net change based on the calculation
            Net_change_list.append(Net_change)
            
            #Create a list for months for the first column 
            Month_List.append(row[0])

            # Calculate max and min in the Net change list
            Greatest_Net_change = max(Net_change_list)
            Lowest_Net_change = min(Net_change_list)

        # Take the prior profit loss for each row    
        if Total_months > 0 :
            Prior_Profit_Loss = int(row[1])      
        
    # Caclulate average change and round to two dec places    
    Average_change = sum(Net_change_list)/len(Net_change_list)
    Average_changes = round( Average_change , 2)
    
    # Find the index of the Greatest and Lowest change
    Greatest_month_index = Net_change_list.index(Greatest_Net_change)
    Lowest_month_index = Net_change_list.index(Lowest_Net_change)

    # Output of the month list using the index above
    Greatest_month = Month_List[Greatest_month_index]
    Lowest_month = Month_List[Lowest_month_index]

# Print out all the outputs plus strings using f string

print(f"Financial Analysis")

print(f"----------------------------")

print(f"Total Months: {Total_months}")

print(f"Total: ${Total_Net}")

print(f"Average Change: ${Average_changes}")

print(f"Greatest Increase in Profits: {Greatest_month} (${Greatest_Net_change})")

print(f"Greatest Decrease in Profits: {Lowest_month} (${Lowest_Net_change})")

# Specify the file to write to
output_path = os.path.join(".", "Analysis", "PyBank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    # Write the outputs of the Financial Analysis task
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Months: {Total_months}\n")
    txtfile.write(f"Total: ${Total_Net}\n")
    txtfile.write(f"Average Change: ${Average_changes}\n")
    txtfile.write(f"Greatest Increase in Profits: {Greatest_month} (${Greatest_Net_change})\n")
    txtfile.write(f"Greatest Decrease in Profits: {Lowest_month} (${Lowest_Net_change})")