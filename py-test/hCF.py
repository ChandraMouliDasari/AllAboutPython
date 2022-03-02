def find_gcd(x, y):
    while(y):
        x, y = y, x % y
  
    return x
n=int(input())
arr=list(map(int,input().split()))
num1=arr[0]
num2=arr[1]
gcd=find_gcd(num1,num2)
  
for i in range(2,len(arr)):
    gcd=find_gcd(gcd,arr[i])
      
print(gcd)
