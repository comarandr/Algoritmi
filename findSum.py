def binary_search(arr, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_sum_pair(arr, S):
    n = len(arr)
    for i in range(n):
        complement = S - arr[i]
        j = binary_search(arr, i + 1, n - 1, complement)
        if j != -1:
            print(i, j)
            return
    print(-1, -1)

# Example usage
V = [3, 7, 8, 11, 15, 20, 24]
S = 23
find_sum_pair(V, S)