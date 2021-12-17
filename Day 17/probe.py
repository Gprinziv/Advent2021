with open("input") as file:
  raw = file.read().replace("..", '=').replace(": ", "=").replace(", ", "=").split("=")
  minX, maxX, minY, maxY = int(raw[2]), int(raw[3]), int(raw[5]), int(raw[6])
y = -(minY + 1)

x = 0
while not minX <= sum(range(x + 1)) <= maxX:
    x+=1

print("Highest possible Y value: " + str(sum(range(y + 1))))


possibleX = []
for posX in range(x, maxX + 1):
  i = 0
  while i < x:
    if minX <= sum(range(posX - i, posX + 1)) <= maxX:
      possibleX.append((i + 1, posX))
    i += 1

possibleY = []      
for posY in range(minY, y+1):
  curY = posY
  i = 1
  while curY >= minY:
    if minY <= curY <= maxY:
      possibleY.append((i, posY))
    curY += (posY - i)
    i += 1

possible = set()
for posX in possibleX:
  for posY in possibleY:
    if posX[0] == posY[0]:
      possible.add((posX[1], posY[1]))
    elif posX[0] == x:
      if posY[0] > posX[0]:
        possible.add((posX[1], posY[1]))

print(len(possible))