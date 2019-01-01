import math
import sys
import random
"""
Implementation of the ElGamal Cryptosystem
I'm not using classes... One day I will fix this to impliment classes
For the sake of laziness I'm just gonna use the 10kth prime, and a random modulo.
By the way, this is really lazy on my part :D
I'm going to encrypt each element and print it to the console. There's a better way to do it, but it's like 2am here in NYC so...
For decryption, I'm gonna decrypt each element and print it to the console, then combine that string into the console.
The random element is going to be from the range of 1 to my trusted prime (BAD I KNOW. I'll FIX IT LATER)
Can I make this less than 100 lines?
@TODO I'll fix it later btw.
"""
trusted_prime = 104729
trusted_modulo = 3

#Alice needs to enter the secret value here.
#This run time should be around O(n^2) Worst case. Srsly....
def Elgamel_Pub(trusted_prime, trusted_modulo):
    Alice = 0
    while True:
        try:
            Alice = int(input("Alice enters a secret key a: "))
            break
        except ValueError:
            print("Try again.")
    while Alice <= 0 or Alice > trusted_prime:
        Alice = int(input("Alice needs to enter a secret key a: "))

    Alice_new = Alice**trusted_modulo % trusted_prime
    Bob = 0
    Bob_string = input("Bob: Enter a string: ")
    Bob_Converted_List = [ord(c) for c in Bob_string]
    #Create the random element now
    random_element = random.randint(1, trusted_prime)
    c_1 = trusted_modulo**random_element % trusted_prime
    c_2_list = list()
    for m in Bob_Converted_List:
        c_2_list.append(m*Alice_new**random_element % trusted_prime)

    print(c_1, c_2_list)

Elgamel_Pub(trusted_prime, trusted_modulo)

true_prime=None
true_modulo=None

def prime_maker(true_prime):
    for a in range(a, num):
        if a % num == 0:
            print('not prime')
            break
        else: # loop not exited via break
    print('prime')

