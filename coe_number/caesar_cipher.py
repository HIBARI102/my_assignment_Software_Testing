def caesarCipher(s, k):

    new_s = ""

    for i in s:

        if i >= "a" and i <= "z":
            new_s += chr((ord(i) - ord("a") + k) % 26 + ord("a"))

        elif "A" <= i <= "Z":
            new_s += chr((ord(i) - ord("A") + k) % 26 + ord("A"))

        else:
            new_s += i

    return new_s
