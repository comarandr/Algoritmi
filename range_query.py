def printArray(a):
    print(a, end = " ")
    
def scanArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens

class Segment:
    def __init__(self, i, j, value, left, right): #costruttore def __init__      self.start = start
        self.i = i
        self.j = j
        self.value = value
        self.left = left
        self.right = right

#procedura per costruire un segment tree quasi bilanciato per un array A
def preprocess_max(a, i, j): #input array, prepara nodi per query, primo nodo è la radice. calcolo ricorsivo dei figli
    if i == j: #intervallo vuoto
        return None #nodo vuoto, None è il valore di default
    if i == j-1: #intervallo con un solo elemento
        return Segment(i, j, a[i], None, None)
    k = (i+j)//2 #indice di mezzo
    left = preprocess_max(a, i, k) #calcolo ricorsivo del figlio sinistro
    right = preprocess_max(a, k, j) #calcolo ricorsivo del figlio destro
    return Segment(i, j, max(left.value, right.value), left, right) #creazione del nodo corrente
    
def prefisso_piu_lungo(s, i ,j): #cerca il prefisso più lungo di s che è un prefisso di i, j
    assert(i<j) #precondizione
    assert(s.i <= i) #precondizione
    #caso base
    if s.i == i and s.j <= j: #caso base, il prefisso è il nodo corrente
        return s #termino ricerca con un prefisso
    #caso induttivo 
    if i < s.left.i:
        return prefisso_piu_lungo(s.left, i, j)
    else:
        return prefisso_piu_lungo(s.right, i, j)

def calcola_max(s, i, j): #calcola il massimo nell'intervallo i, j
    assert(i <= j) #precondizione
    if i == j: #intervallo vuoto
        return float ('-inf') #valore minimo possibile, potrei usare il None, ma devo ricordare di gestirlo (max none, n = n)
    # caso induttivo, vorrei trovare il primo nodo della partizione
    #primo nodo deve essere un prefisso dell'intervallo, iniziare con i, ma deve essere il più grande possibile
    p = prefisso_piu_lungo(s, i, j)
    return max(p.value, calcola_max(s, p.j, j)) #calcolo il massimo tra il massimo del prefisso e il massimo del resto dell'intervallo

a = scanArray()
b = scanArray()
s = preprocess_max(a, 0, len(a)) #costruzione del segment tree

for k in range(0, len(b), 2):
    i = b[k]
    j = b[k+1]
    print(calcola_max(s, i, j+1), end = " ") #calcolo e stampa del massimo nell'intervallo i, j

