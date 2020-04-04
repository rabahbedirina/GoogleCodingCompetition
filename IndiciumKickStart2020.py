

T = int(input())
for i in range(1, T+1):
    N, K = map(int, input().split())

    def latin_square(mylist):
        tmplist = mylist[:]
        latin_square = []
        for j in range(len(mylist)):
            latin_square.append(tmplist[:])
            tmplist = tmplist[1:] + [tmplist[0]]
        s = 0
        for k in range(len(latin_square)):
            s += latin_square[k][k]
        if s == K:
            print("Case #{}: POSSIBLE".format(i))
            for m in latin_square:
                print(*m, sep=" ")
        else:
            print("Case #{}: IMPOSSIBLE".format(i))

        return latin_square

    latin_square(list(range(1, N + 1)))
