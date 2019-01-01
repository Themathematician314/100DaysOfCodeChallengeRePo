#This is the practice coin class that I am going to be usign
import random

class Coin:

    def __init__(self):
        self.sideup = "Heads"
    
    def flip_coin(self):
    if randint(0,1) == 0:
        self.sideup = "Heads"
    else:
        self.sideup = "Tails"
        
    def get_sideup(self):
        return sideup
        
        
        
def main():
    new_coin = Coin()
    print("The side of my coin that is currently face up is: " new_coin.get_sideup())
    
main()
