# Given a string consisting of uppercase and lowercase letters,
# remove the matching pairs (Aa, Bb, etc) until there are no matching pairs within the string.

from pythonds.basic.stack import Stack

def matchingPair(ip_str):
    if ip_str[0].islower() or len(ip_str) ==0:
        return -1
    s = stack()
    stack.push(ip_str[0])
