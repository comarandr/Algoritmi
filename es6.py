#Implementare un algoritmo di riecerca dicotomica su array ordinati di interi:
#Il programma deve
def ricerca_dicotomica(a, key):
    i = 0
    j = len(a)
    while i < j:
        m = (i + j) // 2 #/ divisione, // divisione intera
        if key == a[m]:
            return m
        elif key < a[m]: #cerco nella parte sx
            j = m
        else:
            i = m + 1
            return -1


def ricerca2(a, key,i, j): #
    if j - i <= 0:
        return -1
    m = (i + j) // 2
    if key == a[m]:
        return m
    elif key < a[m]: #cerco nella parte sx
        return ricerca2(a, key, i, m)
    else:
        return ricerca2(a, key, m+1, j)


line = input()
tokens = line.split(" ")
a = [int(x) for x in tokens if x != ""]
#print("Inserire un array ordinato: ")

print("inserire una chiave:")
key = int(input())

pos = ricerca_dicotomica(a, key)
pos2 = ricerca2(a, key, 0, len(a))
print("la chiave sta in posizione ", pos)
#print("la chiave sta in posizione ", pos2)
print(pos2)
    





