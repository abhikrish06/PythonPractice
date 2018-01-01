# Implement a method to perform basic string compression using the counts
# of repeated characters.

def string_compression(ip_str): # requirement is different see line# 24
    str_d = {}
    str_d_list = []
    for i in ip_str:
        str_d[i] = ip_str.count(i)
    #print(str_d)
    for key, value in str_d.items():
        str_d_list.append(key)
        str_d_list.append(str(value))
    #print(str_d_list)
    cmp_str = "".join(str_d_list)
    #print(cmp_str)
    if len(ip_str) > len(cmp_str):
        print(cmp_str)
    else:
        print(ip_str)


string_compression("aabcccdddAABBBBDDDEEEFF")
string_compression("abhishekkrishna")
string_compression("aabcccccaaa") # output: a5b1c5 ; expected output: a2blc5a3

def str_compression(ip_str):
    ip_str_list = []
    curr_letter = ip_str[0]
    cntr = 0
    for i in ip_str:
        if curr_letter == i:
            cntr += 1
        else:
            ip_str_list.append(curr_letter + str(cntr))
            curr_letter = i
            cntr = 1
    ip_str_list.append(curr_letter + str(cntr))
    cmprssd_str = "".join(ip_str_list)

    if len(cmprssd_str) < len(ip_str):
        return cmprssd_str
    else:
        return ip_str

print(str_compression("aabcccdddAABBBBDDDEEEFF"))
print(str_compression("abhishekkrishna"))
print(str_compression("aabcccccaaa"))
