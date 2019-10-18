#!/usr/bin/env python3
import sys

number = float(sys.argv[1]) ## By default, sys imports variables as strings

## here I'm setting some variables that can be evaluated to true using bool()
## this will help me later on to prevent printing redundant information to the terminal
## because I can change the value of the variable to 0 inside of a conditional evaluation

even_flag = 1
third_flag = 1

if number < 0: ## Begin logic by testing if a number is negative
    print('negative')
elif number > 0: ## Chances are, if the number isn't negative it will be positive. So I want to evaluate that possibility before moving on to a zero. 
    print('positive')
    if number < 50: ## test if the number is greater than 50
        if number %2 == 0:
            print('it is an even number that is smaller than 50')
            even_flag = 0 # mark that I've already tested if this number is even
        else:
            print('number < 50') ## I don't like to print redundant information, so only print this if the first condition isn't met
    elif number > 50: ## test if the number is greater than 50
        if number%3 == 0: ## test if the number is divisible by 3
            print('it is larger than 50 and divisible by 3')
            third_flag = 0 # mark that I've already tested if this number is divisible by three
        else:
            print('the number is > 50') ## I don't like to print redundant information, so only print this if the first condition isn't met
    else:
        print('number is 50') ## I just wanted to finish the logic around the number 50 before moving on

    ## These final if statements will only evaluate if I haven't previously tested these conditions earlier in the loop.
    ## Previousily initializing these as numbers that evaluate 'True' with bool() comes in handy allows this because they will only
    ## be set to 0 if the previous conditions were tested. 

    if bool(even_flag) and number%2 == 0: # test if the number is even  
         print('number is even')
    if bool(third_flag) and number%3 == 0: ## test if the number is divisible by 3 
            print('number is divisible by 3')
else:
    print('the number is zero') ## test if the number is zero        

print('The number supplied was:', number)
