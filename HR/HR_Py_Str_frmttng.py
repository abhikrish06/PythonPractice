def print_formatted(number):
    # your code goes here
    pl = len(bin(number).lstrip("0b"))
    print(pl)
    for i in range(1, number+1):
        print(str(i).rjust(pl) +(oct(i).lstrip("0o")).rjust(pl) + (hex(i).lstrip("0x")).upper().rjust(pl) + (bin(i).lstrip("0b")).rjust(pl+1))
print_formatted(17)