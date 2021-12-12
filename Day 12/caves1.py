with open("input") as file:
  paths = [x.strip().split('-') for x in file.readlines()]

caves = []
for path in paths:
  if 'start' in path:
    if path[0] == 'start':
      caves.append(path)
    else:
      caves.append(path[::-1])
    
while not all([cave[-1] == "end" for cave in caves]):
  newCaves = []

  for cave in caves:
    toAdd = []
    endpoint = cave[-1]
    if endpoint != "end":
      for path in paths:
        if path[0] == endpoint:
          if path[1].isupper() or path[1] not in cave:
            toAdd.append(path[1])
        elif path[1] == endpoint:
          if path[0].isupper() or path[0] not in cave:
            toAdd.append(path[0])

    if toAdd:
      for add in toAdd:
        newCaves.append(cave + [add])
    else:
      if endpoint == 'end':
        newCaves.append(cave)
  caves = newCaves

for cave in caves:
  print(cave)
print(len(caves))