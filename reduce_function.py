# Exercise: Reduce Function
# URL: https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true
# Description: Print only one line containing the numerator and denominator of the product 
# of the numbers in the list in its simplest form

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator
