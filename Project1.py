# -*- coding: utf-8 -*-
"""
Algo lab proj 1
"""

#Building prefix array for kmp
def buildarray(pattern):
    list = [0]
    j = 0
    found = False
    for i in range(1, len(pattern)):
        if (pattern[i] == pattern[j]):
            list.append(j+1)
            j += 1
        else:
            while j > 0:
                j -= 1
                j = list[j]
                if (pattern[i] == pattern[j]):
                    list.append(j+1)
                    j += 1
                    found = True
                    break
            if not found:
                list.append(0)
            else:
                found = False
    return list

def kmp(text, pattern):
    #text = "AAAAAAAAAA"
    #pattern = "AAA"
    prefix_arr = buildarray(pattern)
    pattern_i = 0
    for text_i in range(0, len(text)):
        if pattern[pattern_i] == text[text_i]:
            pattern_i += 1
            if pattern_i == len(pattern):
                found_index = text_i - len(pattern) + 1
                print("Pattern found at index: " + str(found_index))
                pattern_i = prefix_arr[pattern_i-1]

        else:
            while pattern_i > 0:
                pattern_i -= 1
                pattern_i = prefix_arr[pattern_i]
                if pattern[pattern_i] == text[text_i]:
                    pattern_i += 1
                    break
  
# prints all occurrences of pattern  
# in text using Z algo 
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
            
def BruteForce_search(text, pattern):
    for x in range(len(text) - len(pattern) + 1):
        for y in range(len(pattern)):
            if(text[y+x] != pattern[y]):
                break
            if (y + 1 == len(pattern)):
                print("Pattern found at index " + str(x))

def main():
    filename = input("Please input file location:\n")
    filename = filename[1:len(filename)-1]
    #print(filename)
    genome_file = open(filename)
    genome_string = genome_file.read()
    genome_string = genome_string[genome_string.find('\n')+1:]
    pattern = input("Please input pattern to find:\n")
    #pattern = "TGACAGA"
    canloop = True
    while canloop: #easier to test algo
        print("--------------------------")
        print("Available algorithms")
        print("1.Brute Force")
        print("2.KMP")
        print("3.Z Algo") 
        print("4.Enter another file location")
        select = input("Enter input 1-3\n") #Placeholder
        select = int(select)
        if (select == 1):
            BruteForce_search(genome_string, pattern)
        elif (select == 2):
            kmp(genome_string, pattern)
        elif (select == 3):
            searchZ(genome_string, pattern)
        elif (select == 4):
            filename = input("Please input file location:\n")
            filename = filename[1:len(filename)-1]
            genome_file = open(filename)
            genome_string = genome_file.read()
            genome_string = genome_string[genome_string.find('\n')+1:]
            pattern = input("Please input pattern to find:\n")
        else: #key in anything else to exit loop
            print("error")
            canloop = False
    

    
                
if __name__ == '__main__':
    main()