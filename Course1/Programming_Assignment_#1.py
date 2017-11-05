<<<<<<< HEAD
a = 1212121212121234343434343434343434444444444
b = 12345678998765432112345678987654321
=======
""" Karatsuba multiplication algorithm """

a = 5698452856984528
b = 5698452856984528
>>>>>>> a2ed8f7ba19b707d7ad28cc123774bb20173a2fc

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
