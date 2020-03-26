import itertools as it
arr = [[1, 2, 3], ["a", "b", "c"]]
print(list(it.product(arr[0], arr[1]), [repeat=2]))
