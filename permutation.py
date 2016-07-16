#!/usr/bin/python3

import sys

def perm2(m):
    if m == 0:
        print(P)
    else:
        for j in range(0, len(P)):
            if P[j] == 0:
                P[j] = m
                perm2(m - 1)
                P[j] = 0

# main
"""
n = int(sys.argv[1])
P = []
for j in range(0, n):
    P.append(0)
perm2(n)
"""
n = int(sys.argv[1])
P = []
for i in range(0, n+1):
    for j in range(0, i):
        P.append(0)
    perm2(i)
    P = []

