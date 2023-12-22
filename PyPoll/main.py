# Import modules
import os
import csv

# Refer to the file resources and budget_data file
csvpath = os.path.join(".", "Resources", "election_data.csv") 

#Read the csv file using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (ie Mark the first row as a header , so that header is skipped in procedures)
    csv_header = next(csvreader)

    #Define variables
    Total_votes = 0
    Charles_counter = 0
    Diana_counter = 0
    Raymon_counter = 0
    Raymon_Percentage = 0
    Charles_Percentage = 0
    Diana_Percentage = 0
    Winner = 0


    # Print the outputs
    for row in csvreader:
        Total_votes = Total_votes + 1 

        # If the person polls a vote add to their counter
        if row[2] == "Charles Casper Stockham":
            Charles_counter = Charles_counter + 1

        elif row[2] == "Diana DeGette":
            Diana_counter = Diana_counter +1

        else : Raymon_counter = Raymon_counter + 1 

# Calculate the percentages to three decimal places in percentage formatt
Charles_Percentage = "{:.3f}%".format(Charles_counter / Total_votes*100)
Diana_Percentage = "{:.3f}%".format( Diana_counter / Total_votes*100)
Raymon_Percentage = "{:.3f}%".format(Raymon_counter / Total_votes *100)

# Find the winner using a if statement
if Charles_Percentage> Diana_Percentage and Charles_Percentage> Raymon_Percentage:
    Winner = "Charles Casper Stockham"
elif Diana_Percentage > Raymon_Percentage:
    Winner = "Diana DeGette"
else : Winner = "Raymon Anthony Doane"  


# Print the outputs
print(f"Election Results")

print(f"------------------------")

print(f"Total Votes: {Total_votes}")

print(f"------------------------")

print(f"Charles Casper Stockham: {Charles_Percentage} ({Charles_counter})")

print(f"Diana DeGette: {Diana_Percentage} ({Diana_counter})")

print(f"Raymon Anthony Doane: {Raymon_Percentage} ({Raymon_counter})")

print(f"------------------------")

print(f"Winner: {Winner}")

print(f"------------------------")



# Specify the file to write to
output_path = os.path.join(".", "Analysis", "PyPoll.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    # Write the outputs in the text file 
    txtfile.write(f"Election results\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Total Votes: {Total_votes}\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Charles Casper Stockham: {Charles_Percentage} ({Charles_counter})\n")
    txtfile.write(f"Diana DeGette: {Diana_Percentage} ({Diana_counter})\n")
    txtfile.write(f"Raymon Anthony Doane: {Raymon_Percentage} ({Raymon_counter})\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Winner: {Winner}\n")
    txtfile.write(f"------------------------")