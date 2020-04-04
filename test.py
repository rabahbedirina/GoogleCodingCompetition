
arr = [1, 2, 3]
tmplist = arr[:]
latin_square = []
for j in range(len(arr)):
    print(tmplist)
    latin_square.append(tmplist[:])
    tmplist = tmplist[1:] + [tmplist[0]]
print(latin_square)
