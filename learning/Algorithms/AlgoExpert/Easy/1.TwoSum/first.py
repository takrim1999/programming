# algorithm for my first implementation is simple.
# just going to traverse full list. and trying to sum
# with other elements except that one. if sum found to be 10
# returing those 2 elements.


def twoSum(array, sum):
    length = len(array)
    for i in range(length):
        for j in range(length):
            if i < j:
                # print(array[i], array[j])
                if (array[i] + array[j]) == sum:
                    print(array[i], array[j])


twoSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
