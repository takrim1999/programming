import sys

# def twoSame(array)


inp = "".join(sys.stdin.readlines()).strip().split("\n")[1:]
for i in inp:
    # print(i)
    a, b, c, d = [int(j) for j in i.split()]
    if a == b == c:
        print("YES")
    elif (a == b) or (b == c) or (a == c):
        print("YES")
    else:
        if abs(a - b) <= d or abs(b - c) <= d or abs(a - c) <= d:
            print("YES")
        else:
            print("NO")
