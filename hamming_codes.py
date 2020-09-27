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
    matrix_pretty_print(ham)

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
    if sum %2 == 0:
        parity = "0"
    else:
        parity = "1" 
    return parity

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
