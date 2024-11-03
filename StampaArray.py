def printArray(a):
    print(a, end = " ")
    
def scanArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens