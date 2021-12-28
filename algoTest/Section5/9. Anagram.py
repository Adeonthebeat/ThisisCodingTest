
# Anagram
# AbaAeCe
# baeeACA

# ABCDEGHKNOPQRUWXbcdfghikotuwxy
# XbCdfGhiNoPuwUyABcDEgHKkOtQRxW

# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoqrtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoqrtuvwxyz
# ZBCcdFfgIJKLMNOPQRSTvVxyYAabDEeGHhijklmnoqrtuUwWXzZBCcdFfgIJKLMNOPQRSTvVxyYAabDEeGHhijklmnoqrtuUwWXz


a = input()
b = input()

# str1 = dict()
# str2 = dict()
#
# for x in a:
#     str1[x] = str1.get(x, 0) + 1
#
# for x in b:
#     str2[x] = str2.get(x, 0) + 1
#
# for i in str1.keys():
#     if i in str2.keys():
#         if str1[i] != str2[i]:
#             print("NO")
#             break
#     else:
#         print("NO")
#         break
# else:
#     print("YES")

###########################################################
# [Dictionary 개선코드]
###########################################################
# str3 = dict()
#
# for x in a:
#     str3[x] = str3.get(x, 0) + 1
#
# for x in b:
#     str3[x] = str3.get(x, 0) - 1
#
# for i in x:
#     if str3.get(i) > 0:
#         print("NO")
#         break
# else:
#     print("YES")

###########################################################
# [리스트 해쉬 코드]
# 아스키 코드
# 65 ~ 90  (대문자 : - 65)
# 97 ~ 122 (소문자 : -71)
# 대문자 A = 65 -> index 0 ->> str4[ord(x) - 65]
###########################################################

str4 = [0] * 52
str5 = [0] * 52

for x in a:
    if x.isupper():
        str4[ord(x) - 65] += 1
    else:
        str4[ord(x) - 71] += 1

for x in b:
    if x.isupper():
        str5[ord(x) - 65] += 1
    else:
        str5[ord(x) - 71] += 1

for i in range(52):
    if str4[i] != str5[i]:
        print("NO")
        break
else:
    print("YES")