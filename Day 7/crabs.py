with open("Day 7\input") as file:
  crabMap = {}
  for crab in [int(x) for x in file.read().split(",")]:
    if crab not in crabMap:
      crabMap[crab] = 1
    else:
      crabMap[crab] += 1

best1 = sum(crabMap[crab] * crab for crab in crabMap)
best2 = sum(crabMap[crab] * sum(range(crab + 1)) for crab in crabMap)
for i in range(1, max(crabMap) + 1):
  total1 = sum(crabMap[crab] * abs(crab - i) for crab in crabMap)
  if total1 < best1:
    best1 = total1

  total2 = sum(crabMap[crab] * sum(range(abs(crab - i) + 1)) for crab in crabMap)
  if total2 < best2:
    best2 = total2

print(best1)
print(best2)