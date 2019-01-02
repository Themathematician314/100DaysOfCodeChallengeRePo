#This is the practice coin class that I am going to be usign
import random
from bs4 import BeautifulSoup
import math
import sys
import os

class Coin():

    def __init__(self):
        self.__sideup = "Heads"
    
    def flip_coin(self):
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
        
    def get_sideup(self):
        return self.__sideup
        
def main():
    new_coin = Coin()
    print("The side of my coin that is currently face up is: ", new_coin.get_sideup())
    
main()

def flipper():
    coin_2 = Coin()
    for i in range(100):
        coin_2.flip_coin()
        print(coin_2.get_sideup())
        
flipper()

class Dragon():
    
    def __init__(self, abilities=None, power=None, toughness=None, luck=None):
        self.__abilities = []
        self.__power = 0
        self.__toughness = 0
        self.__luck = 0

    def power_up(self):
        if self.__power == 0:
            self.__power = random.randint(4, 10)
            return self.__power
        
    def toughness_up(self):
        if self.__toughness == 0:
            self.__toughness = random.randint(4, 10)
            return self.__toughness
        
    def luck_up(self):
        if self.__luck == 0:
            self.__luck = random.randint(0, 5)
            return self.__luck

    def grant_skill(self):
        while self.__abilities == None:
            self.__abilities == "Flying"
            return self.__abilities
    
    def get_power(self):
        return self.__power
    
    def get_toughness(self):
        return self.__toughness
    
    def get_luck(self):
        return self.__luck
    
    def add_abilities(self):
        self.__abilites.append()
    
def main():
    First_Dragon = Dragon()
    First_Dragon.grant_skill()
    First_Dragon.power_up()
    First_Dragon.toughness_up()
    First_Dragon.luck_up()
    print(First_Dragon.get_power(), First_Dragon.get_toughness(), First_Dragon.get_luck())
    
main()
