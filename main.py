import sys
def search(s,k):
    l = 0
    r = n-1

    while l <= r:
        m = (l + r) // 2

        if s[m] == k:
            print(a[k])
            return
        elif s[m] < k:
            l = m + 1
        else:
            r = m - 1
    print(0)
    return


n = int(sys.stdin.readline())
s1 = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
s2 = list(map(int,sys.stdin.readline().split()))

s1.sort()

a = {}
for num in s1:
    if num not in a:
        a[num] = 1
    else:
        a[num] += 1

for num in s2:
    search(s1,num)



