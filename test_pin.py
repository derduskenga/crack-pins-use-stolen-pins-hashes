import unittest
from pin import Pin

class TestPin (unittest.TestCase):
     def testComputeUsernamePINDictionary(self):
        pin = Pin([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], {
        "user1": "d6a9a933c8aafc51e55ac0662b6e4d4a",
        "user2": "b26230fafbc4b147ac48217291727c98",
        "user3": "a6398c2be6b2c5046b0025eefd8e4c2a",
        "user4": "cbcfbad7e9761f71b9b5139185d058f1"}, 6)

        #For a hash with repeat digits
        pin = Pin([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], {'user45':'0dd334f240187c5c733b93684467e746'}, 6)
        self.assertEqual(pin.computeUsernamePINDictionary(),{'user45': '999890'})


        self.assertEqual(pin.computeUsernamePINDictionary(),{'user4': '012348', 'user1': '012345', 'user2': '012346', 'user3': '012347'})

        # For empty username password hash dictionary 
        pin = Pin([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], {}, 6)
        self.assertEqual(pin.computeUsernamePINDictionary(),{})

if __name__ == '__main__':
    unittest.main()