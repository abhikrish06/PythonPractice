class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills[0] != 5:
            return False

        # sum = bills[0]  # 5
        dct = {'5': 0, '10': 0, '20': 0}
        for i in range(len(bills)):
            if bills[i] == 5:
                dct['5'] += 1
                continue

            if bills[i] == 10 and dct['5'] > 0:
                dct['5'] -= 1
                dct['10'] += 1
                continue

            elif bills[i] == 20:
                if dct['10'] == 0 and dct['5'] >= 3:
                    dct['5'] -= 3
                    dct['20'] += 1
                    continue
                elif dct['10']>0 and dct['5']>0:
                    dct['10'] -= 1
                    dct['5'] -= 1
                    dct['20'] += 1
                    continue
                else:
                    return False
        # print(dct)
        return True


obj = Solution()
print(obj.lemonadeChange([5, 5, 10, 10, 20]))
print(obj.lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]))
print(obj.lemonadeChange([10, 10]))
