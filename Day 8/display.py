with open("input") as file:
  displays = [entry.lstrip().strip() for line in file.readlines() for entry in line.split("|")]
  inputs = displays[::2]
  outputs = displays[1::2]
#region Part 1
total = 0
for output in outputs:
  total += sum([0,1][len(digit) in (2, 3, 4, 7)] for digit in output.split(" "))
print(total)
#endregion
#region input
total = 0
for i in range(len(inputs)):
  digits = sorted(inputs[i].split(" "), key=len)
  digiMap = {8:digits[9], 1:digits[0], 7:digits[1], 4:digits[2]}
  digits = digits[3:9]

  for digit in digits:
    if len(digit) == 6 and not all(x in digit for x in digiMap[7]):
      digiMap[6] = digit
      break
  digits.pop(digits.index(digiMap[6]))

  for digit in digits:
    if len(digit) == 6 and not all(x in digit for x in digiMap[4]):
      digiMap[0] = digit
      break
  digits.pop(digits.index(digiMap[0]))
  
  digiMap[9] = digits[3]
  digits.pop(3)

  for digit in digits:
    if not all(x in digiMap[9] for x in digit):
      digiMap[2] = digit
    elif not all(x in digiMap[6] for x in digit):
      digiMap[3] = digit
    else:
      digiMap[5] = digit
#endregion
#region output
  output = outputs[i].split(" ")
  for j in range(len(output)):
    for key, val in digiMap.items():
      if all(x in val for x in output[j]) and len(val) == len(output[j]):
        total += (key * pow(10, 3-j))
print(total)
#endregion