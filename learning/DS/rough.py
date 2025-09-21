# array1 = [1,2,4]
# array2 = [1,3,4]
array1 = []
array2 = [0]

pointer1 = 0
pointer2 = 0

final_array = []

while len(array1) != pointer1 and len(array2) != pointer2:
    if array1[pointer1] < array2[pointer2]:
        final_array.append(array1[pointer1])
        pointer1 += 1
    elif array1[pointer1] > array2[pointer2]:
        final_array.append(array2[pointer2])
        pointer2 += 1
    else:
        final_array.append(array1[pointer1])
        final_array.append(array2[pointer2])
        pointer1 += 1
        pointer2 += 1
if pointer1<len(array1):
    while  len(array1) != pointer1:
        final_array.append(array1[pointer1])
        pointer1 += 1
if pointer2<len(array2):
    while  len(array2) != pointer2:
        final_array.append(array2[pointer2])
        pointer2 += 1
print(final_array)