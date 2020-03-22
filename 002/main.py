#!/usr/bin/env python3
import collections
import itertools as it
import math
import numpy as np

def yakusu(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

# A = input()
A = int(input())
# A = map(int, input().split())
# A = list(map(int, input().split()))
# A = [int(input()) for i in range(N)]
#
# c = collections.Counter()

c = 0
for n in range(1, A+1):
    if n % 2 == 1 and len(yakusu(n)) == 8:
        c += 1

print(c)