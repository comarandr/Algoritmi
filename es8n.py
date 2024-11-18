


def find_sum(a, s):
    i = 0
    j = len(a) - 1
    while i < j: #ragionamento a matrice per quello
        if a[i] + a[j] == s:
            return i, j
        elif a[i] + a[j] < s:
            i += 1 #i = i+1
        else:
            j -= 1 #j = j+1
    return(-1,-1)

a = [int(x) for x in input().split(" ") if x]
s = int(input())

(i,j) = find_sum(a,s) #assegnamenti a più variabili
print(i,j) #output di due variabili