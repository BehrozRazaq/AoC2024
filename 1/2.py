# pritn hello
with open("1/input.txt", "r") as f:
    data = f.readlines()

left = []
right = {}
for line in data:
    line = line.split()
    if not line:
        break
    
    left.append(int(line[0]))
    if int(line[1]) not in right:
        right[int(line[1])] = 0
    right[int(line[1])] += 1

sim = 0
for l in left:
    if l in right:
        sim += l * right[l]
        continue
print(sim)