# a method to replace all spaces in a string with '%20'.

def URLify(ip_str, true_len):
    lst_ip = list(ip_str.strip())
    for i in range(true_len):
        if lst_ip[i] == " ":
            lst_ip[i] = "%20"
    lst_ip.append("%20")
    return "".join(lst_ip)

import time
start = time.clock()

print(URLify("i am krishna                  ",12))

print(time.clock() - start)