with open("depths") as file:
    depths = [int(line.strip()) for line in file.readlines()]

#region Part 1
total = 0
cur = depths[0]
for i in range(1, len(depths)):
    if depths[i] > cur:
        total += 1
    cur = depths[i]
print(total)
#endregion

#region part 2
total = 0
cur = [depths[0], depths[1], depths[2]]
for i in range(3, len(depths)):
    temp = cur[1:] + [depths[i]]
    if sum(temp) > sum(cur):
        total += 1
    cur = temp
print(total)
#endregion