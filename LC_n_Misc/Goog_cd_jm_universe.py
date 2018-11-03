def calDamage(seq):
    dam = 0
    c_curr = 1
    cnt = 0
    lst_sq = list(seq)
    for ch in lst_sq:
        if ch == "S":
            dam = dam + c_curr
            # print("dam:", dam)
        else:
            cnt += 1
            c_curr = (2 ** cnt)
    # print(dam)
    return dam

def swapList(seq):
    lst_seq = list(seq)
    for i in range(len(seq)-1, -1, -1):
        if lst_seq[i] == 'S' and lst_seq[i-1] != 'S':
            lst_seq[i], lst_seq[i-1] = lst_seq[i-1], lst_seq[i]
            break
    return ''.join(lst_seq)

t = int(input())

for i in range(1, t+1):
    sh, seq = input().split(' ')
    sh_i = int(sh)
    final = False
    cntr = 0
    damage = calDamage(seq)

    if sh_i >= damage:
        print('Case #%i: %i' % (i, 0))
        final = True

    while not final:
        damage = calDamage(seq)
        if sh_i >= damage:
            print('Case #%i: %i' % (i, cntr))
            final = True
            break
        else:
            swapped_seq = swapList(seq)
            if swapped_seq == seq:
                print('Case #%i: %s' % (i, "IMPOSSIBLE"))
                final = True
                break
            else:
                cntr += 1
                seq = swapped_seq
                continue
