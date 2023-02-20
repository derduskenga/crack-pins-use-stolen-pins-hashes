# Simulate how hackers crack user PINs/password by using brute force and dictionary attacks 

In computer systems, user passwords aren't stored in the computer database in plain text. Instead, passwords are hashed by using a one-way hashing algorithm. The hash function takes a variable-length input string and converts it into a fixed-length string. This function is called one-way as it's designed to convert a password into a hash, but there's no way or it's hard for a reverse process. 

A reason for hashing passwords is to prevent hackers from reading the information if they compromise the computer system. Even with hashing, hackers can still crack user passwords by using a combination of dictionary and brute force attack. 

In this mini-project, you write code to demonstrate how hackers crack user personal identification numbers (PINs) by using a stolen database of PINs hashes.

## Dictionary and brute force attack example

A hacker gains access into a computer system and steals a database of users' usernames and PIN hashes. We can represent this information by using a table or a dictionary as shown below:

*Table*
|  username | hash  | 
|---|---|
| user1  | d6a9a...6e27a4a  |  
| user2  | d6a9a...0e23a4a  |   
| user3  | d6a9a...1e20a4a  | 
| ...  | ...  |

*Dictionary*

`{'user1':'d6a9a...6e27a4a', 'user2':'d6a9a...0e23a4a', 'user3':'d6a9a...1e20a4a', ...}`

The hacker knows that the users sign in into the system by using a username and a six-digit PIN, and that the hashing algorithm used is md5, so the hacker proceeds as follows: 

1. Generates all possible six-digit PINs and their hashes, called a *dictionary*. It looks similar to the following dictionary, where the `key` is the six-digit PIN, and the `value` is the PINs hash: 
  
    `{..., '012345':'d6a...d4a', '012649':'551...b5d', '014532':'693...0e8', ...}`
  
1. For each PIN hash in the stolen hashes, the hacker searches for its corresponding plain text PIN in the generated six-digit PINs and hashes dictionary. For each match, store the user's username and PIN in a new dictionary similar to the one shown below:

   `{..., 'user1': '012345', 'user100': '012649', 'user486': '014532',...}`


## Starter code

1. `data.py` file contains the information you need to crack users PINs: 
    
    1. `usernamePasswordHashDictionary` represents a dictionary of username and PIN hash values
    
    1. `PinDigits` represents is a list of all the possible digits users use to create their PINs
    
    1. `PinDigits` is the length of the PIN users must use in the system

1. `pin.py` file contains a class, whose constructor assigns values for `PinDigits`, `usernamePasswordHashDictionary` and `pinLength`. It also contains a method `computeUsernamePINDictionary`, which you need to implement. 

1. `main.py` files print the return value from `computeUsernamePINDictionary` method. You don't need to change any line of code in this file. Just run this file once you implement the `computeUsernamePINDictionary` method. 

### Your task

Your task is to implement the `computeUsernamePINDictionary` method. At the moment, it has a declared empty dictionary, `usernamePasswordDictionary`, which you need to add elements into, and then return it.  

For example: 

|  Value of `usernamePasswordHashDictionary` | Expected output  | 
|---|---|
| `{}`  | `{}`  |  
| `{"user1": "d6a9a933c8aafc51e55ac0662b6e4d4a","user2": "b26230fafbc4b147ac48217291727c98", "user3": "a6398c2be6b2c5046b0025eefd8e4c2a","user4": "cbcfbad7e9761f71b9b5139185d058f1"}`  | `{'user4': '012348', 'user1': '012345', 'user2': '012346', 'user3': '012347'}`  |   
| `{'user45':'0dd334f240187c5c733b93684467e746'}`  | `{'user45': '999890'}`  | 

### Important information

- The hashing algorithm is md5.

- The length of all PINs is six digits.

- The PIN can consist of repeating digits such as, 000000 or 000111 or 889881

## Test your code

The starter code provides unit test for your `computeUsernamePINDictionary` method. This test is in the `test-pin.py` file. Once you complete writing the code for your method, run the file to check that your function implementation returns the expected values.  

## Hints

- You can use helper methods, which you can then call from the `computeUsernamePINDictionary` method.  

- You can generate all possible PIN combinations by using the `product` method in the `itertools` module.

- The implementation of the md5 hashing algorithm is available in the `hashlib` module. 

## Bonus Task

1. Calculate the total number of possible PIN combinations you can generate from the above example. Show how you arrive at your answer working: 

      >**Total number of possible PIN combinations =  Number of digit options <sup> Length on PIN </sup>.      
      >Total number of possible PIN combinations = 10 <sup> 6 </sup>.      
      >Total number of possible PIN combinations = 1000000.**

1. Explain how the introduction of a cryptographic salt during hashing can stop the hacker from hacking user PINs. 

     >**A random string, known as a cryptographic salt, is added to the PIN before it's hashed, so even when a hash in the stolen hash matches a hash in the precomputed dictionary, the plain text PIN won't be correct.**

## Resources 

- https://docs.python.org/3/library/hashlib.html 

- https://docs.python.org/3/library/itertools.html
