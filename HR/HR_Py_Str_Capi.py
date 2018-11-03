import string

def cap_func(strng):
    return string.capwords(strng, " ")

def capitalize(ip_string):
    return ' '.join([word.capitalize() for word in ip_string.split(' ')])

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)

# print(string.capwords("1 w 2 r 3g"))
# 1 w 2 r 3g
# 1 W 2 R 3g