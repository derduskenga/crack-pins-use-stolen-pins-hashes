from data import PinDigits, usernamePasswordHashDictionary, pinLength
from pin import Pin

pin = Pin(PinDigits, usernamePasswordHashDictionary, pinLength)

usernamePINDictionary = pin.computeUsernamePINDictionary()

print(usernamePINDictionary)

