#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    # #if n is odd, print weird OR if n is even and 6<=n<=20, print weird
    if n % 2 != 0 or n%2==0 and 6 <= n and 20 >= n:
        print('Weird') 
    # #if n is even AND 2<n<5 print not weird OR if n = even and n>20, print not weird
    elif n % 2 == 0 and 2<=n and 5 >= n or n%2==0 and n>=20:
        print("Not Weird")
    
        
    