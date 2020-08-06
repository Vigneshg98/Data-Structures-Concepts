def partition(inp, start, end) :
    i = start+1
    piv = inp[start]

    for j in range(start+1, end+1) :
        if inp[j] < piv :
            inp[i], inp[j] = inp[j], inp[i]
            i+=1
    inp[start], inp[i-1] = inp[i-1], inp[start]
    return i-1

def quickSort(inp, start, end) :
    if start < end :
        piv = partition(inp, start, end)
        quickSort(inp, start, piv-1)
        quickSort(inp, piv+1, end)

inp = list(map(int, input().split()))
n = len(inp)
quickSort(inp, 0, n-1)
print(inp)
