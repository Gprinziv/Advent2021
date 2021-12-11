def getInput(input):
  with open(input) as file:
    output = [[int(x) for x in y.strip()] for y in file.readlines()]
  return output

def flash(x, y):
  if x == 0:
    toFlash = [(x,y-1), (x+1,y-1), (x+1,y), (x,y+1), (x+1,y+1)]
    if y == 0:
      toFlash = toFlash[2:]
    elif y == 9:
      toFlash = toFlash[:3]
  elif x == 9:
    toFlash = [(x-1,y-1), (x,y-1), (x-1,y), (x-1,y+1), (x,y+1)]
    if y == 0:
      toFlash = toFlash[2:]
    elif y == 9:
      toFlash = toFlash[:3]
  elif y == 0:
    toFlash = [(x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]
  elif y == 9:
    toFlash = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1,y)]
  else:
    toFlash = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]
  return toFlash

def part1(octopodes, turns):
  total = 0
  for i in range(turns):
    for y in range(10):
      for x in range(10):
        octopodes[y][x] += 1

    for y in range(10):
      for x in range(10):
        if type(octopodes[y][x]) == int and octopodes[y][x] > 9:
          octopodes[y][x] = 'a'
          total += 1
          flashed = flash(x, y)
          while flashed:
            (i, j) = flashed.pop()
            if type(octopodes[j][i]) == int:
              octopodes[j][i] += 1
              if octopodes[j][i] > 9:
                octopodes[j][i] = 'a'
                total += 1
                flashed += flash(i, j)
    
    for y in range(10):
      for x in range(10):
        if octopodes[y][x] == 'a':
          octopodes[y][x] = 0
  """
  print("After the flash")
  for line in octopodes:
    print(line)
  print(total)
  """
  return total

def part2(octopodes):
  step = 0
  while True:
    for y in range(10):
      for x in range(10):
        octopodes[y][x] += 1

    for y in range(10):
      for x in range(10):
        if type(octopodes[y][x]) == int and octopodes[y][x] > 9:
          octopodes[y][x] = 'a'
          flashed = flash(x, y)
          while flashed:
            (i, j) = flashed.pop()
            if type(octopodes[j][i]) == int:
              octopodes[j][i] += 1
              if octopodes[j][i] > 9:
                octopodes[j][i] = 'a'
                flashed += flash(i, j)
    step += 1
    if all(x == 'a' for line in octopodes for x in line):
      return step

    for y in range(10):
      for x in range(10):
        if octopodes[y][x] == 'a':
          octopodes[y][x] = 0

octopodes = getInput("input")
#print(part1(octopodes, 100))
print(part2(octopodes))
for line in octopodes:
  print(line)