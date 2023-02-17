import itertools
import hashlib

class Pin:
    def __init__(self, PinDigits, usernamePasswordHashDictionary, pinLength):
        self.PinDigits = PinDigits
        self.usernamePasswordHashDictionary = usernamePasswordHashDictionary
        self.pinLength = pinLength
    
    def computePINPermutationsStringList(self):
        PINPermutationsStrList = []
        if len(self.usernamePasswordHashDictionary) == 0:
            return  PINPermutationsStrList 
        #Get a list of tuples, each tuple elements represents each possible PIN Permutation
        PINPermutations = list(itertools.product(self.PinDigits, repeat=self.pinLength))

        #Convert list of tuples into a list of PIN strings
       
        for PINPermutation in PINPermutations:
            PINPermutationStr = ""
            for digit in PINPermutation:
                PINPermutationStr = PINPermutationStr + str(digit)
            PINPermutationsStrList.append(PINPermutationStr)
        return PINPermutationsStrList

    def computeUsernamePINDictionary(self):
        ## Get matching pins from usernamePasswordHashDictionary, and store it into usernamePasswordDictionary
        #For each PIN in PINPermutationStrList, convert it into
        usernamePasswordDictionary = {}
        for pin in self.computePINPermutationsStringList():
            for key, value in self.usernamePasswordHashDictionary.items():
                #if a value in the usernamePasswordHashDictionary matches a has value in generated possible pins
                if value == hashlib.md5(pin.encode()).hexdigest():
                    #add the username (key) and pin into usernamePasswordDictionary
                    usernamePasswordDictionary[key] = pin
        return usernamePasswordDictionary
