class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dom_len = len(cpdomains)
        dom_dict, sub_dom_dict = {}, {}
        res = cpdomains
        for i in range(dom_len):
            val, key = cpdomains[i].split(' ')
            # print(val, key)
            dots = key.count('.')
            if dots == 1:
                lst = list(key.split('.'))
                # print(lst)
                if lst[1] in sub_dom_dict:
                    sub_dom_dict[lst[1]] += int(val)
                else:
                    sub_dom_dict[lst[1]] = int(val)

            else:
                lst = list(key.split('.'))
                sub_st = str(lst[1] + '.' + lst[2])
                if sub_st in sub_dom_dict:
                    sub_dom_dict[sub_st] += int(val)
                else:
                    sub_dom_dict[sub_st] = int(val)

                if lst[2] in sub_dom_dict:
                    sub_dom_dict[lst[2]] += int(val)
                else:
                    sub_dom_dict[lst[2]] = int(val)

        for k, v in sub_dom_dict.items():
            vl = str(str(v) + ' ' + str(k))
            res.append(vl)

        return res

obj = Solution()
print(obj.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))