b = [6, 2, 7, 1, 5]


def bubblesort_min(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] < a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
    return a


print(bubblesort_min(b))
