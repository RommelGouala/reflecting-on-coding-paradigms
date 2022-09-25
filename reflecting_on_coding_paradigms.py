# make a funtion that will flatten and sort an array of integers in asccecding order

def flat_n_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

print(flat_n_sort([[7, 6], [5, 7]]))