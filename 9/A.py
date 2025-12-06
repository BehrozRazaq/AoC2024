data = "12345"
files = {}
j = -1
latest_id = 0
for i in range(len(data)):
    amount = int(data[i])
    is_file = i % 2 == 0
    if is_file:
        j += 1
        char = str(j)
    else:
        char = "."
    for id in range(latest_id, latest_id + amount):
        files[id] = char

    latest_id += amount

print(files)
for right in reversed(files.keys()):
    for left in files.keys():
        if left >= right:
            break
        if left < right and files[left] == "." and files[right] != ".":
            files[left] = files[right]
            files[right] = "."
            print(files)
            break

check_sum = 0
for k, v in files.items():
    if v == ".":
        continue

    check_sum += k * int(v)

print(check_sum)
