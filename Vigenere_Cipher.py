import math
import os
import random

def main():
    vigenere_cipher()
    inverse_function_with_key()

def vigenere_cipher():
    #This part converts the input to its respective number
    Input_list = []
    Cipher_list = []
    coded_list = []
    Cipher_Output = []
    blank_list = []
    #I want to remove all spacing
    converter_dictionary = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    reconverter_dictionary = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
    while True:
        try:
            plaintext = input('Enter the plaintext that you are going to use: ')
            plaintext = plaintext.lower()
            plaintext = ''.join(ch for ch in plaintext)
            if plaintext.isnumeric():
                raise ValueError
            break
        except ValueError:
            print('Invalid input. Please enter a valid input.')
    for i in plaintext:
        Input_list.append(converter_dictionary[i])
    print(Input_list)
    while True:
        try:
            cipher_key = input('Enter the key you wish to use: ')
            cipher_key = cipher_key.lower()
            if cipher_key.isnumeric():
                raise ValueError
            break
        except ValueError:
            print('Input is invalid, please enter another input: ')
    for letters in cipher_key:
        Cipher_list.append(converter_dictionary[letters])
    #Employ the euclidean algorithm here in working with the input list.
    """ So a = bq + r where q is the quotient an r is the remainder. So to code this, we need to have a string and cover two cases. One where len(input_list) < len(cipher list) and the second case is
    where len(input_list) >= len(cipher_list).
    For the first case, we can just add the values for i in range (0, t)and convert it. Trivial.
    The second case requires a bit of intuition."""

    #This is the length of the input value
    v_1 = len(Input_list)
    #this is the length of the cipher value
    v_2 = len(Cipher_list)
    """For the second case, I want to be able to loop the length so that v_1 > v_2, we know that by the Euclidean Algorithm, we can convert the values from v_1 = v_2 * q + r where r becomes our modular
    resultant."""
    if v_1 < v_2:
        for i in range(0, v_1):
            coded_list.append(Input_list[i] + Cipher_list[i])
    else:
        for j in range(0, v_1):
            if j < v_2:
                coded_list.append(Input_list[j] + Cipher_list[j])
            else:
                j_changed = j % v_2
                coded_list.append(Input_list[j] + Cipher_list[j_changed])
    #We now need to convert our values into ciphertext
    for i in coded_list:
        i = i % 26
        Cipher_Output.append(reconverter_dictionary[i])
    print(''.join(Cipher_Output))

def inverse_function_wo_cipher_key():
    #We need a counter for each elelemt that we can access. Should I make a list or should I focus on creating just blank element that store the values in it?
    a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = 0
    Empty_List = []
    cipher_text = input('Enter the text that you want to decipher: ')
    #We want to remove all spacing from the cipher text if possible. We know that if we remove the spacing from the cipher text, we then can analyze the count of how many elements there are.
    cipher_text = cipher_text.lower()
    for letter in cipher_text:
        Empty_List.append(letter)
    for inputs in Empty_List:
        if inputs is ' ':
            Empty_List.remove(' ')
        else:
            pass
    #once we remove the spaces, we want to add up the elements back together and then analyze how many of each elements there are.
    cipher_text = ''.join(Empty_List) #If an error occurs, it is probably from here.
    for letter in cipher_text:
        if letter == 'a':
            a += 1
        elif letter == 'b':
            b += 1
        elif letter == 'c':
            c += 1
        elif letter == 'd':
            d += 1
        elif letter== 'e':
            e += 1
        elif letter == 'f':
            f += 1
        elif letter == 'g':
            g += 1
        elif letter == 'h':
            h += 1
        elif letter == 'i':
            i += 1
        elif letter == 'j':
            j += 1
        elif letter == 'k':
            k += 1
        elif letter == 'l':
            l += 1
        elif letter == 'm':
            m += 1
        elif letter == 'n':
            n += 1
        elif letter == 'o':
            o += 1
        elif letter == 'p':
            p += 1
        elif letter == 'q':
            q += 1
        elif letter == 'r':
            r += 1
        elif letter == 's':
            s += 1
        elif letter == 't':
            t += 1
        elif letter == 'u':
            u += 1
        elif letter == 'v':
            v += 1
        elif letter == 'w':
            w += 1
        elif letter == 'x':
            x += 1
        elif letter == 'y':
            y += 1
        elif letter == 'z':
            z += 1
        else:
            pass
    values = ''.join(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
    print(values)
    #after running through the exception case we can now statistlically analyze the data
    # The question is do I want to make a dictionary of the code? Let's do it

def inverse_function_with_key():
    Empty_List = []
    cipher_key_list = []
    Decrypted = []
    cipher_text = input('Enter the text that you want to decipher: ')
    converter_dictionary = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    reconverter_dictionary = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
    #We want to remove all spacing from the cipher text if possible. We know that if we remove the spacing from the cipher text, we then can analyze the count of how many elements there are.
    cipher_text = cipher_text.lower()
    for letter in cipher_text:
        Empty_List.append(converter_dictionary[letter])
    for inputs in Empty_List:
        if inputs is ' ':
            Empty_List.remove(' ')
        else:
            pass
    given_cipher_key = input("Enter the given cipher key: ")
    given_cipher_key = given_cipher_key.lower()
    for char in given_cipher_key:
        cipher_key_list.append(converter_dictionary[char])
    #The math here is that we do c_i + k_i % 26. Then convert it back into the dictionary
    #First we need to compare the lengths first.
    print(Empty_List, cipher_key_list, Decrypted)
    v_1 = len(cipher_text)
    v_2 = len(given_cipher_key)
    if v_1 < v_2:
        for i in range(0, v_1):
            difference = Empty_List[i] - cipher_key_list[i]
            if difference >= 0:
                Decrypted.append(converter_dictionary[difference])
            else:
                Decrypted.append(converter_dictionary[difference+25])
    else:
        for i in range(0, v_1):
            if i < v_2:
                difference = Empty_List[i] - cipher_key_list[i]
                if difference >= 0:
                    Decrypted.append(reconverter_dictionary[difference])
                else:
                    Decrypted.append(reconverter_dictionary[difference+25])
#TODO Figure this out
#This is where there are a lot of error messages. Divide the string into chunks
            else:
                

main()
