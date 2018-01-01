# Determine whether or not one string is a permutation of another
def strings_perm_chk(str1,str2):
    if len(str1) != len(str2):
        #print("inside len")
        return False
    else:
        #print("outside len")
        str1_d = {}
        str2_d = {}
        for i in str1:
            str1_d[i] = str1.count(i)
        for i in str2:
            str2_d[i] = str2.count(i)
        #print(str1_d)
        #print(str2_d)
        if sorted(str1_d) == sorted(str2_d):
            return True
        else:
            return False

def strings_perm_chk2(str1,str2):
    if len(str1) == len(str2):
        #print("inside len")
        if sorted(str1) == sorted(str2):
            return True
        else:
            return False
    else:
        #print("outside len")
        return False

def is_permutation(str1, str2):
  counter = Counter()
  for letter in str1:
    counter[letter] += 1
  for letter in str2:
    if not letter in counter:
      return False
    counter[letter] -= 1
    if counter[letter] == 0:
      del counter[letter]
  return len(counter) == 0

class Counter(dict):
  def __missing__(self, key):
    return 0

import time
start = time.clock()
#print(strings_perm_chk("abhishek","krishnaa")) #2.5297958983324115e-05(abhi,kris) 2.869619227959153e-05("abhishek","bhaikesh")
#print(strings_perm_chk2("abhishek","krishnaa")) #2.2277307164419744e-05(abhi,kris) 2.454279602859802e-05("abhishek","krishnaa")
print(is_permutation("abhishek","krishnaa")) #3.6625403304215507e-05(abhi,kris) 2.9073773756954577e-05 ("abhishek","krishnaa")

print(time.clock() - start)
