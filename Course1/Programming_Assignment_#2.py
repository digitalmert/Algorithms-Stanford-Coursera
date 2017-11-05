with open('PATH_TO_FILE') as f:
    lines = [int(x) for x in f.read().splitlines()]


def merge(a, b, cumInv):
    """ Merging two arrays """
    c = []
    inversions = 0
    """ Compute the length of array a and b initially"""
    lenA, lenB = len(a), len(b)
    while lenA != 0 and lenB != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
            """ Counting the length of array a in each iteration with len(a) is likely to make running time quadratic.
                It is enough to decrement the lenA by 1 here"""
            lenA -= 1
        else:
            c.append(b[0])
            b.remove(b[0])
            """ Same logic with lenA applies here """
            lenB -= 1
            inversions = inversions + lenA
    if len(a) == 0:
        c += b
    else:
        c += a
    return c, inversions + cumInv


def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        n = len(arr) / 2
        firstHalf, inv1 = mergeSort(arr[:n])
        secondHalf, inv2 = mergeSort(arr[n:])
        return merge(firstHalf, secondHalf, inv1 + inv2)


result = mergeSort(lines)
print(result[1])
