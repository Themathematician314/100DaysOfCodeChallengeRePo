import math
import random
import os
import hashlib as h
import matplotlib as mpl
import datetime
import sys

#This is just a sample of how card encryption works. DO NOT ACTUALLY USE THIS FOR REAL LIFE ENCRYPTION! THIS IS JUST AN EXAMPLE OF ME USING RSA ENCRYPTION ON A CREDIT CARD

class Card:

    def __init__(self, card_number, date, security_value):
        self.card_number = card_number
        self.date = date
        self.security_value = security_value

    def get_card_info(self):
        return self.card_number
        return self.date
        return self.security_value

#RSA Encryption here below.
"""
def encrypt():

    #We need to input a card
    #Sample Card (The card isn't real)
    #1357 9024 6812 3456

    card_Creation()
    encryption(encryption_exponent_choice, N)
"""
#Create a card
def card_Creation():
    Card_Test = True
    CCV_Test = True
    Date_Test = True
    while Card_Test == True:
        try:
            card_number = int(input("Enter your card information please: "))
        except ValueError:
            print("You must try again: ")
        while card_number.isnumeric() == False or len(card_number) != 16:
            card_number = int(input("Enter your card information. You failed!: "))
            if len(card_number) == 16:
                return card_number
                Card_Test = False
    
    while CCV_Test == True:
        try:
            #Length must be 3!
            CCV_value = int(input("Enter your CCV. The length must be 3: "))
        except ValueError:
            print("You must try again: ")
        while CCV_value.isnumeric() == False or len(CCV_Value) != 3:
            CCV_value = int(input("Enter the CCV Value of your card. You failed: "))
            if len(CCV_value) == 3:
                return CCV_value
                CCV_Test = False

    #The format of the card should be yyyymm combined as a string after the values are input. 
    while Date_Test == True:
        #Enter the year
        try:
            year = int(input("Enter the year of expiration for your card: "))
        #check for three things, whether the input is correct, whether the input is expired or whether the length of the input is greater than 4.
        except ValueError:
            print("You need to enter the year! You failed. ")
        while year.isnumeric() == True or len(year) != 4:
            print("Enter the year correctly! ")
            while year <= datetime.datetime.year():
                print("Enter the date. Your card is expired: ")
        
def card_creation_2()
    #length of the card MUST BE 16 digits
    card_number = str(input("Enter your card information please: "))
    for i in card_number:
        while i != '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0':
            card_number = str(input("Enter your card info again, make sure they are all numbers: "))
        while len(card_number) != 16:
            card_number = str(input("Enter your card info again, make sure the string is len 16:"))
    return card_number
    #Enter the date Format must be military
    date = str(input("Enter your date in the following format: yyyymmdd: "))
    for i in date:
        while i != '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0':
            date = str(input("Enter the expiration date of your card. Make sure that you do not place any non numerical character: "))
        while len(date) != 8:
            card_number = str(input("Enter the expiration date of your card. Make sure that the length is 8: "))
    security_value = str(input("Enter the security code of your card: "))
    for element in security_value:
        while element != '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0':
            security_value = int(input("Enter the security code of your card, ensure that you do not have any nonnumerical character: "))
        while len(security_value) != 3:
            security_value = int(input("Enter the security code of your card, ensure that the length is exactly 3: "))
    Card_Stored = Card(card_number, date, security_value)
    Card_Stored.get_card_info()

def key_generation():

    #Find two prime numbers, and I would prefer if the two numbers were strictly greater than 10^16 but less than 10^20. I don't want my laptop to overheat.
    #I will try to optimize this so that it can run in Q  = O(ln(n)n) time. Clearly the most effective is O(n) time. That's a pipedream though. So to reach Q time would be fine by me
    p_count = 0
    q_count = 0
    prime_p_run = True
    while prime_p_run == True:
        try:
            p = int(input("Enter the first prime number p: "))
            break
        except ValueError:
            print("Try again!")
        for i in range(2, p):
            if p % i == 0:
                p_count += 1
            else:
                pass
        if p_count > 0:
            p = int(input("Enter the first prime number p again: "))
            p_count = 0
    #OK it's prime, but we now want to check if it's less than 10^16
        else:
            while p < 10^16 or p > 10^20:
                p =  int(input("Enter the first prime number again  please. This time ensure that it's greater than 10^16 but less than 10^20: "))
        prime_p_run == False
    prime_q_run = True
    while prime_q_run == True:
        try:
            q = int(input("Enter the second prime number q: "))
        except ValueError:
            print("Try again!")
        for i in range(2, q):
            if q % i == 0:
                q_count += 1
            else:
                pass
        if q_count > 0 :
            q = int(input("ENter the second prime number q again please: "))
            q_count = 0
        else:
            prime_q_run == False
            return q

    #We need to now construct the secret key value that encrypts the information
    #We shall produce the encryption exponent at random
    possible_encryption_exponent = list()
    N = int((p-1)*(q-1))
    for i in range(2, N):
        if math.gcd(i, N) == 0:
            pass
        else:
            possible_encryption_exponent.append(int(i))
    encrpytion_exponent_choice = random.randint(1, len(possible_encryption_exponent))
    return possible_encryption_exponent[int(encrpytion_exponent_choice)]
    #Return the two possible values
    print(encrpytion_exponent_choice, N)
    return(encrpytion_exponent_choice, N)

def encryption(encryption_choice_exponent, N):
    #Input the card data. Find values s.t. len of the integers is 16. Assuming converting our inputs to strings and integers are free of course.
    key_generation()    

def Mil_rab_Test():
    pass
    
"""
Encryption method:

m*(value^e) mod(N) where gcd(value, N) = 1
m = card_value*date*ccv % floor(cube_root(N))
Then convert that string to hexadecimal

Alright here's the encrption trick. We will proceed with a demonstration encryption below then do the actual

def encryption_sample(encrpytion_exponent_choice, N):
    placeholder = True
    while placeholder == True:
        try:
            plain_integers = int(input("Enter a string of numbers: "))            
        except ValueError:
            print("You didn't follow instructions: ")
        if plain_integers.isnumeric() == True:
            placeholder == False
    cipher_integers = plain_integers**encryption_exponent_choice
    
    """
card_Creation()
