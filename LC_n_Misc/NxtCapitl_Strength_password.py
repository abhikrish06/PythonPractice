# Complete the function below.

def strengthen_passwords(passwords):
    ch = ['s', 'S']
    for i in range(len(passwords)):
        ps = passwords[i]
        n = len(ps)
        if n == 1:
            for j in ch:
                if j in ps:
                    ps = ps.replace(j, '5')
        else:
            for j in ch:
                if j in ps:
                    ps = ps.replace(j, '5')

            lst_pass = list(ps)
            #print('len_lst_pass:', len(lst_pass))
            if n % 2 != 0:
                mid_ch = lst_pass[n // 2]
                if mid_ch.isdigit():
                    lst_pass[n // 2] = str(2 * int(mid_ch))
            elif n % 2 == 0:
                temp = lst_pass[-1]
                lst_pass[-1] = lst_pass[0]
                lst_pass[0] = temp
                a, b = lst_pass[0], lst_pass[-1]
                print(a, b)
                if a.islower() and b.isupper():
                    lst_pass[0] = a.upper()
                    lst_pass[-1] = b.lower()
                elif a.isupper() and b.islower():
                    lst_pass[0] = a.lower()
                    lst_pass[-1] = b.upper()
                elif a.isupper() and b.isupper():
                    lst_pass[0] = a.lower()
                    lst_pass[-1] = b.lower()
                elif a.islower() and b.islower():
                    lst_pass[0] = a.upper()
                    lst_pass[-1] = b.upper()
            # cnt = passwords.lower().count('nextcapital')
            # if cnt == 1:
            if ps.lower().count('nextcapital'):
                ind = ps.lower().index('next')
                txt = lst_pass[ind:ind+4]
                rev = txt[::-1]
                print(ind, txt, rev)
                for indx in range(4):
                    lst_pass[ind + indx] = rev[indx]
            passwords[i] = ''.join(lst_pass)
    return passwords

#passwords = ['GoCardinals', 'Doge', 'KfghjD', 'nExTcapITalxnextcapital', 'ThreeSThree']
passwords = ['hooRayTxeNcapItaLnextcapitall']

print(strengthen_passwords(passwords))