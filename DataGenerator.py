import csv


def generate_binary_numbers(num_bits):
    result = []
    for i in range(2**num_bits):
        binary_number = bin(i)[2:].zfill(num_bits)
        result.append(binary_number)

    return result


def process_binary_number(bin_num):
    isPalindrome = bin_num == bin_num[::-1]

    return list(map(int, list(str(bin_num) + str(int(isPalindrome)))))


# Generate all 10-bit binary numbers
binary_nums_10bit = generate_binary_numbers(10)

# Data to be written to the CSV file
data = list(map(process_binary_number, binary_nums_10bit))

# Filename
file_name = "palindrome.csv"

# Writing to the CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Writing the data to the CSV file
    writer.writerows(data)

print("Data Generated Successfully")
