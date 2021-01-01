from collections import defaultdict
answer = []
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

playsDict = {}
d = {}

for i in range(len(genres)):
    genre = genres[i]
    play = plays[i]
    playsDict[genre] = playsDict.get(genre, 0) + play
    d[genre] = d.get(genre, [0]) + [(play, i)]

print(d)

genreSort = sorted(playsDict.items(), key=lambda x: x[0], reverse=True)

for(genre, totalPlay) in genreSort:
    d[genre] = sorted(d[genre], key=lambda x: (-x[0], x[1]))
    answer += [idx for (play, idx) in d[genre][:2]]

print(answer)

print(playsDict)
print(d)
print(genreSort)