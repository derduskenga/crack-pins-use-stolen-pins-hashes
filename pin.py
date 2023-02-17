# import modules here if needed
class Pin:
    def __init__(self, PinDigits, usernamePasswordHashDictionary, pinLength):
        self.PinDigits = PinDigits
        self.usernamePasswordHashDictionary = usernamePasswordHashDictionary
        self.pinLength = pinLength

    def computeUsernamePINDictionary(self):
        #Add elements to this dictionary and then return it. 
        usernamePasswordDictionary = {}
  