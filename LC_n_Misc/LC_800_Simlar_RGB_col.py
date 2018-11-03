class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        p, q, r = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        print(p, q, r)
        diff = {}
        # for i in range(16):
        #     if i > 9:
        #         hx = hex(i)
        #         u = ''.join([hx.replace('0x', ''), hx.replace('0x', '')])
        #         # print(''.join([u.replace('0x', ''), u.replace('0x', '')]))
        #     else:
        #         u = ''.join([str(i), str(i)])
        #         # print(u)

        for i in range(0, 256, 17):
            for j in range(0, 256, 17):
                for k in range(0, 256, 17):
                    # v = ["{:02x}".format(i), "{:02x}".format(j), "{:02x}".format(k)]  # or X for uppercase
                    diff[i,j,k] = (-(p - i) ^ 2 - (q - j) ^ 2 - (r - k) ^ 2)
                    #print(v)
            #print(p, int(v, 16))
        # print(-(p - 0x11) ^ 2 - (q - 0xee) ^ 2 - (r - 0x66) ^ 2)
        # for i in range(0,16777215+1):
        print(diff)
        # max_key = max(diff, key=lambda k: diff[k])
        # print(max_key, diff[max_key])

        return True


# -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2
obj = Solution()
obj.similarRGB("#09f166")
