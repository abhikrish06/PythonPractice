import email.utils
import re

for _ in range(int(input())):
    s = email.utils.parseaddr(input())
    if re.match(r'[a-zA-Z](\w|-|\.|_)+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', s[1]):
        valid_email = s
        print(email.utils.formataddr(valid_email))
        