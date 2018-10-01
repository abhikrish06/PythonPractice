class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.lst, self.keylst = [], []
        self.cntr = 0
        sm = 0
        for i in range(0, len(A) - 1, 2):
            # print(A[i])
            sm += A[i]
            if A[i] > 0:
                self.lst.append([sm, A[i+1]])
                self.keylst.append(sm)
        # print(self.dct)

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        # print(self.A)
        self.cntr += n
        # print(self.cntr)
        for k in self.lst:
            if self.cntr <= k[0]:
                return k[1]
            elif self.cntr > self.keylst[-1]:
                return -1


# Your RLEIterator object will be instantiated and called as such:
obj = RLEIterator([3,8,0,9,2,5])
param_1 = obj.next(2)

# ["RLEIterator","next","next","next","next"]
# [[[3,8,0,9,2,5]],[2],[1],[1],[2]]

# ["RLEIterator","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next"]
# [[[923381016,843,898173122,924,540599925,391,705283400,275,811628709,850,895038968,590,949764874,580,450563107,660,996257840,917,793325084,82]],
#  [612783106],   [486444202],  [630147341],  [845077576],  [243035623],[731489221],[117134294],[220460537],[794582972],[332536150],[815913097],[100607521],[146358489],[697670641],[45234068],[573866037],[519323635],[27431940],[16279485],[203970]]
#
# ["RLEIterator","next","next","next","next","next","next"]
# [[[784,303,477,583,909,505]],[130],[333],[238],[87],[301],[276]]
