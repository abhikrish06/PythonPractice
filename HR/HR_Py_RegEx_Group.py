import re
m = re.search(r'([0-9a-zA-Z])\1+', input().strip())
print(m.group())
print(m.group(1) if m else -1)