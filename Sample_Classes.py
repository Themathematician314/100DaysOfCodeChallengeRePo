#This is the practice coin class that I am going to be usign
import random

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
        self.__abilites = abilites
        self.__power = power
        self.__toughness = toughness
        self.__luck = luck
        
    def get_abilities(self):
        return self.__abilities
    
    def get_power(self):
        return self.__power
    
    def get_toughness(self):
        return self.__toughness
    
    def stats_up(self):
        while power=None:
            power = 4
            return power
        while toughness=None:
            toughness = 4
            return toughness
    def grant_skill(self):
        while abilities=None:
            abilities ="Flying, Trample"
            return abilities
    
def main():
    First_Dragon = Dragon()
    
    First_Dragon
