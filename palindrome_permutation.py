from collections import defaultdict

def palindrome_permutation(str):
    stripped_str = str.replace(' ', '').lower()
    freq_table = defaultdict(int)
    for c in stripped_str:
        freq_table[c] += 1

    singular_found = False
    for _, val in freq_table.iteritems():
        if val % 2 != 0:
            if singular_found:
                return False
            else:
                singular_found = True
    return True