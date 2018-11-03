n = int(input())
tele_dir = dict(input().split() for _ in range(n))
# d = dict(raw_input().split() for _ in range(n))

while(True):
    try:
        name = input()
        if name in tele_dir.keys():
            print(name +"="+tele_dir[name])
        else:
            print("Not found")
    except EOFError:
        break
