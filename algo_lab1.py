
filename = 'test.fna'
test = open(filename)
testread = test.read()
tofind = "TTTATACCTTCC"
#testread = "geeksforgeeks"
#tofind = "geeks"
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
