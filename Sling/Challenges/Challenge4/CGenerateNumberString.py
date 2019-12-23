from Constant import *

class CGenerateNumberString:

    def convertNumberToString(self, pNumber):
        '''
        This function converts large numbers to string
        :param pNumber: fibonacci number
        :return: String
        '''
        DigitLength = len(str(pNumber))

        numberString = BLANK_CHARACTER

        counter = DigitLength
        tempNumber = str(pNumber)

        while counter > 2:

            digitIndex = (DigitLength - counter)
            tempNumber = str(pNumber)[digitIndex:]
            numberPlaces = int(int(tempNumber) / gNumberPlaces[counter - 1])

            if numberPlaces == 0:
                numberString += BLANK_CHARACTER
            else:
                numberString += self.convertNumberToString(numberPlaces) + ONE_SPACE_CHARACTER + gNumberPlacesString[
                    counter - 1]

            numberString += ONE_SPACE_CHARACTER
            counter = counter - len(str(numberPlaces))

        twoDigitnumber = int(tempNumber[-2:])
        numberString += self._converttwodigitNumberToString(twoDigitnumber)

        return numberString

    def _converttwodigitNumberToString(self, pTwoDigitNumber):
        '''
        This function convert two digit number to string
        :param twoDigitnumber: Integer
        :return: String
        '''
        if int(pTwoDigitNumber) > 19:
            tenthPlace = int(str(pTwoDigitNumber)[0])
            onesPlace = int(str(pTwoDigitNumber)[1])
            numberString = gTenthStringList[tenthPlace] + ONE_SPACE_CHARACTER + gNumberStringList[onesPlace - 1]
        else:
            numberString = gNumberStringList[int(pTwoDigitNumber) - 1]
        return numberString
