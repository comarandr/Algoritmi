def find_max_diff(a):
    #idea 1 se avessi array ausiliario b tale che
    # b[i] = max per j>=i di a[j]
    # b[i] = max a[i...]
    #allora sarebbe facile calcolare
    #max {a [j] - a[i] | i <= j}
    # = max {b[i] - a[i] | i = 0, ... n-1}
    #idea 2 : calcolare b di cui sopra è facile,
    # basta partire da i = n-1 e andare all'indietro
    # preprocessing per calcolare b[i] 
    b = [0] * len(a) #array di n elementi
    c = [0] * len(a) #array di n elementi
    curr_max = float('-inf')
    for k in range(len(b)-1, -1, -1):
        if a[i] > curr_max:
            curr_max = a[i]
            b[i] = curr_max
            c[i] = i
        else:
            b[i] = curr_max
            c[i] = c[i+1]
        b[k] = max(curr_max, a[k])
    
    curr_max_diff = float('-inf')
    best_i = None
    for i in range (0, len(a)):
        if b[i] - a[i] > curr_max_diff:
            curr_max_diff = b[i] - a[i]
            best_i = i
            best_j = c[i]
    return (best_i, best_j)
   


