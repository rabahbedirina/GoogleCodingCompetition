

T = int(input())
for i in range(1, T+1):
    s = (str(input().strip().replace("(", ""))).replace(")", "")
    y = ""
    for j in s:

        if j != "0" and not j.isspace() and j != "":
            n = int(j)
            c = "("*n+j+")"*(n)
        else:
            c = j
        y += c

    y = y.replace(")(", "")
    print("Case #{}: {} ".format(i, y))
