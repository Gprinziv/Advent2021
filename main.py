def getInput(input):
  with open(input) as file:
    output = [[int(x) for x in y.strip()] for y in file.readlines()]
  return output

octopodes = getInput("test")