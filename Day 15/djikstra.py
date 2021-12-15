from collections import defaultdict
import heapq
#Thanks to reddit user mebeim for their writeup of Djikstra's Algorithm.
#Elements of that code were used here.

def getAdjacent(point, end):
  for a, b in ((0,1), (0,-1), (1,0), (-1,0)):
    x, y = point[0] + a, point[1] + b
    if 0 <= x <= end[0] and 0 <= y <= end[1]:
      yield x, y

with open("test2") as file:
  raw = [[int(x) for x in line.strip()] for line in file.readlines()]

#region part 2 modifier
maxX = len(raw[0])
maxY = len(raw)

for line in raw:
  for i in range(1, 5):
    line += [9 if x+i==9 else (x+i)%9 for x in line[:maxX]]
for i in range(1, 5):
  for line in raw[:maxY]:
    raw.append([9 if x+i==9 else (x+i)%9 for x in line])
#endregion

distances = defaultdict(lambda: float('inf'), {(0,0):0})
end = (len(raw[0]) - 1, len(raw) - 1)
toSearch = [(0, (0,0))]
visited = set()

while toSearch:
  distance, node = heapq.heappop(toSearch)
  if node == end:
    print("finished! Distance is " + str(distance))
    break
  if node in visited:
    continue
  visited.add(node)
  for point in getAdjacent(node, end):
    if point in visited:
      continue
    x, y = point
    newdist = distance + raw[y][x]
    if newdist < distances[point]:
      distances[point] = newdist
      heapq.heappush(toSearch, (newdist, point))