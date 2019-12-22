"""
20 Dec 2019
This program will convert numbers to and from binary and decimal.
It was written By Ryan Rogers for the purpose of practicing coding.
It will take input and decide wether or not it is a convertable number
then convert the number. Acceptable input is 8 digit 1s or 0s, or interger
between 0 and 255
"""

# takes number and returns true if it is binary
def check_if_binary(number):
    if len(number) != 8:
        binary = False
    else:
        for i in range(len(number)):
            if number[i] != "1" and number[i] != "0":
                binary = False
                break
            else:
                binary = True
    return binary

# takes number and returns true if decimal  
def check_if_decimal(number):
    try:
        if int(number) <= 255 and int(number) >= 0:
            decimal = True
        else:
            decimal = False
        return decimal
    except ValueError:
        decimal = False
    return decimal            

# play again logic
def again():
    while True:
        choice = input("Again? y/n: ")
        if choice == "y":
            again = True
            break
        if choice == "n":
            again = False
            break
        else:
            pass
    return again

# welcome banner
def welcome():
    print("Hello world, this is a program to convert binary numbers to decimal and visa versa")

# algorithm for converting binary number to decimal
def convert_bin_dec(number):
    answer = []
    decimals = [128,64,32,16,8,4,2,1]
    for i in range(len(number)):       
        if number[i] == "1":
            answer.append(decimals[i])
        else:
            pass
    print(sum(answer))

# algorithm for converting decimals to binary
def convert_dec_bin(number):
    binary = []
    decimals = [128,64,32,16,8,4,2,1]
    for i in range(8):
        if int(number) >= decimals[i]:
            number = int(number)
            binary.append("1")
            number = number - decimals[i]           
        else:
            binary.append("0")
    print("".join(binary))

# main function
def main():
    welcome()
    while True:
        number = input("Enter a number to convert: ")
        if check_if_binary(number) == True:
            convert_bin_dec(number)
        elif check_if_decimal(number) == True:
            convert_dec_bin(number)
        else:
            print("Check the number again?\n binary numbers are 8 digits long and contain 1 and or 0s,\n convertable decimals are 0-255")
        if again() == False:
            break
        else:
            pass
main()
