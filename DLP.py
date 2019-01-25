import math
import random

def main():
  
    g = int(input("Enter a number: "))
    prime = int(input("Enter a number: "))
    target = int(input("Enter a number: "))
    for i in range(prime):
        if g**i % prime == target:
            return i
    print(i)
   
main()
