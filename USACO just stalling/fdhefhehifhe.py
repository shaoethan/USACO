#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
  ans=""
  if " "in s:
    lis=s.split(" ")
    for c in range(len(lis)):
      lis[c]=lis[c].capitalize()
    for i in range(len(lis)):
        if i!=len(lis)-1:
            ans+=lis[i]+" "
        else:
            ans+=lis[i]
    return ans
  else:
    return s.capitalize()

s=input()

print(solve(s))