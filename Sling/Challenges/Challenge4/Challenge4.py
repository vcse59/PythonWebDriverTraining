from Fibonacci import Fibonacci
import argparse
from Constant import *
from CGenerateNumberString import *

''' This function contorl Parsing command line parameters '''
def get_command_line_arguments():
    parser = argparse.ArgumentParser(description='Fibonacci nth order')
    parser.add_argument("fibonacciOrder", help="nth order of Fibonacci sequence")
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    generateNumberStringObj =   CGenerateNumberString()
    args = get_command_line_arguments()
    fibonacciNthnumber  =   Fibonacci(int(args.fibonacciOrder))

    if fibonacciNthnumber == -1:
        print("Error : Incorrect input")
    else:
        print("%s order of fibonacci sequence is %s" %(args.fibonacciOrder, fibonacciNthnumber))
        numberString = BLANK_CHARACTER
        if fibonacciNthnumber == 0:
            numberString = ZERO_STRING
        else:
            numberString = generateNumberStringObj.convertNumberToString(fibonacciNthnumber)
        print("String representation of %s is %s" %(fibonacciNthnumber, numberString))
