def quicksort(array, left, right):
    mid = array[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while array[i] < mid:
            i += 1
        while array[j] > mid:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if left < j:
        quicksort(array, left, j)
    if right > i:
        quicksort(array, i, right)
    return(array)


def mass(a):
    b = []
    for i in a:
        if not b or i != b[-1]:
            b.append(i)
    return(b)


n = int(input())
a = []
for x in range (n):
    tmp1 = list(map(int, input().split()))
    for i in range (tmp1[0], tmp1[1]+1):
        if i not in tmp1:
            tmp1.append(i)
    a = a + tmp1
a = quicksort(a, 0, len(a)-1)
a = mass(a)
print(len(a))
