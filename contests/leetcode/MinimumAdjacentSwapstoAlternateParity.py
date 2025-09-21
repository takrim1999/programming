def minSwaps(nums):
    count = 0
    first = 0
    next = 1
    while first < len(nums)-1:
        while nums[first] & 1 == nums[next] & 1:
            count += 1
            next += 1
            if next == len(nums):
                return count
        temp = nums.pop(next)
        nums.insert(first + 1, temp)
        first += 1
        next = first + 1
    return count
print(minSwaps([4,5,6,8]))