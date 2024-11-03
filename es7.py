def printArray(a):
    print(a, end = " ")
    
def scanArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens

def calcola_somma(a, i, j):
    somma = 0
    for k in range(i, j + 1):
        somma += a[k] #somma = somma + a[k]
    return somma

def calcola_max(a, i, j):
    m = 0
    for k in range(i, j + 1):
        m = max(m, a[k])
    return m

a = scanArray()
b = scanArray()

def preprocessing_per_somma(a):
    c = [0 for i in range(0, len(a)+1)]
    #c[k] = a[0] + a[1] + ... + a[k-1]
    c[0] = 0
    for k in range(1, len(a)+1):
        c[k] = c[k-1] + a[k-1]
    return c

c = preprocessing_per_somma(a)

def calcola_somma_furba(c, i, j):
    return c[j+1] - c[i]

for k in range(0, len(b), 2): #m iterazioni
    i = b[k]
    j = b[k + 1]
    print(calcola_somma(a, i, j), end = " ")

