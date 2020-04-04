

T = int(input())
for i in range(1, T+1):
    N = int(input())
    arr = []
    t = 0
    r = 0
    c = 0
    for j in range(N):
        ar = list(map(int, input().split()))
        arr.append(ar)
        t += arr[j][j]
        setrows = len(set(ar))
        if setrows != N:
            r += 1
    print(arr)

    for m in range(N):
        arrinv = []
        for p in range(N):
            arrinv.append(arr[p][m])
        setcolum = len(set(arrinv))
        if setcolum != N:
            c += 1

    print("Case #{}: {}  {}  {}".format(i, t, r, c))
