# sorting
def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    sorted1 = sorted(str1)
    sorted2 = sorted(str2)
    for i in range(len(str1)):
        if sorted1[i] != sorted2[i]:
            return False
    return True


# freq
def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    freq = [0 for _ in range(128)]
    for i in str1:
        value = ord(i)
        freq[value] += 1
    for j in str2:
        value = ord(j)
        freq[value] -= 1
        if freq[value] < 0:
            return False
    return True