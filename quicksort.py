#quicksort
def qsort(arr, left, right):
    if (left < right):
        #divide array in two "unequal" parts, smaller elements on left
        pos = part(arr, left, right)
        #sort the left side recursively
        qsort(arr, 0, pos - 1)
        #sort the right
        qsort(arr, pos + 1, right)
    
def part(arr, left, right):
    #array is unsorted, pick the rightmost element as a pivot
    #everything "smaller" than pivot will move to left
    pivot = arr[right]
    #sp points to last element moved
    sp = left - 1
    
    for i in range(left, right):
        if (arr[i] < pivot):
            sp += 1
            (arr[i], arr[sp]) = (arr[sp], arr[i])
    pos = sp + 1
    (arr[pos], arr[right]) = (arr[right], arr[pos])
    return pos
            