v = [7, 3, 1, 6, 9, 5, 8, 10, 4, 2]

def selection_sort(v):
    size = len(v)
    for i in range(size - 1):
        min_idx = i
        for j in range(i + 1, size):
            if(v[j] < v[min_idx]):
                min_idx = j
        if(min_idx != i):
            temp = v[i]
            v[i] = v[min_idx]
            v[min_idx] = temp

selection_sort(v)
print(v)
