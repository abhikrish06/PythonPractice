from collections import defaultdict
from fractions import gcd
import functools


class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) == 0 or len(deck) == 1:
            return False
        dct = defaultdict()
        for v in deck:
            if v in dct:
                dct[v] += 1
            else:
                dct[v] = 1

        res = functools.reduce(gcd, list(dct.values()))

        return False if res == 1 else True