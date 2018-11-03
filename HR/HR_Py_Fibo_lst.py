def fibonacci(n):
    # return a list of fibonacci numbers
    lst = []
    for i in range(n):
        if i == 0 or i == 1:
            lst.append(i)
        else:
            lst.append(lst[i-1]+ lst[i-2])
    return print(lst)


fibonacci(7)