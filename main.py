with open("vents") as file:
  vents = []
  for line in file.readlines():
    vents.append([int(y) for x in line.strip().split(" -> ") for y in x.split(",")])

#region Part 1
maxX = max([vent[0] for vent in vents] + [vent[2] for vent in vents])
maxY = max([vent[1] for vent in vents] + [vent[3] for vent in vents])
ventMap = [[0 for x in range(maxX + 1)] for y in range(maxY + 1)]
for vent in vents:
  ventX = sorted([vent[0], vent[2]])
  ventY = sorted([vent[1], vent[3]])
  if vent[0] == vent[2]:
    for y in range(ventY[0], ventY[1] + 1):
      ventMap[y][vent[0]] += 1
  elif vent[1] == vent[3]:
    for x in range(ventX[0], ventX[1] + 1):
      ventMap[vent[1]][x] += 1
#region Part 2
#endregion
  else:
    if (vent[0] < vent[2] and vent[1] < vent[3]) or (vent[0] > vent[2] and vent[1] > vent[3]):
      for i in range(ventX[1] - ventX[0] + 1):
        ventMap[ventY[0] + i][ventX[0] + i] += 1
    else:
      for i in range(ventX[1] - ventX[0] + 1):
        ventMap[ventY[0] + i][ventX[1] - i] += 1
#endregion

total = 0
for vent in ventMap:
  for item in vent:
    if item > 1:
      total += 1
  #print(" ".join(str(x) if x > 0 else "-" for x in vent))
print(total)