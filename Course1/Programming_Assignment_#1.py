a = 5698452856984528
b = 5698452856984528

def karatsuba(m, n, leng):
    if leng == 1:
        return m * n
    else:
        lower1 = m % (10**(leng/2))
        lower2 = n % (10**(leng/2))
        upper1 = m / (10**(leng/2))
        upper2 = n / (10**(leng/2))
        lower_prod  = karatsuba(lower1, lower2, leng / 2)
        upper_prod  = karatsuba(upper1, upper2, leng / 2)
        middle_prod =karatsuba(upper1+lower1, upper2+lower2,(max(len(str(upper1+lower1)), len(str(upper2+lower2))))) - upper_prod - lower_prod
        return upper_prod * 10**(leng/2*2) + middle_prod * 10**(leng/2) + lower_prod

t = karatsuba(a,b,len(str(a)))

print(t)
print(a*b)
print(a*b==t)
