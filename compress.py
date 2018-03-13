from collections import defaultdict

def compress(test_string):
    compressed_arr = []
    count = 1
    for i in range(len(test_string)):
        count_char = test_string[i]
        if i+1 == len(test_string):
            compressed_arr.extend((count_char, str(count)))
            count = 1
        if i+1 == len(test_string) or count_char != test_string[i+1]:
            compressed_arr.extend((count_char, str(count)))
            count = 1
        else: 
            count += 1
    if len(compressed_arr) >= len(test_string):
        return test_string
    else:
        return ''.join(compressed_arr)    

