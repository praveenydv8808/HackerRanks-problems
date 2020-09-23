#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    if n>0 and n<=100:
        for e in range(1,n+1):
            for i in range(1,e+1):
                print("#",end=" ")
            print()
            
staircase(6)
