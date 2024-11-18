def find_interval_sum(a,s): #soluzione con complessità O(n), tempo lineare
    current_sum = 0
    start = 0
    for end in range(len(a)):
        current_sum += a[end]
        while current_sum > s and start <= end:
            current_sum -= a[start]
            start += 1
        if current_sum == s:
            return start, end
    return None

#idea 1 se devo calcolare la somma a[k] per k = i ... j
# lo faccio usando un array b ausiliario che contiene somme di prefeissi
# di a crescenti (b[j+1]-b[i])

#idea 2: muovo i e j in funzione del confronto fra la somma di cui sopra e la somma s desiderata:
# se la somma è minore di s, incremento j
# se la somma è maggiore di s, incremento i
#sto sfruttando il fatto che l'array non contenga valori negativi
a = [int(x) for x in input().split(" ") if x]
s = int(input())

def find_interval_sum(a,s): #soluzione con complessità O(n), tempo lineare
b = [0] * (len(a) + 1) #moltiplicare un array per un numero intero replica intero #array #n elementi ci sono n+1 prefissi, il primo è vuoto (c malloc)
for k in range (1, len(a) + 1):
    b[k] = b[k-1] + a[k-1] #calcolo della somma dei prefissi
# comincio la ricerca
i = j = 0
while j < len(a): #guardia
    c = b[j+1] - b[i] #calcolo della somma di a[k] per k = i ... j 
    if c == s:
        return (i, j)
    elif c < s:
        j += 1
    else:
        i += 1
        if i > j: #correzione per non terminare precocemente, occhio a non sforare la guardia
            j = j + 1
return (-1,-1)


