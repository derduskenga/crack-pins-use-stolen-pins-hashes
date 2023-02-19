# Simulate how hackers crack user PINs/password by using brute force and dictionary attacks 

In computer systems, user passwords aren't stored in the computer database in plain text. Instead of plain text, passwords are converted into a hash value by using a one-way hashing function. The hash function takes a variable-length input string and converts it into a fixed-length string. This function is called one-way as it's is designed to convert a password into a hash, but there's no way of or it's hard for a reverse process. 

A reason for hashing passwords is to prevent them from being read if the computer system is compromised by hackers. Even with this measure, hackers can still crack user passwords by using dictionary attack. 

In this mini-project, you'll write code to demonstrate how hackers crack user personal identification numbers (PINs) by using a stollen database of PINs hashes

## Dictionary attack example

A hacker gains access into a computer system and steals users' usernames and PIN hashes. This information can be represented in a table or a dictinary as shown below:

*Table*
|  username | hash  | 
|---|---|
| user1  | d6a9a...6e27a4a  |  
| user2  | d6a9a...0e23a4a  |   
| user3  | d6a9a...1e20a4a  | 
| ...  | ...  |

*Dictionary*

`{'user1':'d6a9a...6e27a4a', 'user2':'d6a9a...0e23a4a', 'user3':'d6a9a...1e20a4a'}`

The hacker knows that the users sign in into the system by using a username and a 6-digit PIN, so the hacker proceeds as follows: 

1. Generates all possible 6-digit PIN and their hashes
1. 

add table and dictinary here



## Starter code

## Your task

### Additional information 

## Test your code

## Hints

## Bonus Task

1. Possible number of PINs the hacker has to generate - permutations. 
2. How use of a cryptographic salt can stop the hacker from hacking user password.

## Resources 
