def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    perms = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            perms.append([m]+p)
    return perms


print(permutation(['A', 'B', 'C']))
# c) jezeli lista jest pusta nie isnieja permutacje
# jezeli lista sklada sie z tylko jednego elementu ta lista
# jest jedyna permutacja
# d) lst- lista obiektow z ktorych skladaja sie permutacje
# perms - lista wszystkich mozliwych permutacji
# e) m- pierwszy element permutacji
# remLst- pozostale elementy permutacji
# f) lst np ['A','B','C']
#  i np 1
# m np "A"
# remLst np "C"
# g) tworzenie szystkich mozliwych kombinacji elementow z listy
# remLst
