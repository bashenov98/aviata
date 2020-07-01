def repeatedString(s, n):
    ans = 0
    for i in range(n):
        if s[i] == 'a':
            ans = ans + 1
    return ans


s = input()
n = int(input())

if n > len(s):
    s = s*int((n/len(s))+1)

print(repeatedString(s, n))

