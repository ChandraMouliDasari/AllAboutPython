def prime(n,k):
    lt = []
    for i in range(n,k):
        print('this is i',i)
        for j in range(2,int(i/2)+1):
            print("this is j",j)
            if i % j ==0:
                break
        else:
            lt.append(i)
    return lt



a = int(input())
b = int(input())
print(prime(a,b))