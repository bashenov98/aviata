def minimumBribes(arr, t):
    a = [0] * len(arr)
    for i in range(t):
        if (int(q[i])-(i+1)>2):
            return -1
    while True:
        mustCheck = False
        for i in range(1,t):
            if (int(q[i-1]) > int(q[i])):
                a[int(q[i - 1]) - 1] += 1
                mustCheck = True
                q[i - 1], q[i] = q[i], q[i - 1]
        if not mustCheck :
            break

    return sum(a)



t = int(input())
for i in range(t):
    t = int(input())
    c = input()
    q = c.split(" ")
    ans = minimumBribes(q,t)
    if (ans == -1):
        print("Too chaotic")
    else:
        print(ans)

# 2 1 5 3 4

# 3 1 2 5 4




