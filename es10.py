# Versione O(n^2)
def max_difference_n2(arr):
    max_diff = float('-inf')
    n = len(arr)
    pair = (0, 0)
    
    for i in range(n):
        for j in range(i, n):
            if arr[j] - arr[i] > max_diff:
                max_diff = arr[j] - arr[i]
                pair = (i, j)
    
    return pair

# Versione O(n)
def max_difference_n(arr):
    n = len(arr)
    if n < 2:
        return (0, 0)
    
    min_index = 0
    max_diff = float('-inf')
    pair = (0, 0)
    
    for j in range(1, n):
        if arr[j] - arr[min_index] > max_diff:
            max_diff = arr[j] - arr[min_index]
            pair = (min_index, j)
        
        if arr[j] < arr[min_index]:
            min_index = j
    
    return pair

# Esempio di utilizzo
if __name__ == "__main__":
    V = [14, 16, 1, 5, 13, 0, 3]
    print("Versione O(n^2):", max_difference_n2(V))  # Output: (2, 4)
    print("Versione O(n):", max_difference_n(V))    # Output: (2, 4)

