def insertion_sort(array1):
    for j in range(1, len(array1)):
        key = array1[j]
        k = j - 1

        while k>= 0 and key < array1[k]:
            array1[k + 1] = array1[k]
            k = k - 1


        array1[k + 1] = key


array1 = [9, 8, 6, 7, 1]
print("Unsorted Array:", array1)
insertion_sort(array1)
print('Sorted Array: ', array1)



