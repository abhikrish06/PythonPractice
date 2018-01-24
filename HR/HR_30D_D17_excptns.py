#Write your code here
class Calculator:
    def power(self, n, b):
        try:
            if n < 0 or b < 0:
                raise Exception('n and p should be non-negative')
            else:
                return pow(n, b)
        except ValueError:
            return 'n and p should be non-negative'

# conceptual one
class e(Exception):
    def __init__(self):
        Exception.__init__(self,"n and p should be non-negative")

class Calculator:
    def power(self,n,p):
        if  n < 0 or p < 0:
            raise e
        else:
            return n**p