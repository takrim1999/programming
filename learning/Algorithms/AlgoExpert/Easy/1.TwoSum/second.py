def twoSum(array, sum):
    for i in array:
        if (sum - i) in array and (sum != (sum - i)):
            print(i, sum - i)


twoSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
