from copy import deepcopy
#Convert the algorithm and image to easily usable objects.
binD = {".":0, 0:".", 1:"#", "#":1}
steps = 50
#region setup
with open("input") as file:
  raw = [x.strip() for x in file.read().split("\n\n")]
  iea = raw[0]
  image = [[binD[x] for x in line] for line in raw[1].split("\n")]

#Extend the border of the image so we can enhance twice.
for i in range(len(image)):
  image[i] = [0 for x in range(steps+1)] + image[i] + [0 for x in range(steps+1)]

for i in range(steps+1):
  image.insert(0, [0 for x in range(len(image[0]))])
  image.append([0 for x in range(len(image[0]))])
#endregion

#region operate on the image
while steps > 0:
  newImage = deepcopy(image)
  for i in range(len(image[0])):
    if image[0][0] == 0:
      newImage[0][i] = binD[iea[0]]
      newImage[-1][i] = binD[iea[0]]  
    else:
      newImage[0][i] = binD[iea[-1]]
      newImage[-1][i] = binD[iea[-1]]

  for j in range(1, len(image)-1):
    if image[0][0] == 0:
      newImage[j][0] = binD[iea[0]]
      newImage[j][-1] = binD[iea[0]]
    else:
      newImage[j][0] = binD[iea[-1]]
      newImage[j][-1] = binD[iea[-1]]

    for i in range(1, len(image[j])-1):
      pixelArray = [image[j-1][i-1], image[j-1][i], image[j-1][i+1], image[j][i-1], image[j][i], \
      image[j][i+1], image[j+1][i-1], image[j+1][i], image[j+1][i+1]]
      pixel = int("".join(str(x) for x in pixelArray), 2)
      newImage[j][i] = binD[iea[pixel]]
  image = newImage
  #endregion
  steps -= 1


for line in image:
  print("".join(binD[x] for x in line))
print()

count = sum(sum(line) for line in image)
print(count)