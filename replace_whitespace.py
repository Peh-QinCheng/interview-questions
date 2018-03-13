def replace_whitespace(str, length):
    new_str = []
    for i in range(length):
        if str[i] == ' ':
            new_str.append('%20')
        else:
            new_str.append(str[i])
    return ''.join(new_str)