#Building prefix array

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

# filename = 'test.fna'
# test = open(filename)
# text = test.read()
# tofind = "TTTATACCTTCC"
text = "aaaabaaaaabbbaaaab"
pattern = "aaab"
prefix_arr = buildarray(pattern)
pattern_i = 0
for text_i in range(0, len(text)):
    if pattern[pattern_i] == text[text_i]:
        pattern_i += 1
        if pattern_i == len(pattern):
            found_index = text_i - len(pattern) + 1
            print("Found at index: " + str(found_index))
            pattern_i = prefix_arr[pattern_i-1]

    else:
        while pattern_i > 0:
            pattern_i -= 1
            pattern_i = prefix_arr[pattern_i]
            if pattern[pattern_i] == text[text_i]:
                pattern_i += 1
                break
