order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

# alternate soln
import string

print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')
