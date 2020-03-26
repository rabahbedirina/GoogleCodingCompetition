

T = int(input())
for i in range(1, T+1):
    N, B, P = map(int, input().split())
    arr = []
    for j in range(N):
        arr.append(list(map(int, input().split())))

    print("Case #{}: {}".format(i, arr))
