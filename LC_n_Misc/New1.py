def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


def roman2numeric(ip_str):
    total_final = 0
    i = 0
    while(i < len(ip_str)):
        v1 = value(ip_str[i])

        if (i + 1 < len(ip_str)):

            # Getting value of symbol s[i+1]
            v2 = value(ip_str[i + 1])

            # Comparing both values
            if (v1 >= v2):

                # Value of current symbol is greater or equal to the next symbol
                total_final = total_final + v1
                i = i + 1
            else:

                # Value of current symbol is less to the next symbol
                total_final = total_final + v2 - v1
                i = i + 2
        else:
            total_final = total_final + v1
            i = i + 1

    return total_final

print("Integer form of Roman Numeral is ",end="")
print(roman2numeric("CMIX"))