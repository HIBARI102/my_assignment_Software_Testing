def funnyString(s):

    n = len(s)

    for i in range(1, n):

        diff1 = abs(ord(s[i]) - ord(s[i - 1]))

        diff2 = abs(ord(s[n - 1 - i]) - ord(s[n - i]))

        if diff1 != diff2:

            return "Not Funny"

    return "Funny"
