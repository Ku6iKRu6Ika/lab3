from random import shuffle
def bubbleSort(arr, swap):
    sorted = False
    while(not sorted):
        sorted = True
        
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                swap(i, i+1)
                sorted = False
    return

def merge(arr, n1, n2, m1, m2):
    res = [0 for i in range(m2-n1+1)]
    a = n1
    b = m1
    for i in range(len(res)):
        if(a == n2+1):
            res[i] = arr[b]
            b += 1
            continue
        elif(b == m2+1):
            res[i] = arr[a]
            a += 1
            continue
        else: 
            res[i] = min(arr[a], arr[b])
        if(arr[a] == res[i]):
            a += 1
        elif(arr[b] == res[i]):
            b += 1
    return res
        

def mergeSort(arr, swap):
    n = 1
    while(n<len(arr)):
        n*=2
        for i in range(0, len(arr), n):
            n1 = i
            n2 = i+n//2-1
            if(n2>=len(arr)): continue
            m1 = i+n//2
            m2 = min(i+n-1, len(arr)-1)
            res = merge(arr, n1, n2, m1, m2)
            for i in range(n1, m2):
                swap(i, arr.index(res[i-n1], i, m2+1))

        
    return

def test(sort, arr = []):
    global _swaps
    def swap(n1, n2):
        global _swaps
        arr[n1], arr[n2] = arr[n2], arr[n1]
        _swaps += 1
    _swaps = 0
    
    if(not arr):
        arr = list(range(100))
        shuffle(arr)
    orig = sorted(arr.copy())
    sort(arr, swap)

    return (arr == orig, _swaps)

    

if __name__ == "__main__":
    arr = list(range(500))
    shuffle(arr)

    print("{0:>15}:   Working - {1}, Required {2:>8} swaps".format("BubbleSort", *test(bubbleSort, arr.copy())))
    print("{0:>15}:   Working - {1}, Required {2:>8} swaps".format("MergeSort", *test(mergeSort, arr.copy())))