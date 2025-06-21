def twoSum(array, sum):
    first = 0
    last = len(array) - 1
    array.sort()
    # print(array)
    while first != last:
        if array[first] + array[last] == sum:
            print(array[first], array[last])
            break
        elif (array[first] + array[last]) > sum:
            last -= 1
        elif (array[first] + array[last]) < sum:
            first += 1


twoSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
