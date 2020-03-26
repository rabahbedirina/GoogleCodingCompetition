t = int(input())
for j in range(1, t + 1):
    n = input()
    if int(n) > 0:
        seen = set(n)
        expected = {'0', '1', '8', '6', '5', '9', '4', '3', '2', '7'}
        i = 1
        while seen != expected:
            prod = str(int(n) * i)
            seen.update(set(prod))
            i += 1
        print("Case #{}: {}".format(j, prod))
    else:
        print("Case #{}: INSOMNIA".format(j))
