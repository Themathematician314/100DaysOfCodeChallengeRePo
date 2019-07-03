import math
import random
import hashlib

"""So here's how the encryption works. Let's choose two prime numbers p and q and select an encryption exponent e such that gcd((p-1)(q-1), e) = 1.
Notice that we publish N = pq and e. 
Bob wants to send a message m to Alice. So he encrypts it by using c = m^e % mod(N)
Bob will send that message. We did this part/. (Update 6/29)

#TODO (We want to now learn how to decrypt hexadecimal values and use this)
Alice will recieve c = m^e $mod(N). Alice solves the equation e*d = 1 % mod(N). By using c^d, Alice gets back the message m. So we want to decrypt the function. (We are still working on this 7/1/2019)
"""

class RSA_Key:

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def get_key(self, p, q):
        return p*q
    
#This is the portion to find out whether our key value works.
def prime_checker_p():
    prime_check = 0
    Need_an_integer = True
    Need_a_Prime = True
    while Need_an_integer == True and Need_a_Prime == True:
        #This part fixes input errors 
        #TODO improve on this along with prime value q. Task for the morning.
        try:
            p = int(input("Enter a prime number This is your first prime number: "))
            break
        except ValueError:
            print("Your value doesn't work! ")
            break
        if p.isnumeric() == True:
            Need_an_integer == False
    if Need_a_Prime == True:
        for i in range(3, math.floor(math.ceil(p))):
            if p % i == 0:
                    prime_check += 1
            else:
                break
        while prime_check >= 1:
            print("Your input isn't prime! ")
        #find a way to reloop back to p
    else:
        print("The value is prime!")
        return p
        return True

def prime_checker_q():
    prime_check = 0
    #TODO improve on this along with prime value q
    #I want to ensure that if I enter a prime value then I'm fine, if I enter a non integer value then the program should not continue
    while True:
        try:
            q = int(input("Enter a prime number. This is your second prime number: "))
            break
        except ValueError:
            print("Your value doesn't work! ")
            break
    for i in range(3, math.floor(math.ceil(q))):
        if q % i == 0:
            prime_check += 1
        else:
            break
    if prime_check >= 1:
        print("Your input isn't prime! ")
    else:
        print("The value is prime!")
        return q
        return True

#This is how I want to convert the message into integers.
def message_convert(N, value):

    Bobs_message = input("Enter anything: ")
    #So lets encrypt Bob's message this way, each element becomes encrypted first.
    #Take any element and convert it to ACSII
    to_encrypt = [ord(x) for x in Bobs_message]
    encrypted_message = []
    reencrypted_message = []
    for unencrypted in to_encrypt:
        encrypted_message.append(unencrypted**value % N)
    #Raise ASCII value to the unencrypted 
    for element in encrypted_message:
        print(element)
    for element in encrypted_message:
        reencrypted_message.append(hex(element))
    for element in reencrypted_message:
        print(element)
    print(''.join(reencrypted_message))

def prime_modulus(p, q):
    space_of_possible_values = []
    for element in range(3, (p-1)*(q-1)):
        if math.gcd(element, (p-1)*(q-1)) == 1:
            space_of_possible_values.append(element)
        else:
            pass
    return space_of_possible_values

def encrpytion():
    #The results will be different here
    p = prime_checker_p()
    q = prime_checker_q()
    key = RSA_Key(p, q).get_key(p, q)
    modulus_space = prime_modulus(p,q)
    mod_choice = modulus_space[random.randint(0,len(modulus_space))]
    print(mod_choice)
    message_convert(key, mod_choice)
    return mod_choice

    #EG Code using 313 and 131 as p and q respectively with different prime modulus. Plaintext is ?????
    #T1 using 21217 and result is 0x21740x891d0x2cd60x2cd60x2d65 / 2174891d2cd62cd602d65
    #T2 using 11473 and result is 0x8e000x60420x5ba00x5ba00x1767

"""
    29389
Enter anything:
0x3b17 0x82ee 0x6073 0x6073 0x3b17
0x7b3d 0x85e9 0x547e 0x547e 0xa024
0x5d18 0x4381 0x4f66 0x4f66 0x4165
0x735f 0x9ffe 0x16d4 0x16d4 0x2831
0x4240 0x88cb 0x5a4a 0x5a4a 0x7a77

Notice that there are a ton of 0xs in this code. So, we can divide each of these strings in 0x _ _ _ _
Another key notice is that (if we didn't know our cipher text) that the last two pieces of the cipher text are the same.
The length of each bit is six. so we know we have a 5 element word with r' representing repeating elements.

_ _ r' r' _ <------ r' is not the letter itself. r' represents repeating letters and _ represents unknown patterns.
"""
# I believe I can find a decryption algorithm here. Let's create it assuming we know the prime modulus. So Alice knows the prime modulus, knows the RSA Key and knows the 
# exponent used. Then tis is quite obvious to code. This is for Alice ONLY!

