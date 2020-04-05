def main():
    s = input()
    y, l = '', 0
    for i in s:
        i = int(i)
        for j in range(i-l):
            y += '('
        for j in range(l-i):
            y += ')'
        y += str(i)
        l = i
    for i in range(l):
        y += ')'
    return y


t = int(input())

for i in range(t):
    print("Case #{}: {}".format(i+1, main()))
