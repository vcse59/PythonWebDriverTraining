from Fibonacci import Fibonacci
import argparse

ZERO_STRING         =   'zero'
BLANK_CHARACTER     =   ''
ONE_SPACE_CHARACTER =   ' '

gNumberStringList   =   ['one', 'two', 'three', 'four', 'five',
                         'six', 'seven', 'eight', 'nine', 'ten',
                         'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                         'sixteen', 'seventeen', 'eighteen', 'nineteen']

gTenthStringList    =   [BLANK_CHARACTER, BLANK_CHARACTER, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
                         'eighty', 'ninety']
gNumberPlaces       =   [1, 1, 100, 1000, 1000, 1000, 1000000, 1000000, 1000000,
                         1000000000, 1000000000, 1000000000,
                         1000000000000, 1000000000000, 1000000000000]
gNumberPlacesString =   ['', '', 'hundred', 'thousand', 'thousand', 'thousand', 'million', 'million',
                         'million', 'billion', 'billion', 'billion', 'trillion', 'trillion', 'trillion']

''' This function contorl Parsing command line parameters '''
def get_command_line_arguments():
    parser = argparse.ArgumentParser(description='Fibonacci nth order')
    parser.add_argument("fibonacciOrder", help="nth order of Fibonacci sequence")
    args = parser.parse_args()
    return args

def convertNumberToString(fibonacciNumber):
    '''
    This function converts large numbers to string
    :param fibonacciNumber: fibonacci number
    :return: String
    '''
    DigitLength = len(str(fibonacciNumber))

    numberString = BLANK_CHARACTER

    counter = DigitLength
    tempNumber = str(fibonacciNumber)

    while counter > 2:

        digitIndex = (DigitLength - counter)
        tempNumber = str(fibonacciNumber)[digitIndex:]
        numberPlaces = int(int(tempNumber) / gNumberPlaces[counter - 1])

        if numberPlaces == 0:
            numberString += BLANK_CHARACTER
        else:
            numberString += convertNumberToString(numberPlaces) + ONE_SPACE_CHARACTER + gNumberPlacesString[counter - 1]

        numberString += ONE_SPACE_CHARACTER
        counter = counter - len(str(numberPlaces))

    twoDigitnumber = int(tempNumber[-2:])
    numberString += converttwodigitNumberToString(twoDigitnumber)

    return numberString

def converttwodigitNumberToString(twoDigitnumber):
    '''
    This function convert two digit number to string
    :param twoDigitnumber: Integer
    :return: String
    '''
    if int(twoDigitnumber) > 19:
        tenthPlace = int(str(twoDigitnumber)[0])
        onesPlace = int(str(twoDigitnumber)[1])
        numberString = gTenthStringList[tenthPlace] + ONE_SPACE_CHARACTER + gNumberStringList[onesPlace - 1]
    else:
        numberString = gNumberStringList[int(twoDigitnumber) - 1]
    return numberString

if __name__ == '__main__':

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
            numberString = convertNumberToString(fibonacciNthnumber)
        print("String representation of %s is %s" %(fibonacciNthnumber, numberString))
