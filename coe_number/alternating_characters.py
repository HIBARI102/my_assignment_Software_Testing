def alternatingCharacters(s):

    n = len(s)

    de = 0

    for i in range(1, n):

        if s[i] == s[i - 1]:

            de += 1

    return de
