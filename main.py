with open("test") as file:
  paths = [x.strip().split('-') for x in file.readlines()]