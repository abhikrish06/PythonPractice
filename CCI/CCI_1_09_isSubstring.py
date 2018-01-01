# Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

def isRotation(str1, str2):
    if len(str1) != len(str2):
        return False
    return isSubstring(str1 + str1, str2)


def isSubstring(str1, str2):
    if len(str2) > len(str1):
        return False
    for i in range(len(str1) - len(str2) + 1):
        isSubstringexists = True
        for j in range(len(str2)):
            if str1[i + j] != str2[j]:
                isSubstringexists = False
                break
        if isSubstringexists:
            return True
    return False


print(isRotation("abhikrish", "ishabhikr"))
