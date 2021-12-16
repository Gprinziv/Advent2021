def literal(packet):
  cur, number = 0, ""
  while packet[cur] == '1':
    number += packet[cur+1:cur+5]
    cur += 5
  number += packet[cur+1:cur+5]
  print("Literal contents: " + number)
  print("As an integer: " + str(int(number, 2)))
  return number

def operator(packet):
  return

def idpacket(packet):
  return

with open("test") as file:
  bits = bin(int(file.read(), 16))[2:]

toProcess = [bits]
versions = []

while toProcess:
  packet = toProcess.pop(0)
  ver = int(packet[:3], 2)
  versions.append(vid)
  tid = int(packet[3:6], 2)
  lid = packet[6]
  print(tid)
  if tid == 4:
    literal(packet[6:])
  elif lid == '1':
    pass
  else:
    pass
