def arm(n):
    order = len(str(n))
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit**order
        temp //=10
    if sum == n:
        print("YES")
    else:
        print("NO")
    
    return 


number = int(input())
arm(number)