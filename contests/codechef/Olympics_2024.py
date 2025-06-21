import sys

listMedal = sys.stdin.readline().split()
print(15 - sum([int(i) for i in listMedal]))
