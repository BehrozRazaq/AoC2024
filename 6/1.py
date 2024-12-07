with open("6/input.txt", "r") as f:
    data = f.readlines()

guard = {"pos": (0, 0), "dir": (-1, 0)}

grid = []
visited = []
for r, line in enumerate(data):
    row = []
    f_row = []
    line = line[:-1] if line[-1] == "\n" else line
    for c, char in enumerate(line):
        f_row.append(False)
        if char == "#":
            row.append(True)
            continue
        if char == "^":
            f_row[-1] = True
            guard["pos"] = (r, c)
        row.append(False)
    visited.append(f_row)
    grid.append(row)


out_of_grid = lambda ax: ax < 0 or ax >= len(grid)
move = lambda a: (a["pos"][0] + a["dir"][0], a["pos"][1] + a["dir"][1])


def turn(n_turns):
    possible_turns = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    return possible_turns[n_turns % 4], n_turns + 1


def move_guard(n_turns):
    if out_of_grid(guard["pos"][0]) or out_of_grid(guard["pos"][1]):
        return False, n_turns
    pot_r, pot_c = move(guard)
    if out_of_grid(pot_r) or out_of_grid(pot_c):
        guard["pos"] = (pot_r, pot_c)
        return False, n_turns
    if grid[pot_r][pot_c]:
        guard["dir"], n_turns = turn(n_turns)
        return True, n_turns
    else:
        guard["pos"] = (pot_r, pot_c)
        visited[pot_r][pot_c] = True
        return True, n_turns


import time

st = time.time()
continue_ = True
n_turns = 0
while continue_:
    continue_, n_turns = move_guard(n_turns)
    ct = time.time()
    elapsedt = int(ct - st)


n_visited = sum([pos for v_row in visited for pos in v_row])
print(n_visited)
