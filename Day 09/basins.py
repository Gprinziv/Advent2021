with open("input") as file:
  heightmap = [line.strip() for line in file.readlines()]

def part1():
  lows = []
  #region first row
  if all(heightmap[0][0] < x for x in [heightmap[1][0], heightmap[0][1]]):
    lows.append(heightmap[0][0])
  for i in range(1, len(heightmap[0]) - 1):
    if all(heightmap[0][i] < x for x in [heightmap[0][i-1], heightmap[1][i], heightmap[0][i+1]]):
      lows.append(heightmap[0][i])
  if all(heightmap[0][-1] < x for x in [heightmap[1][-1], heightmap[0][-2]]):
    lows.append(heightmap[0][-1])
  #endregion
  #region middle
  for j in range(1, len(heightmap) - 1):
    if all(heightmap[j][0] < x for x in [heightmap[j-1][0], heightmap[j+1][0], heightmap[j][1]]):
      lows.append(heightmap[j][0])
    for i in range(1, len(heightmap[j]) - 1):
      if all(heightmap[j][i] < x for x in [heightmap[j][i-1], heightmap[j][i+1], heightmap[j+1][i], heightmap[j-1][i]]):
        lows.append(heightmap[j][i])
    if all(heightmap[j][-1] < x for x in [heightmap[j-1][-1], heightmap[j+1][-1], heightmap[j][-2]]):
      lows.append(heightmap[j][-1])
  #endregion
  #region last row
  if all(heightmap[-1][0] < x for x in [heightmap[-2][0], heightmap[-1][1]]):
    lows.append(heightmap[-1][0])
  for i in range(1, len(heightmap[0]) - 1):
    if all(heightmap[-1][i] < x for x in [heightmap[-1][i-1], heightmap[-2][i], heightmap[-1][i+1]]):
      lows.append(heightmap[-1][i])
  if all(heightmap[-1][-1] < x for x in [heightmap[-2][-1], heightmap[-1][-2]]):
    lows.append(heightmap[-1][-1])
  #endregion
  total = 0
  for low in lows:
    total += int(low) + 1
  print(total)

def makeBasin(x, y):
  toModify = [(x, y)]
  count = 0
  while toModify:
    mod = toModify.pop(0)
    if heightmap[mod[1]][mod[0]] != '9':
      heightmap[mod[1]] = heightmap[mod[1]][:mod[0]] + '9' + heightmap[mod[1]][mod[0]+1:]
      count += 1

    toCheck = [(mod[0] + 1, mod[1]), (mod[0] - 1, mod[1]), (mod[0], mod[1] - 1), (mod[0], mod[1] + 1)]
    if mod[0] == 0:
      toCheck.pop(1)
      if mod[1] == 0:
        toCheck.pop(1)
      elif mod[1] == len(heightmap) - 1:
        toCheck.pop(2)
    elif mod[0] == len(heightmap[0]) - 1:
      toCheck.pop(0)
      if mod[1] == 0:
        toCheck.pop(1)
      elif mod[1] == len(heightmap) - 1:
        toCheck.pop(2)
    else:
      if mod[1] == 0:
        toCheck.pop(2)
      elif mod[1] == len(heightmap) - 1:
        toCheck.pop(3)
    for check in toCheck:
      if heightmap[check[1]][check[0]] != '9':
        toModify.append(check)

  return count

def part2():
  counts = []
  for j in range(len(heightmap)):
    for i in range(len(heightmap[0])):
      if int(heightmap[j][i]) in range(9):
        counts.append(makeBasin(i, j))
  counts = sorted(counts)[-3:]
  total = 1
  for count in counts:
    total *= count
  print(total)

part1()
part2()