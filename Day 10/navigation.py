with open("input") as file:
  navigation = [x.strip() for x in file.readlines()]

def findCorrution(line):
  opens = ("(", "[", "{", "<")
  closes = {")":"(", "]":"[", "}":"{", ">":"<"}
  queue = []
  for i in range(len(line)):
    if line[i] in opens:
      queue.append(line[i])
    else:
      if closes[line[i]] == queue[-1]:
        queue.pop()
      else:
        return line[i]
  return None

def part1():
  points = {")": 3, "]": 57, "}": 1197, ">":25137}
  corruptions =  []
  for line in navigation:
    illegalChar = findCorrution(line)
    if illegalChar:
      corruptions.append(illegalChar)
  total = 0
  for character in points:
    total += corruptions.count(character) * points[character]
  return total

def findIncomplete(line):
  opens = {"(":")", "[":"]", "{":"}", "<":">"}
  closes = {")":"(", "]":"[", "}":"{", ">":"<"}
  queue = []
  for i in range(len(line)):
    if line[i] in opens:
      queue.append(line[i])
    else:
      if closes[line[i]] == queue[-1]:
        queue.pop()
      else:
        return None
  return [opens[x] for x in queue[::-1]]

def findScore(incomplete):
  points = {")":1, "]":2, "}":3, ">":4}
  cur = 0
  score = 0
  while cur < len(incomplete):
    score *= 5
    score += points[incomplete[cur]]
    cur += 1
  return score

def part2():
  scores = []
  for line in navigation:
    incomplete = findIncomplete(line)
    if incomplete:
      scores.append(findScore(incomplete))
  scores.sort()
  return scores[(len(scores) - 1) // 2]


print(part1())
print(part2())