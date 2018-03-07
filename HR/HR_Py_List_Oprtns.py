if __name__ == '__main__':
    N = int(input())
    fin_lst = []

    for i in range(N):
        lst = input().split()
        #print(lst)
        if 'insert' in lst:
            getattr(fin_lst, lst[0])(int(lst[1]), int(lst[2]))
        elif 'remove' in lst:
            getattr(fin_lst, lst[0])(int(lst[1]))
        elif 'append' in lst:
            getattr(fin_lst, lst[0])(int(lst[1]))
        elif 'reverse' in lst:
            fin_lst.reverse()
        elif 'sort' in lst:
            fin_lst.sort()
        elif 'pop' in lst:
            fin_lst.pop()
        elif 'print' in lst:
            print(fin_lst)

