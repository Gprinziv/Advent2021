from math import ceil, floor

def snailExplode(n, cur, end):
  tree = ["[", "]", ","]
  pre = n[:cur]
  post = n[end+1:]
  comma = n[cur:end].index(",")
  ex1 = int(n[cur+1:cur+comma])
  ex2 = int(n[cur+comma+1:end])

  #Add ex1 to pre.
  preCur = len(pre) - 1
  while preCur >= 0:
    if pre[preCur] in tree:
      preCur -= 1
    else:
      break
  if preCur > -1:
    prepreCur = preCur-1
    while pre[prepreCur].isnumeric():
      prepreCur -= 1
    ex1 += int(pre[prepreCur+1:preCur+1])
    pre = pre[:prepreCur+1] + str(ex1) + pre[preCur+1:]

  #Add ex2 to post.
  postCur = 0
  while postCur < len(post):
    if post[postCur] in tree:
      postCur += 1
    else:
      break
  if postCur < len(post):
    postpostCur = postCur +1
    while post[postpostCur].isnumeric():
      postpostCur += 1
    ex2 += int(post[postCur:postpostCur])
    post = post[:postCur] + str(ex2) + post[postpostCur:]

  #Now replace the pair with a single zero.
  return pre + '0' + post

def snailReduce(n):
  cur, depth = 0, 0
  doneExploding = False
  while cur < len(n):
    if not doneExploding:
      if n[cur] == "[":
        depth += 1
        if depth > 4:
          end = cur+1
          while n[end] not in ["[", "]"]:
            end += 1
          if n[end] == ']':
            n = snailExplode(n, cur, end)
            cur = -1
            depth = 0
      elif n[cur] == "]":
        depth -= 1
    elif n[cur].isnumeric() and n[cur+1].isnumeric():
      end = cur+2
      while n[end].isnumeric():
        end+=1
      num = int(n[cur:end])
      n = n[:cur] + "[" + str(floor(num/2)) +  "," + str(ceil(num/2)) + "]" + n[end:]
      cur = -1
      depth = 0
      doneExploding = False
    cur += 1
    if cur == len(n) and not doneExploding:
      cur = 0
      doneExploding = True
  return n

def getMagnitude(n):
  cur = 0
  while cur < len(n):
    if n[cur] == '[':
      end = cur+1
      while n[end] not in ["[", "]"]:
        end+=1
      if n[end] == ']':
        comma = n[cur:end].index(",")
        mag = 3 * int(n[cur+1:cur+comma]) + 2 * int(n[cur+comma+1:end])
        n = n[:cur] + str(mag) + n[end+1:]
        cur = -1
    cur += 1
  return n

with open("input") as file:
  raw = [x.strip() for x in file.readlines()]

#region Part 1
"""
snailSum = raw[0]
for line in raw[1:]:
  snailSum = "[" + snailSum + "," + line + "]"
  print("Checking addition: " + snailSum)
  snailSum = snailReduce(snailSum)
  print("Result: " + snailSum + "\n")
print(snailSum)
magnitude = getMagnitude(snailSum)
print(magnitude)
"""
#endregion

#region Part 2
maxMagnitude = 0

for i in range(len(raw)):  
  for j in range(i):
    subSum = snailReduce("[" + raw[i] + "," + raw[j] + "]")
    magnitude = int(getMagnitude(subSum))
    if magnitude > maxMagnitude:
      maxMagnitude = magnitude
  for j in range(i+1, len(raw)):
    subSum = snailReduce("[" + raw[i] + "," + raw[j] + "]")
    magnitude = int(getMagnitude(subSum))
    if magnitude > maxMagnitude:
      maxMagnitude = magnitude

print(maxMagnitude)
#endregion