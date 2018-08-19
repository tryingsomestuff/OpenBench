from utils_hack import SPRT

games = 10
for _ in range(1):
    winrate = 0.501
    w = games*winrate
    l = games*(1-winrate)
    print (games, SPRT(w, l, 1, 800, 805))
    games += 10

# Find Threads / Options for the Dev Engine
tokens = "Threads=1 Hash=8".split(' ')
devoptions = ' option.'.join(['']+tokens)

print(devoptions)
