def nonConstructibleChange(coins):
    coins.sort()
    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        else:
            currentChangeCreated += coin

    return currentChangeCreated


print(nonConstructibleChange([1, 2, 1, 4]))
[5, 7, 1, 1, 2, 3, 22]
