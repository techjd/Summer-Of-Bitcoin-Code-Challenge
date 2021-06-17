# Written By Jaydeepsinh Parmar
# Contact At :- jaydeepparmar253@gmail.com
# LinkedIn:- https://www.linkedin.com/in/techjd/
# Solution of Summer Of Bitcoin Challenge

# importing csv module
import csv

# CSV file name
filename = "mempool.csv"

# Initializing the titles and rows list
fields = []
rows = []

# Reading CSV File
with open(filename, 'r') as csvfile:
    # Creating a CSV Reader Object
    csvreader = csv.reader(csvfile)

    # Extracting Field Names Through First Row
    fields = next(csvreader)

    # Extracting Each Data Row One By One and adding it in rows list
    for row in csvreader:
        rows.append(row)

# Printing Fields Names and Length for Reference
# print('Field Names are : ' + ' , '.join(field for field in fields))
# print(len(rows))
# print('\n')

# Removing the parent Transactions field if it's not present
for idx, row in enumerate(rows[:len(rows)]):
    for i, j in enumerate(row[:len(row)]):
        if row[i] == '':
            row.pop()
            # print(row)
        else:
            pass

max_weight = 4000000  # Initializing The Max Weight
curr_weight = 0  # Initializing curr_weight ( Will Be used in later part of code )

# Iterating Through Whole Mempool CSV File
for ind, row in enumerate(rows[:len(rows)]):
    # Opening Block.txt file in append mode to append in file
    with open("block.txt", "a") as file:
        # if length of a single row is 4 i.e if parent transaction is present
        if len(row) == 4:
            # Checking if the parent transaction is a single txn_id OR Multiple txn_ids
            if ';' in row[3]:
                # If there are multiple txn_ids then converting it into list so that we can access it one by one
                parent_txns = row[3].split(';')
                # Assigning Value of curr_weight to the current index row as we will add all these later on to check
                # if they exceeds max_weight or not
                curr_weight = int(row[2])
                # At this step we are iterating into the parent_txn ( Here we are only integrating into those
                # parent_txs which are having multiple txn )
                for j in parent_txns[:len(parent_txns)]:
                    # Here we will start iterating from the beginning of the file to index - 1 in mempool csv file
                    for i in rows[:ind]:
                        # If we found out that the txn_id and the txn_id present in parent_txn are equal we are
                        # adding the weight to cuu_weight , We are also checking if curr_weight is greater than
                        # max_weight . If it's getting greater then we will simply not do anything OR else we will
                        # append those txn_ids to the block.txt file
                        if i[0] == j:
                            curr_weight += int(i[2])
                            if curr_weight > max_weight:
                                pass
                            else:
                                # If curr_weight is less than max_weight then we will simply write it to block.txt
                                file.write(i[0])
                                # Creating A New Line
                                file.write("\n")
                                print(i[0])
                        else:
                            pass
                    # Creating A New Line After Iteration
                    file.write("\n")
                    # Assigning Current Weight to 0 After 1 iteration is complete
                    curr_weight = 0
            else:
                # Assigning Value of curr_weight to the current index row as we will add all these later on to check
                # if they exceeds max_weight or not
                curr_weight = int(row[2])
                # Here again we will be iterating in the whole mempool csv file from 0 till current index - 1
                for i in rows[:ind]:
                    # If at any point in iteration we found that parent_txn is equal to txn_id ,
                    # we will add the weight of that txn_id to current one .
                    if i[0] == row[3]:
                        curr_weight += int(i[2])
                        if curr_weight > max_weight:
                            pass
                        else:
                            # If curr_weight doesn't exceeds then we will simply write to file
                            # Writing to File
                            file.write(i[0])
                            # Adding a New Line After Appending a New Line
                            file.write("\n")
                            print(i[0])
                    else:
                        pass
                # Assigning Current Weight to 0 After 1 iteration is complete
                curr_weight = 0
            # Closing File
            file.close()
        else:
            pass
