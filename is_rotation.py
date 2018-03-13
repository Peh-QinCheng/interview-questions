# def is_rotation(s1, s2):
#     if len(s1) != len(s2):
#         return False
#     counter = 0
#     s1_counter = 0
#     s2_counter = 0
#     substring1 = []
#     while((s1_counter < len(s1) - 1) && (s2_counter < len(s2) - 1)):
#         if s1[s1_counter] != s2[s2_counter]:
#             if len(substring1) != 0:
#                 break
#             s2_counter += 1
#         else:
#             substring1.append(s1[s1_counter])
#             s1_counter += 1
#             s2_counter += 1
#         substring1 = ''.join(substring1)
#         split_point = s1_counter - 1

def is_rotation(s1, s2):
    if len(s1) != len(s2) || len(s1) == 0 || len(s2) == 0:
        return False
    return isSubstring(s2, s1+s1)

def isSubstring(s1, s2):
    s1_counter = 0
    s2_counter = 0
    combo = False
    while(s1_counter < len(s1) and s2_counter < len(s2)):
        if s1[s1_counter] == s2[s2_counter]:
            combo = True
            s1_counter += 1
            s2_counter += 1
        else:
            if combo == True:
                return False
            s2_counter += 1
    if s1_counter == len(s1):
        return True
            