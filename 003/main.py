S = input()

c = 0
cmax = -1
for s in S:
  if s in ['A', 'C', 'G', 'T']:
    c += 1
  else:
    if c > cmax:
      cmax = c
    c = 0

if c > cmax:
  cmax = c
c = 0

print(cmax)