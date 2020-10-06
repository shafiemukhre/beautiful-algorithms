## Karatsuba Multiplication

```python
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
```

## Karatsuba multiplication (refined)

```python
class Solution:
    def refined_karatsuba(self, x, y):
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

        #3 recursive calls instead of 4
        ac = self.refined_karatsuba(a, c) #step ①
        bd = self.refined_karatsuba(b, d) #step ②
        ad_plus_bc = self.refined_karatsuba(a+b, c+d) - bd - ac #step ④ = step ③ - ② - ① 
        
        formula = ((10**n)*ac) + (10**m)*ad_plus_bc + bd
        return formula
```