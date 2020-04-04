
T = int(input())
for i in range(1, T+1):
    N = int(input())
    S = []
    E = []
    y = ""
    for j in range(N):
        a, b = map(int, input().split())
        S.append(a)
        E.append(b)
    for p in range(N):
        for k in range(p + 1, N):
            if S[p] <= S[k] and S[k] < E[p]:
                # print("yes")
                y += "C"
            else:
                # print("NO")
                y += "J"
    print("Case #{}: {}".format(i, y))
