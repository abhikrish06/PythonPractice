# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

def one_away(str1, str2):
    str1_d = {}
    str2_d = {}
    for i in str1:
        str1_d[i] = str1.count(i)
    for i in str2:
        str2_d[i] = str2.count(i)
    #print(str1_d)
    #print(str2_d)

    if len(str1) == len(str2):
        cntr = 0
        for key in str1_d:
            if key in str2_d and str1_d[key] == str2_d[key]:
                continue
            elif key not in str2_d and str1_d[key] == 1:
                cntr += 1
        if cntr == 0 or cntr == 1:
            return True
        elif cntr > 1:
            return False
    #elif len(str1) > len(str2):

print(one_away("pale","bale"))
print(one_away("pale","bake"))