def one_away(str1, str2):
    if len(str1) == len(str2):
       return check_replacement(str1, str2)
    elif len(str1) + 1 == len(str2):
       return check_insertion(str1, str2):
    elif len(str1) - 1 == len(str2):
       return check_insertion(str2, str1)
    return false


def check_replacement(str1, str2):
    diff = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if diff:
                return False
            diff = True
    return True

def check_insertion(short, long):
    count1 = 0
    count2 = 0
    while(count1 < len(short) and count2 < len(long)):
        if short[count1] != short[count2]:
            if count1 != count2:
                return False
            count2 += 1
        else:
            count1 += 1
            count2 += 1
    return True
    