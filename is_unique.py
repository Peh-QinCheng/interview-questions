def is_unique(str):
    freq_table = {}
    for char in str:
        if char in freq_table:
            freq_table[char] += 1
        else:
            freq_table[char] = 1
    for freq in freq_table.values():
        if freq > 1:
            return False
    return True


## Solution
def is_unique(str):
    if len(str) > 128:
        return False
    char_set = [False for _ in range(128)]
    for char in str:
        ascii  = ord(char)
        if char_set[ascii]:
            return False
        else:
            char_set[ascii] = True
    return True

# No data structure
def is_unique(str):
    for i in range(len(str)):
        for j in range(len(str)):
            if i == j:
                continue
            if str[i] == str[j]:
                return False
    return True
