

T = int(input())
for i in range(1, T+1):
    N, B = map(int, input().split())
    Ai = list(map(int, input().split()))
    arr = sorted(Ai)
    s = 0
    c = 0

    for item in arr:
        s += item
        if s <= B:
            c += 1

    print("Case #{}: {}".format(i, c))
