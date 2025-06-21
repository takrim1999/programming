def tournamentWinner(matches, results):
    winner = {}
    for i, j in zip(matches, results):
        team = i[1 - j]
        if team in winner:
            winner[team] += 3
        else:
            winner[team] = 3
    return max(winner)


print(
    tournamentWinner([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1])
)
