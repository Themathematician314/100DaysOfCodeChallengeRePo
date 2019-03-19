import math
import random
from random import randint
import matplotlib as mpl
import numpy as np
from decimal import *

class Coin:

#the __init__method here
    def __init__(self):
        self.__sideup = "Heads"

    """The toss method generates a r.n. in the range of 0 to 1. If 0, H; else 1 = T"""
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
#The get_sideup method returns the value referenced by side_up

    def get_sideup(self):
        return self.__sideup

class Dice:

    def __init__(self):
        self.sideup = "1"
        self.value = 1

    def toss(self):
        q = random.randint(1, 6)
        if q == 1:
            return self.sideup == '1'
            return self.value == 1
        elif q == 2:
            return self.sideup == '2'
            return self.value == 2
        elif q == 3:
            return self.sideup == '3'
            return self.value == 3
        elif q == 4:
            return self.sideup == "4"
            return self.value == 4
        elif q == 5:
            return self.sideup == "5"
            return self.value == 5
        else:
            return self.sideup == "6"
            return self.value == 6

    def get_info(self):
        return self.sideup
        return self.value   

#Notice this tends to one. Lim k -> inf = 1

def main():

    TestCoin = Coin()

    for i in range(5):
        #Let's flip a coin around a trillion times and collect the number of heads and tails
        TestCoin.toss()
        print("The side up is", TestCoin.get_sideup())
    
#OK this shit works
def coin_flip():

    Coin_Test = Coin()
    Total_Heads_T = []
    Total_Tails_T = []
    total_head = 0
    total_tail = 0
    #I want to impliment this experiment however many times. 
    for i in range(0, 50):
        total_head = 0
        total_tail = 0
        #In each of those five experiments I want to flip the coin 1,000 times, then after the end of the experiment send the result to Total_Heads_t and Total_Toals_T
        for j in range(10000):
#Toss the coin here.
            Coin_Test.toss()
            if Coin_Test.get_sideup() == "Heads":
                total_head += 1
            else:
                total_tail += 1
        Total_Heads_T.append(total_head)
        Total_Tails_T.append(total_tail)
    element_total_H = 0
    element_total_T = 0
    for i in Total_Heads_T:
        element_total_H += i
    for j in Total_Tails_T:
        element_total_T += j
    print(float(element_total_H/len(Total_Heads_T)), float(element_total_T/len(Total_Tails_T)))

def Poisson_PMF_Expected_value():
    lambda_value = int(input("Enter a positive number: "))
    k = int(input("Enter a positive number: "))
    total = 0
    for i in range(0, k):
        total += math.exp(-lambda_value)*((lambda_value**i)/math.factorial(i))
    print(total)

"""OK Expected Value is done here YAY"""

def EV_and_Variance():

    EV_array = []
    Second_Moment_Array = []
    #Input a bunch of float values here basically
    num_of_elements = int(input("Enter the number of elements you wish to put in: "))
    for element_count in range(num_of_elements):
        value = float(input("Enter a number: "))
        EV_array.append(float(value))
        Second_Moment_Array.append(float(value**2))
    total = 0
    for element in EV_array:
        total += float(element)
    mu = float(total/num_of_elements)
    print(mu)
    return mu
    second_moment_sum = 0
    for float_int in Second_Moment_Array:
        second_moment_sum += float(float_int)
    SM = float(second_moment_sum/num_of_elements)
    print(float(SM - (mu**2)))
    return (float(math.sqrt(SM - (mu**2))))

def EV():

    num_element = int(input("Enter the number of elements you wish to place in: "))
    total_mu =  0
    for element in range(num_element):
        number = int(input("Enter a number: "))
        total_mu += (float(number))
    mu = float(total_mu/num_element)
    print(mu)
    return mu

#We will now use the Law of Large Numbers coin flipping.
#Input a large list of results and then try to 
def Law_Of_Large_Numbers(List_a, List_b):
    while 
if __name__ == "__main__":
    coin_flip()
