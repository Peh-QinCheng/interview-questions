def permutate(fixed, chars):
    if len(chars) == 1:
        print fixed + chars
        return
    for i in range(len(chars)):
        head = fixed + chars[i]
        rest = chars[0:i] + chars[i+1:len(chars)]
        permutate(head, rest)

def permutate_new(fixed, chars, arr):
    if len(chars) == 1:
        return arr.append(fixed + chars)
    for i in range(len(chars)):
        head = fixed + chars[i]
        rest = chars[0:i] + chars[i+1:len(chars)]
        permutate_new(head, rest, arr)
    return arr


# permutate("", "ABC")
print permutate_new("", "ABCD", [])