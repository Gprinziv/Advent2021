with open("bingo") as file:
  raw = file.readlines()
  numbers = [int(x) for x in raw[0].strip().split(",")]
  boards, board = [], []
  for i in range(2, len(raw)):
    if raw[i] == "\n":
      boards.append(board)
      board = []
    else:
      board.append([int(x) for x in raw[i].strip().split()])
  boards.append(board)

def checkForWinners():
  index = 0
  while index < len(boards):
    remove = False
    for i in range(5):
      if all([x[i] == "x" for x in boards[index]]) or all([x == "x" for x in boards[index][i]]):
        remove = True

    if remove:
      boards.pop(index)
    else:
      index += 1

def playBingo():
  round = 1
  while numbers:
    current = numbers.pop(0)
    print("Round " + str(round) + " || Pulled number is... " + str(current) + "! " + str(len(numbers)) + " numbers remain")
    winner = False
    for board in boards:
      for line in board:
        if current in line:
          index = line.index(current)
          line[index] = "x"
          if all([x == "x" for x in line]) or all([x[index] == "x" for x in board]):
            winner = [boards.index(board), current]
    if winner:
      return winner
    round += 1

def printBoard(index = None):
  print()
  print("Printing board: " + (str(index + 1) if index != None else "all"))
  if not index:
    for board in boards:
      for line in board:
        print(" ".join([str(x).ljust(2) for x in line]))
      print()
  else:
    for line in boards[index]:
      print(" ".join([str(x).ljust(2) for x in line]))

#region Part 1
"""
winner = playBingo()
total = []
for line in boards[winner[0]]:
  for item in line:
    if type(item) == int:
      total.append(item)
score = sum(total) * winner[1]
print(score)
"""
#endregion

#region Part 2
while len(boards) > 1:
  playBingo()
  checkForWinners()
  print(str(len(boards)) + " board" + ("s" if len(boards) > 1 else "") + " remain" + ("s" if len(boards) == 1 else "") + ".")
printBoard(0)
losingBoard = playBingo()
total = []
for line in boards[0]:
  for item in line:
    if type(item) == int:
      total.append(item)
score = sum(total) * losingBoard[1]
print(score)
#endregion