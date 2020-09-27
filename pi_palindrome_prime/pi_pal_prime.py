################################################################################
# File:	        pi_pal_prime.py
# Author: 		Dan Gerstl
# Email:		drgerstl@gmail.com
# Date:			09/25/2020
# Purpose:	    Accepts a text file which is expected to contain the digits of 
#               pi. It then finds the first 7 digit, prime, palindromic number
#               and prints the number with a success message. If no number was 
#               found it prints an error message instead. pi.txt is expected to
#               be in the same directory as this file.
################################################################################

####
# Reads in pi from a text file and searches through it for the first 
# 7 digit, prime, palindromic number and prints the number if found. Else it
# prints an error.
####

def main():
    
    # Local Variables
    right = 7
    test_string = "" 
    test_num = 0
    goal = 0

    # Read in text file containing the first million digits of pi
    file = open("pi.txt", "r")
    pi = file.read()

    # Step though pi and test each 7 digit interval
    for char in range(7, len(pi)):
        
        # Slice 7 character string
        test_string = pi[right - 7: right]
        right += 1

        if is_palindrome(test_string):
            test_num = int(test_string)
            
            if is_prime(test_num):
                goal = test_num
                break
        
    # Check to ensure a valid number was found
    if goal > 0:
        print(f"The first 7 digit, prime, palindromic number in pi is: {goal}")
    else:
        print("Error: Number matching desired specifications not found.")

    return

####
# Accepts a string as an input and returns a boolean value indicating whether
# or not the provided string is a palindrome
####

def is_palindrome(string):

    # Local Variables
    left = 0
    right = len(string) - 1
    palindrome = False

    # Check each character starting at the ends and moving to the middle
    while right - left > 0:
        if string[left] == string[right]:
            left += 1
            right -= 1            
        else: # Characters dont match 
            return palindrome

    # String is a pallindrome
    palindrome = True

    return palindrome

####
# Accepts an integer value and returns a boolean indicating whether or not the
# provided number is a prime number
####

def is_prime(number):

    # Local Variables
    prime = True
    i = 5
    step = 6

    # Check for 1-3 and basic division elimination
    if number <= 3:
        return prime
    elif number % 2 == 0 or number % 3 == 0:
        prime = False
        return prime

    # Check other possibilites by trial division
    while (i * i) <= number:
        if (number % i == 0) or (number % (i + 2) == 0):
            prime = False
            return prime
        i = i + step

    return prime

# Main
if __name__ == "__main__":
    main()