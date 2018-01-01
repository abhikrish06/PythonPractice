def unique_string(ip_string):
    chars = []
    for i in ip_string:
        if i in chars:
            return False
        else:
            chars.append(i)
    return True

print(unique_string("abhi"))