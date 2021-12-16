with open("test") as file:
  bits = bin(int(file.read(), 16))[2:]

ver = int(bits[:3], 2)
tid = int(bits[3:6], 2)
lid = bits[7]

if tid == 4:
  print("Yay!")
else:
  pass

print(ver)
print(pid)
