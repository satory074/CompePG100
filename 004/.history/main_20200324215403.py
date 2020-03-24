#!/usr/bin/env python3
import collections
import itertools as it
import math
import numpy as np

# A = input()
# A = int(input())
N, M = map(int, input().split())
# A = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(N)]
#
# c = collections.Counter()

max = -1
for m1 in range(M):
    for m2 in range(M):
        if m1 != m2:
            tensu = 0
            for n in range(N):
                tensu += max(A[n][m1], A[n][m2])
