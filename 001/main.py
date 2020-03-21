#!/usr/bin/env python3
import collections
import itertools as it
import math
import numpy as np


while 1:
    # A = input()
    # A = int(input())
    n, x = map(int, input().split())
    plus1 = lambda x: x + 1
    # A = list(map(int, input().split()))
    # A = [int(input()) for i in range(N)]
    #
    # c = collections.Counter()

    if (n, x) == (0, 0):
        break
    else:
        c = 0
        for i in range(n):
            for j in range(i):
                for k in range(j):
                    if (i+1) + (j+1) + (k+1) == x:
                        c += 1

    print(c)