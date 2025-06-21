def validateSubsequence(array, subarray):
    arrayPointer = 0
    subarrayPointer = 0
    while arrayPointer != len(array):
        # print(array[arrayPointer])
        if array[arrayPointer] == subarray[subarrayPointer]:
            subarrayPointer += 1
        arrayPointer += 1
    return subarrayPointer == len(subarray)


print(validateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
