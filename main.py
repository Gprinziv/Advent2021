with open("input") as file:
  raw = file.readlines()
  p1 = int(raw[0][-2])
  p2 = int(raw[1][-1])

#region Part 1
score1, score2, rolls = 0, 0, 0
die= [x+1 for x in range(100)]

firstHalf = True
while score1 < 1000 and score2 < 1000:
    rolls += 3
    temp = die[:3]
    if firstHalf == True:
        p1 = (p1 + sum(temp)) % 10
        score1 += 10 if p1 == 0 else p1
        firstHalf = False
    else:
        p2 = (p2 + sum(temp)) % 10
        score2 += p2
        firstHalf = True
    die = die[3:] + temp

print(rolls * min(score1, score2))
#endregion
#region Part 2

#endregion