"""The fact that I have to go through so many tiny steps just to create this shitty encryption. It's a joke. """
#TODO Fix this because this isn't working for me.   
def Alice_Decrypt(mod_choice, p, q):
    invertion_value = 0
    for i in range(3, (p-1)*(q-1)):
        if (i*mod_choice) % ((p-1)*(q-1)) == 1:
            #From Fermat's Little Theorem, we know that if gcd(c, p-1*q-1) = 1, then for every e in [1, N] \exists d \in [1, N] s.t. e*d = 1 mod(p-1*q-1)
            invertion_value = i
        else:
            pass
    #Let's get the length of our N value
    N = p*q
    key_length = len(str(N))+1
    print(key_length)
    ciphertext = input("Enter the ciphertext: ")
    ciphertext_bytes = []
    ciphertext_chunks = []
    cipher_chunks_final = []
    for i in ciphertext:
        ciphertext_bytes.append(i)
    cipher_len = len(ciphertext_bytes)
    for index in range(cipher_len+1):
        if index % key_length == 0:
            ciphertext_chunks.append(ciphertext_bytes[index-key_length:index])
    for list_element in ciphertext_chunks:
        cipher_chunks_final.append(''.join(list_element))
    #remove the first element
    cipher_chunks_final.remove(cipher_chunks_final[0])
    print(cipher_chunks_final)
    pseudo_decoded = []
    pseudo_decoded_2 = []
    for element in cipher_chunks_final:
        pseudo_decoded.append(element)
    for cipher_letter in pseudo_decoded:
        #UTF-8 Gives me Korean Characters
        cipher_text = str(cipher_letter)
        new_cipher_text = int(cipher_text, 16)
        pseudo_decoded_2.append(new_cipher_text)
    print(pseudo_decoded_2)
    print("The inversion value for ", mod_choice, "is", invertion_value)
    final_decrypted = []
    for number in pseudo_decoded_2:
        to_decode_value = number**invertion_value % N
        print(to_decode_value)
        decoded_element = chr(to_decode_value)
        final_decrypted.append(decoded_element)
    print(final_decrypted)

#TODO Create Eve's portion of this code. There's three parts to this approach. The first approach requires a bit of intuition. There is a multi-step process in trying to decrypt this!
#1. If we know N and our exponent value e, then we are daijyobu. So we take cipher**d (as e*d == 1 mod(p-1*q-1)).
#2. If we ONLY know N, then we can construct a space of e, then use the following trick:
#a. Statistically speaking, most passwords use a,e,i,o,u and 1,2,3,4,5,6,7,8,9,0 (Unless they are REALLY SMART and just use !@#$%^&*() for their passwords)
#So we can break their encryption by then raising each element to the required modulus and finding a match. (By the way this is highly inefficient so fuck that I wouldn't do that.)
#I can write the code for this but I REALLY don't recommmend doing this. This is useful for encryption purposes but it's for fun. #forfunplayer

def eve_attempt_1(N, exponent):
    #So EVE only knows about the encryption value and the exponent. Eve knowing about N doesn't necessarily mean that she knows p, q. But Eve can deduce p and q through two tricks.
    #If p and q are not too big, then we can get ceil(sqrt(N)) and get all the factors this way. So we have two numbers typically, and so the first one is p and the second value is q
    #The other trick is that if we know N, and we know our exponent, we can use the Pollard's p-1 method, with the magical property that we magically find a number L such that p-1 | L but q-1 doesn't.
    #
    ciphertext = input("Enter the ciphertext: ")
    prime_factors_of_N = []
    for i in range(math.ceil(math.sqrt(N))):
        if N % i == 0:
            prime_factors_of_N.append(i)
            print(i)
        else:
            pass
    #We can now access p and q, so we can get p-1 and q-1. Let's define elements here. So the first element is p, and the second one is q.
    p = prime_factors_of_N[0]
    q = prime_factors_of_N[1]
    #We know the encryption exponent, so it suffices to just find the inverse of the ciphertext.
    for inverse_target in range(p-1*q-1):
        if exponent*inverse_target == 0 % p-1*q-1:
            print(inverse_target)
        else:
            pass
    #We know the value, we convert our ciphertext from hex to ascii to integers, then invert and convert those values back to letters and we are good.
    #This is the easy case. Procrastinate on this!

if __name__ == "__main__":
    Alice_Decrypt(21217, 313, 131)
   
