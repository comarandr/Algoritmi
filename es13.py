def quicksort (a, i,j)
    if j - i <= 1:
        return
    k = partition(a, i, j)
    quicksort(a, i, k)
    quicksort(a, k, j)