# Given a string, write a function to check if it is a permutation of a palindrome.

def permutation_palindrome(ip_str):
    nw_ip_str = ip_str.replace(" ","")
    str_d = {}
    odd_cntr = 0
    for i in nw_ip_str:
        str_d[i] = nw_ip_str.count(i)
    print(str_d)
    for key in str_d:
        if str_d[key]%2 == 1:
            odd_cntr += 1
    if odd_cntr > 1:
        return False
    else:
        return True

print(permutation_palindrome("abha bhi     "))