from sys import argv
import argparse

def message_to_ham(message):
    if(len(message) < 11):
        print("Messages should be a length of 11")
    #1 = col 2 and col 4
    #2 = col 3 and col 4
    #4 = row 2 and row 4
    #8 = row 3 and row 4
    #0 = everything i
    one = message[0] + message[1] + message[3] + message[4] + message[6] + message[8] + message[10] 
    two = message[0] + message[2] + message[3] + message[5] + message[6] + message[9] + message[10] 
    four = message[1] + message[2] + message[3] + message[7] + message[8] + message[9] + message[10]   
    eight = message[4] + message[5] + message[6] + message[7] + message[8] + message[9] + message[10]    
    one = determine_bit(one)
    two = determine_bit(two)
    four = determine_bit(four)
    eight = determine_bit(eight)
    zero = one + two + message[0] + four + message[1:4] + eight + message[4:11]
    ham = determine_bit(zero) + zero 
    matrix_pretty_print(ham)    
    
def ham_to_message(ham):
    if(len(ham) < 16):
        print("Ham messages should be a length of 16")
    #1 = col 2 and col 4
    #2 = col 3 and col 4
    #4 = row 2 and row 4
    #8 = row 3 and row 4
    #0 = everything i
    one = ham[3] + ham[5] + ham[7] + ham[9] + ham[11] + ham[13] + ham[15] 
    two = ham[3] + ham[6] + ham[7] + ham[10] + ham[11] + ham[14] + ham[15] 
    four = ham[5] + ham[6] + ham[7] + ham[12] + ham[13] + ham[14] + ham[15]   
    eight = ham[9] + ham[10] + ham[11] + ham[12] + ham[13] + ham[14] + ham[15]    
    
    error = []
    one = determine_bit(one)
    if one != ham[1]:
        error.append(1)  
        print("You have an error in column 2 or 4.")
        matrix_pretty_print(" x x x x x x x x")
    else:
        print("There are no errors in column 2 or 4.")
        error.append(0)
    two = determine_bit(two)
    if two != ham[2]:
        error.append(1) 
        print("You have an error in column 3 or 4.")
        matrix_pretty_print("  xx  xx  xx  xx") 
    else:
        print("There are no errors in column 3 or 4.")
        error.append(0)
    four = determine_bit(four)
    if four != ham[4]:
        error.append(1)
        print("You have an error in row 2 or 4.")
        matrix_pretty_print("    xxxx    xxxx") 
    else:
        print("There are no errors in row 2 or 4")
        error.append(0) 
    eight = determine_bit(eight)
    if eight != ham[8]:
        error.append(1)
        print("You have an error in row 3 or 4.")
        matrix_pretty_print("        xxxxxxxx") 
    else:
        print("There are no errors in row 3 or 4") 
        error.append(0) 
    
    error_bit = determine_error_bit(error)
    error_pos = 0
    if error_bit != -1:
        error_pos = int(error_bit, 2)
        print(f"Your error is at position {error_pos}.")
    
    corrected_message = ""
    for i in range(len(ham)):
        if i != error_pos:
            corrected_message += ham[i]
        else:
            if int(ham[error_pos])%2 == 0: 
                corrected_message += "1"
            else:
                corrected_message += "0"

    if corrected_message[0] != ham[0]:
        print("You may have an additional error")
        print("Message")
        matrix_pretty_print(ham)
    else:
        print("Corrected Message")
        matrix_pretty_print(corrected_message)

def matrix_pretty_print(ham):
    if((len(ham)%4) != 0):
        print("Ham messages should be divisible by 4 for printing")
    bar = "|"
    print(bar + bar.join(ham[0:4]) + bar)
    print(bar + bar.join(ham[4:8]) + bar)
    print(bar + bar.join(ham[8:12]) + bar)
    print(bar + bar.join(ham[12:16]) + bar)

def determine_bit(message_stub):
    sum = 0
    for bit in message_stub:
        sum += int(bit)
    if sum%2 == 0:
        parity = "0"
    else:
        parity = "1" 
    return parity

def determine_error_bit(error_array):
    value = ""
    for iter in error_array:
        value += str(iter)
    if value == "0000":
        return -1
    return value 
        
def main():
    parser = argparse.ArgumentParser(description="""
            This script encrypts an 11 bit message into a ham code 16 bit 
            message or decrypts a ham coded 16 bit message into a 11 bit 
            message.
            """)
    parser.add_argument("--h", metavar='ham', help="Convert a ham coded string back to its original message")
    parser.add_argument("--m", metavar='message', help="Create a ham coded string from a message")

    args=parser.parse_args()

    message = args.m
    ham = args.h
    
    if(ham):
        ham_to_message(ham)
    if(message):
        message_to_ham(message)

main()
