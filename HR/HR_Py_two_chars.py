# https://www.hackerrank.com/challenges/two-characters/problem

def validateString(str):
    for i in range(len(str) - 1):
        if str[i] == str[i+1]:
            return False
    return True


def twochars(ip_str):
    st = list(set(ip_str))
    print(st)
    max_len = 0
    for i in range(len(st)):
        for j in range(i+1, len(st)):
            c_list = [c for c in ip_str if c == st[i] or c == st[j]]
            print(c_list)
            if validateString(c_list):
                max_len = max(max_len, len(c_list))
    return max_len

print(twochars('beabeefeab'))