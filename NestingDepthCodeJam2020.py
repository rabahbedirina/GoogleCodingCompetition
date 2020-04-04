

T = int(input())
for i in range(1, T+1):
    s = (str(input().strip().replace("(", ""))).replace(")", "")
    y = ""
    for j in range(len(s)):

        if s[j] != "0" and not s[j].isspace() and s[j] != "":
            n = int(s[j])
            c = "("*n+s[j]+")"*n
        else:
            c = s[j]
        y += c
    count = 0

    for p in range(y.find("("), len(y)):

        if y[p] == "(":
            count += 1
        else:
            break
    for k in range(count):
        y = y.replace(")(", "")
    print("Case #{}: {} ".format(i, y))
