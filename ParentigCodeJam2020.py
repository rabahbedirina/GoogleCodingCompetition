def main():
    n = int(input())
    things = [list(map(int, input().split())) for i in range(n)]
    print(things)
    things = [[things[i][0], things[i][1], i] for i in range(n)]
    print(things)
    things.sort(key=lambda x: x[0])
    print(things)
    a, b = -1, -1
    res = [None for i in range(n)]
    print(res)
    for i in range(n):
        if things[i][0] < a:
            if things[i][0] < b:
                return 'IMPOSSIBLE'
            else:
                b = max(b, things[i][1])
                res[things[i][2]] = 'J'
        else:
            a = max(a, things[i][1])
            res[things[i][2]] = 'C'
    print(res)
    return ''.join(res)


t = int(input())

for i in range(t):
    print("Case #{}: {}".format(i+1, main()))
