# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:14:22 2020

@author: john lee
"""

# Fills Z array for given string str[] 



def searchZ(text, pattern):

    string = pattern + '$' + text
    z = [0] * len(string)

    n = len(string)

    l, r, k = 0, 0, 0

    for i in range(1, n):
        if i > r:
            l, r = i, i

            while r < n and string [r-l] == string[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i-l

            if z[k] < r - i + 1:
                z[i] = z[k]

            else:
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1

    for i in range(n):
        if z[i] == len(pattern):
            print("Pattern found at index", i - len(pattern) - 1)
  
# Driver Code 
if __name__ == "__main__":
    filename = 'test.fna'
    test = open(filename)
    text = test.read()
    # text = "GEEKS FOR GEEKS"
    # pattern = "GEEK"
    pattern = "TTTATACCTTCC"
    searchZ(text, pattern) 
    
