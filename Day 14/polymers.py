with open("input") as file:
  raw = file.read().split("\n\n")
  polymer = raw[0]
  inserts = {x.split(" -> ")[0] : x.split(" -> ")[1] for x in raw[1].split("\n")}


#region part 1
"""
for loop in range(10):
  i = 0
  while i < len(polymer):
    if polymer[i:i+2] in inserts:
      polymer = polymer[:i+1] + inserts[polymer[i:i+2]] + polymer[i+1:]
      i += 1
    i += 1

most = max(set(polymer), key = polymer.count)
least = min(set(polymer), key = polymer.count)
print(polymer.count(most)-polymer.count(least))
#print(polymer)
"""
#endregion
#region part 2
polydict = {}
counts = {x:polymer.count(x) for x in polymer}
print(counts)
for i in range (len(polymer) - 1):
  base = polymer[i:i+2]
  polydict[base] = 1 if base not in polydict else polydict[base] + 1

for i in range(40):
  tempdict = polydict.copy()
  for key, count in polydict.items():
    counts[inserts[key]] = count if inserts[key] not in counts else counts[inserts[key]] + count
    base1 = key[0] + inserts[key]
    base2 = inserts[key] + key[1]
    if tempdict[key] == count:
      tempdict.pop(key)
    else:
      tempdict[key] -= count
    tempdict[base1] = count if base1 not in tempdict else tempdict[base1] + count
    tempdict[base2] = count if base2 not in tempdict else tempdict[base2] + count
  polydict = tempdict

most = max(val for val in counts.values())
least = min(val for val in counts.values())
print(most-least)

print(counts)
#endregion