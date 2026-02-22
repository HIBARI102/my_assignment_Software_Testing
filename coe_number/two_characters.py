def alternate(s):

    unique_chars = list(set(s))
    max_len = 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1 = unique_chars[i]
            char2 = unique_chars[j]

            last_char = ""
            current_len = 0
            is_valid = True

            for char in s:
                if char == char1 or char == char2:

                    if char == last_char:
                        is_valid = False
                        break
                    last_char = char
                    current_len += 1

            if is_valid:
                max_len = max(max_len, current_len)

    return max_len
