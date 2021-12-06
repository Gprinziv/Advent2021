with open("test") as file:
  lanternfish = [int(x) for x in file.read().split(",")]

days = 0
limit = 256
lanMap = {i:0 for i in range(9)}
print(lanMap)
for fish in lanternfish:
  lanMap[fish] += 1
while days <= limit:
  zeroDay = lanMap[0]
  for i in range(8):
    lanMap[i] = lanMap[i+1]
  lanMap[6] += zeroDay
  lanMap[8] = zeroDay
  days += 1
print(sum([lanMap[i] for i in range(8)]))