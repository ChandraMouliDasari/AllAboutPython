def element(arr,n,k):
    arr.sort()
    return arr[k-1]


n=int(input())
arr=list(map(int,input().split()))
k = int(input())
print(element(arr,n,k))