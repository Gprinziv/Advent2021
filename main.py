with open("test") as file:
  raw = file.read().replace("..", '=').replace(": ", "=").replace(", ", "=").split("=")
  minX, maxX, minY = int(raw[2]), int(raw[3]), int(raw[5])
maxY = -(minY + 1)

print(raw)
x = 0
while not minX <= sum(range(x + 1)) <= maxX:
    x+=1

possibleX = []
for posX in range(x, maxX + 1):
    i = 0:
    while i < 

print("Minimum X velocity: " + str(x))
print("Maximim X velocity: " + str(maxX))
print("Minimum Y velocity: " + str(minY))
print("Maximim Y velocity: " + str(maxY))

print("Highest possible Y value: " + str(sum(range(maxY + 1))))