def sortedSquaredArray(array):
    sortedArray = [0 for _ in array]
    first = 0
    last = len(array) - 1
    point = len(sortedArray) - 1
    while not (first > last):
        if abs(array[first]) == abs(array[last]):
            sortedArray[point] = array[first] * array[last]
            first += 1
            last -= 1
        elif abs(array[first]) > abs(array[last]):
            sortedArray[point] = array[first] * array[first]
            point -= 1
            first += 1
        elif abs(array[first]) < abs(array[last]):
            sortedArray[point] = array[last] * array[last]
            point -= 1
            last -= 1
        else:
            return False
    return sortedArray


print(sortedSquaredArray([-7, -5, -4, 3, 6, 8, 9]))
