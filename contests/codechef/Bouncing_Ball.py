import sys


inp = "".join(sys.stdin.readlines()).strip().split("\n")[2::2]

for game in inp:
    # game = [int(_) for _ in game.split()]
    game = game.split()
    if len(game)<=2:
        
    # print(game.count(0))
