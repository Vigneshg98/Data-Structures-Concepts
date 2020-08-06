def merge(inp, start, mid, end) :
    n1 = mid - start + 1
    n2 = end - mid

    L = [0]*n1
    R = [0]*n2

    for i in range(n1) :
        L[i] = inp[start+i]

    for i in range(n2) :
        R[i] = inp[mid+1+i]

    i, j, k = 0, 0, 1

    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            inp[k] = L[i] 
            i += 1
        else: 
            inp[k] = R[j] 
            j += 1
        k += 1
        
    while i < n1: 
        inp[k] = L[i] 
        i += 1
        k += 1

    while j < n2: 
        inp[k] = R[j] 
        j += 1
        k += 1


def mergeSort(inp, start, end) :
    if start < end :
        mid = (start+end)//2
        mergeSort(inp, start, mid)
        mergeSort(inp, mid+1, end)
        merge(inp, start, mid, end)

inp = list(map(int, input().split()))
n = len(inp)
mergeSort(inp, 0, n-1)
print(inp)
