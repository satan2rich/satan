import random
import requests
import requests
def generate_cc():
    # Generate a random credit card number
    cc_num = ''.join([str(random.randint(0, 9)) for _ in range(16)])
    return cc_num


def is_valid_cc(cc_num):
    # Check if the credit card number is valid using the Luhn algorithm
    reversed_digits = list(map(int, cc_num))[::-1]
    doubled = [d * 2 if i % 2 else d for i, d in enumerate(reversed_digits)]
    summed = sum(d // 10 + d % 10 for d in doubled)
    return summed % 10 == 0


def print_cc(cc_num, is_valid):
    # Print the credit card number with color based on its validity
    if is_valid:
        print(f"\033[92m{cc_num} (Valid)\033[0m")
    else:
        print(f"\033[91m{cc_num} (Invalid)\033[0m")


def generate_ccs(count):
    # Generate the specified number of credit card numbers and check their validity
    for i in range(count):
        cc_num = generate_cc()
        is_valid = is_valid_cc(cc_num)
        print_cc(cc_num, is_valid)


# Prompt the user for the number of credit card numbers to generate
print("How Many Card Do You Want To Gen")
count = input()
count = int(count)
generate_ccs(count)
# Generate the credit card numbers and print the results
generate_ccs(count)
input()
