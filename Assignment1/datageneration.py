# Author: Vivek Pawar; Date : 20/01/2024
import csv
palindrome_list = []

# Function to check if the given number is palindrome of not
def isPalindrome(x):
    temp = x
    rev = 0
    for i in range(10):
        ld = temp%2
        rev = rev*2+ld
    return rev == x

# Iterate from 0 to 1023 (encluding edge values)
for i in range(1024):
    palindrome_dict = {} # To store instance of dataset in key value pair
    temp = i
    for j in range(10):
        palindrome_dict['x'+str(j)] = temp%2 # Store 10 instances of the dataset
        temp //= 2;
    
    # If number is palindrome mark the output labes as 1 else 0
    if isPalindrome(i):
        palindrome_dict['y'] = 1
    else :
        palindrome_dict['y'] = 0
    palindrome_list.append(palindrome_dict)


# Get the fields name for the dataset
fields = palindrome_list[0].keys()

# Write the list of dictiory to csv file
with open("palindrome_data.csv", "w") as datafile:
    # Initialize the csv writer object for datafile
    writer = csv.DictWriter(datafile, fieldnames=fields)

    # Write header fields in the csv file
    writer.writeheader()

    # Write rows of csv file
    writer.writerows(palindrome_list)




