def interval(a,b):
    count = 0
    for i in range(a,b+1):
        if i%2!=0:
            count += 1
    return count

low = int(input())
high = int(input())
print(interval(low,high))

#Method 2
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        return (((high - low)//2) + 1)