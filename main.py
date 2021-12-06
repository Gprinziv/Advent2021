with open("input") as file:
  lanternfish = [int(x) for x in file.read().split(",")]

days = 0
limit = 256
lanMap = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
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