with open("diagnostic") as file:
  binaries = [line.strip() for line in file.readlines()]

#region Part 1
half = int(len(binaries) / 2)
max = pow(2, len(binaries[0])) - 1
gamma = []
for i in range(len(binaries[0])):
  if sum(int(x[i]) for x in binaries) > half:
    gamma.append(1)
  else:
    gamma.append(0)
num = 0
for x in gamma:
  num = 2 * num + x

print(num * (max-num))
#endregion

#region Part 2
half = len(binaries) / 2
oxygen, carbon = [], []
common = 1 if sum(int(x[0]) for x in binaries) >= half else 0

for entry in binaries:
  if int(entry[0]) == common:
    oxygen.append(entry)
  else:
    carbon.append(entry)

i = 1
while len(oxygen) > 1:
  half = len(oxygen) / 2
  common = 1 if sum(int(x[i]) for x in oxygen) >= half else 0
  temp = []
  for item in oxygen:
    if int(item[i]) == common:
      temp.append(item)
  oxygen = temp
  i += 1

i = 1
while len(carbon) > 1:
  half = len(carbon) / 2
  uncommon = 0 if sum(int(x[i]) for x in carbon) >= half else 1
  temp = []
  for item in carbon:
    if int(item[i]) == uncommon:
      temp.append(item)
  carbon = temp
  i += 1

print(int(carbon[0], 2) * int(oxygen[0], 2))
#endregion