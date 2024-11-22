##non efficiente, Theta (n^2)
def majority(a):
    for i in range(len(a)):
        count = 0
        for j in range(len(a)):
            if a[i] == a[j]:
                count += 1
        if count > len(a) // 2:
            return a[i] 
    return None

def majority2(a): #tempo lineare
    #trovo il candidato migliore e lo metto in c
    c = None
    k = 0
    for i in range(len(a)):
        if k == 0:
            c = a[i]
        if c == a[i]:
            k += 1
        else:
            k -= 1
        if k == 0:
            c = None
    #inoltre se il candidato corrente in posizione 
    # controllo che il candidato vada bene
    count = 0
    for i in range(len(a)):
        if a[i] == c:
            count += 1
    if count > len(a) // 2:
        return c
    else:
        return None

a = [int(x) for x in input().split(" ") if x]
c = majority(a)
if c != None:
    print(c)
else:
    print("No majority element")

#