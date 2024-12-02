with open("1/input.txt", "r") as f:
    data = f.readlines()

left = []
right = []
for line in data:
    line = line.split()
    if not line:
        break

    left.append(int(line[0]))
    right.append(int(line[1]))

left.sort()
right.sort()

dist = 0
for l, r in zip(left, right):
    dist += abs(l - r)

print(dist)
