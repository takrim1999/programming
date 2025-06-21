import sys

_ = sys.stdin.read().strip().split()[1:]
for num in _:
    num = list(num[::-1])
    # print(num)
    point = 0
    flag = True
    while flag:
        if point == len(num):
            num.append("0")
            flag = False
        if int(num[point]) + 1 == 10:
            num[point] = "0"
            point += 1
        else:
            num[point] = str(int(num[point]) + 1)
            flag = False
    print("".join(num[::-1]))
