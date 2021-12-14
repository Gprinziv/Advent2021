with open("input") as file:
  raw = file.read().split("\n\n")
  points = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in raw[0].split("\n")]
  folds = [(x.split("=")[0][-1], int(x.split("=")[1])) for x in raw[1].split("\n")]

maxX, maxY = 0, 0
for point in points:
  maxX = point[0] if point[0] > maxX else maxX
  maxY = point[1] if point[1] > maxY else maxY
grid = [["." for x in range(maxX + 1)] for y in range(maxY + 1)]

try:
  for p in points:
    grid[p[1]][p[0]] = '#'
except IndexError:
  print("Index error at " + str(p))

for fold in folds:
  val = fold[1]
  if fold[0] == 'x':
    print("Folding along x = " + str(val))
    for y in range(len(grid)):
      for x in range(1, len(grid[y]) - val):
        if grid[y][val + x] == "#":
          grid[y][val - x] = "#"
      grid[y] = grid[y][:val]
  else:
    print("Folding along y = " + str(val))
    for y in range(1, len(grid) - val):
      for x in range(len(grid[0])):
        if grid[val + y][x] == '#':
          grid[val - y][x] = '#'
    grid = grid[:val]

count = sum(x.count("#") for x in grid)
print(count)

print("Done!")
for line in grid:
  print("".join(line))