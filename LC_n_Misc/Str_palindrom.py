# check whether a given string is palindrome

ip_str = input()
rev_str = ip_str[::-1]

if ip_str == rev_str:
    print(True)
else:
    print(False)