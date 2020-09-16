
filename = 'test.fna'
test = open(filename)
testread = test.read()
print(testread)
tofind = "TTTATACCTTCC"
# =============================================================================
# testread = "geeksforgeeks"
# tofind = "geeks"
# =============================================================================
count = 0
LengthOfToFind = len(tofind)
LengthOfTestRead = len(testread)

for x in range(LengthOfTestRead - LengthOfToFind + 1):
    #print(testread[x])
    for y in range(LengthOfToFind):
        #print(tofind[y])
        if (testread[y+x] != tofind[y]):
            break
        if (y + 1 == LengthOfToFind):
            print("found at index " + str(x))
            
def BruteForce_search(text, pattern):
    for x in range(len(text) - len(pattern) + 1):
        for y in range(len(pattern)):
            if(text[y+x] != pattern[y]):
                break
            if (y + 1 == len(pattern)):
                print("found at index " + str(x))
                
BruteForce_search(testread, tofind)
