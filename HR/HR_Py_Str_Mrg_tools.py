# https://www.hackerrank.com/challenges/merge-the-tools/problem

def rem_dups(sub_str):
    str_d = []
    for i in range(len(sub_str)):
        if sub_str[i] in str_d:
            continue
        else:
            str_d.append(sub_str[i])
    return ''.join(str_d)

#print(rem_dups('cdeefaab'))

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        print(rem_dups(string[i:i+k]))
        # print(i)
        # print(string[i:i + k])
    return

merge_the_tools("AABCAAADA",3)