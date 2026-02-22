def staircase(n, display):
    if not (0 < n <= 30):
        return "Out of range"

    result = ""
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        symbols = display * i
        result += spaces + symbols
        if i < n:
            result += "\n"
    return result
