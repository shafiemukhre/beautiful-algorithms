"""
author: shafiemukhre
date: 10-05-2020
"""
class Solution:
    def karatsuba(self, x, y):
        X = str(x)
        Y = str(y)
        if len(X) == 1 or len(Y) == 1:
            return x*y

        n = len(X)
        m = n // 2

        a = int(X[:m])
        b = int(X[-m:])
        c = int(Y[:m])
        d = int(Y[-m:])

        ac = self.karatsuba(a, c)
        ad = self.karatsuba(a, d)
        bc = self.karatsuba(b, c)
        bd = self.karatsuba(b, d)
        
        formula = ((10**n)*ac) + (10**m)*(ad + bc) + bd
        return formula

s = Solution()
print(s.karatsuba(1234, 5678)) #7006652

#multiplication of 2 64-digit numbers
n1 = 3141592653589793238462643383279502884197169399375105820974944592
n2 = 2718281828459045235360287471352662497757247093699959574966967627
print(s.karatsuba(n1, n2)) #8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
 