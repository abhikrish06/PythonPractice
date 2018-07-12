from sympy import sieve

class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        new_res = self.listPrime(N)
        for val in new_res:
            if val >= N:
                return val

    def listPrime(self,n):
        # "Return all primes <= n."
        res = list(sieve.primerange(2, 120000000))
        new_res = []
        for i in res:
            if str(i) == str(i)[::-1]:
                new_res.append(i)
        return new_res

obj =Solution()
# print(obj.primePalindrome(2))
# print(obj.primePalindrome(3))
# print(obj.primePalindrome(4))
# print(obj.primePalindrome(5))
# print(obj.primePalindrome(6))
# print(obj.primePalindrome(8))
# print(obj.primePalindrome(13))
print(obj.primePalindrome(9989900))

# import simplejson
# fp = open('primeNos.txt', 'w')
# simplejson.dump(list(sieve.primerange(2, 100000001)),fp)
# fp.close()


# new_res = []
# for i in list(sieve.primerange(2, 120000001)):
#     if str(i) == str(i)[::-1]:
#         new_res.append(i)
# fp = open('palinPrimeNos.txt', 'w')
# simplejson.dump(new_res,fp)
# fp.close()