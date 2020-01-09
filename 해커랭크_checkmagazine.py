#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    m_dict = Counter(magazine)
    n_dict = Counter(note)

    temp = n_dict - m_dict
    
    if len(temp) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
