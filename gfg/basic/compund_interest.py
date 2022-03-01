def fact(n):
    fact = 1
    while(n > 1):
        fact *= n
        n -= 1
    return fact
 
    # return 1 if (n==1 or n==0) else n * fact(n - 1);

n = int(input())
print(fact(n))
a = 1
b = 5
a *= b
print(a)