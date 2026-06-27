def lps(pattern):
    table = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:
            length += 1
            table[i] = length
            i += 1

        else:
            if length:
                length = table[length - 1]
            else:
                table[i] = 0
                i += 1

    return table

def search(text, pattern):
    table = lps(pattern)

    i = j = 0

    while i < len(text):

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            return i - j

        elif i < len(text) and text[i] != pattern[j]:
            if j:
                j = table[j - 1]
            else:
                i += 1

print(search("ababcabcababd", "ababd"))
