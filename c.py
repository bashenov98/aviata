def gloveMerchant(ar, n):
    ans = 0
    arSet = set(ar)
    for i in arSet:
        ans += ar.count(i)//2
    return ans
            
n = int(input())
c = input()
ar = c.split(" ")
print(gloveMerchant(ar, n))
