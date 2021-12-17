def literal(packet):
  number, cur = "", 0
  while packet[cur] == '1':
    number += packet[cur+1:cur+5]
    cur += 5
  number += packet[cur+1:cur+5]
  #print("Literal contents: " + number)
  #print("As an integer: " + str(int(number, 2)))
  return cur + 5

def unpack(packet):
  versions = []
  processQueue = [1]

  while processQueue:  
    numItems = processQueue.pop()
    c = 0
    versions.append(int(packet[:3], 2))
    tid = int(packet[3:6], 2)

    while numItems > 0:
      if tid == 4:
        c += literal(packet[6:]) + 6
        packet = packet[6:]
      else:
        ltid = bits[6]
        if ltid == '1':
          #suspend the current loop on the string and pick it back up once this operator packet has been cleared.
          pass
        else:
          length = 22 + int(packet[7:22], 2)
          versions += unpack(packet[22:length])
          packet = packet[length:]
      numItems -= 1
  return versions

with open("test2") as file:
  bits = bin(int(file.read(), 16))[2:]

versions = unpack(bits)
print(versions)