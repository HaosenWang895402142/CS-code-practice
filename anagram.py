def anagram(s1,s2):

    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        print('s1 pos',pos)
        c1[pos] = c1[pos] +1
        print('c1',c1)

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        print('s2 pos', pos)
        c2[pos] = c2[pos]+1
        print('c2',c2)

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(anagram('http','tthp'))