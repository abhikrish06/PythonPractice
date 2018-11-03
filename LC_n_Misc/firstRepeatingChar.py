# Given a string, find its first non-repeating character using 2 loops O(n^2)

def firstRepeatingChar(ip_str):
    for i in range(len(ip_str)):
        isRepeated = False
        for j in range(len(ip_str)):
            if i != j and ip_str[i] == ip_str[j]:
                isRepeated = True
                break

        if isRepeated == False:
            return ip_str[i]

    return "no non-repeating character"


print(firstRepeatingChar("baby"))
print(firstRepeatingChar("ccoolloorr"))
print(firstRepeatingChar("color"))