with open("input") as file:
  paths = [x.strip().split('-') for x in file.readlines()]

#region generate starting caves & remove start paths
caves = []
for path in paths:
  if 'start' in path:
    if path[0] == 'start':
      caves.append([0] + path)
    else:
      caves.append([0] + path[::-1])

cur = 0
while cur < len(paths):
  if "start" in paths[cur]:
    paths.pop(cur)
  else:
    cur += 1
#endregion  
  
while not all([cave[-1] == "end" for cave in caves]):
  newCaves = []

  for cave in caves:
    toAdd = []
    reAdd = []
    endpoint = cave[-1]
    if endpoint != "end":
      for path in paths:
        if path[0] == endpoint:
          if path[1].isupper() or path[1] not in cave:
            toAdd.append(path[1])
          elif cave[0] == 0 and path[1] in cave:
            reAdd.append(path[1])
        elif path[1] == endpoint:
          if path[0].isupper() or path[0] not in cave:
            toAdd.append(path[0])
          elif cave[0] == 0 and path[0] in cave:
            reAdd.append(path[0])

    if toAdd or reAdd:
      for add in toAdd:
        newCaves.append(cave + [add])
      for add in reAdd:
        newCaves.append([1] + cave[1:] + [add])
    elif endpoint == 'end':
      newCaves.append(cave)
  caves = newCaves

#for cave in caves:
#  print(cave)
print(len(caves))