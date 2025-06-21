import sys


inp = "".join(sys.stdin.readlines()).strip().split("\n")[1]
# print(sorted([int(i) for i in inp.split()], reverse=True))
inp = [int(i) for i in inp.split()]
team = inp
sortedTeams = sorted(inp)
# print(sortedTeams)
win = [None] * 16
point = 0
for i, j in zip([0, 1, 3, 7, 15], [1, 3, 7, 15, 16]):
    for k in sortedTeams[i:j]:
        win[team.index(k)] = str(point)
    point += 1

win = " ".join(win)
print(win)
# winList = [3, 3, 4, 3, 1, 3, 3, 0, 2, 3, 2, 2, 1, 3, 2, 3]
# for i in zip(
#     sorted([int(i) for i in inp.split()], reverse=True), sorted(winList, reverse=True)
# ):
#     print(i)
