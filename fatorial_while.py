#!/usr/bin/env python3
import sys
num = sys.argv[1]
num = int(num)
n = num - 1

while n >= 1:
	num = num*n
	n = n - 1
print(num)
