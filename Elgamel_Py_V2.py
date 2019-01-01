import math
import sys
import random

#So where to start?
#OK so see the notes that I had from my Elgamel Py V1. I'm trying to make this and use class statements.

class Public_Key(object):
  
  #prime is the prime value of the space that we are working in, and g is the 
  def __init__(self, prime=None, g=None, x=None):
    self.prime = prime
    self.g = g
    self.x = x
 
class Private_Key(object):

  def __init__(self, prime=None, g=None, x=None):
    self.prime = prime
    self.g = g
    self.x = x
    
#These functions are needed. We assume that a > b
def gcd(a, b):
  while b != 1:
    c = a % b
    a = b
    b = c
  return a

def exp_modulus(a, b, c):
  return pow(a, b, c)

def
