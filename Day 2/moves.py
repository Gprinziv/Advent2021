with open("instructions") as file:
  moves = [line.strip().split(" ") for line in file.readlines()]

#region Part 1
position = [0,0]
for instruction in moves:
    if instruction[0] == "forward":
        position[0] += int(instruction[1])
    elif instruction[0] == "down":
        position[1] += int(instruction[1])
    else:
        position[1] -= int(instruction[1])
        if position[1] < 0:
            position[1] = 0
print(position)
print(position[0] * position[1])
#endregion

#region Part 2
position = [0,0]
aim = 0
for instruction in moves:
    if instruction[0] == "forward":
        position[0] += int(instruction[1])
        position[1] += int(instruction[1]) * aim
        if position[1] < 0:
            position[1] = 0
    elif instruction[0] == "down":
        aim += int(instruction[1])
    else:
        aim -= int(instruction[1])
print(position)
print(position[0] * position[1])
#endregion