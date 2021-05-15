"""
sorting algorithms: Hackerranck Problems 
This link is quit important: https://www.hackerrank.com/challenges/tutorial-intro/problem 
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#problem 1: Intro 
def introTutorial(V, arr):
    for i in arr:
        if i == V:
            return arr.index(i)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#problem 2: Insertion Sort - Part 1 
def insertionSort1(n, arr):
    for j in range(1, n): #not sure n-1 or n 
        key = arr[j]
        i = j - 1 
        while i >= 0 and arr[i] > key: 
            arr[i+1] = arr[i]
            i -= 1
            #print(arr)
            print(*arr, end =' ')
            print(sep = '\n')
        arr[i+1] = key
    #print(arr)
    print(*arr, end=' ')

def insertionSort2(n, arr):
      for j in range(1, n): #not sure n-1 or n 
        key = arr[j]
        i = j - 1 
        while i >= 0 and arr[i] > key: 
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
        print(*arr, end =' ')
        print(sep = '\n')

    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)




