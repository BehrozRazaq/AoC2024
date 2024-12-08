def parse_grid(grid_txt: str):
    grid = []
    for row in grid_txt:
        grid.append([c for c in row])
    return grid


def in_bounds(grid, r, c):
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    potentials = []
    for r_off, c_off in dirs:
        pot_r, pot_c = r + r_off, c + c_off
        if pot_r >= 0 and pot_r < len(grid) and pot_c >= 0 and pot_c < len(grid):
            potentials.append(True)
        else:
            potentials.append(False)

    return all(potentials)


def is_x_mas(grid, r, c):
    dirs = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
    opp = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
    n_ms = 0

    for i, offs in enumerate(dirs):
        r_off, c_off = offs
        c_r, c_c = r + r_off, c + c_off
        o_r_off, o_c_off = opp[i]
        o_r, o_c = r + o_r_off, c + o_c_off

        if grid[c_r][c_c] == "M" and grid[o_r][o_c] == "S":
            n_ms += 1

    return n_ms == 2


def find_x_mas(grid):
    n_x_mas = 0
    xmasses = []
    for r, row in enumerate(grid):
        for c, letter in enumerate(row):
            if letter != "A" or not in_bounds(grid, r, c):
                continue

            n_x_mas += 1 if is_x_mas(grid, r, c) else 0

    return n_x_mas


def main():
    with open("4/input.txt") as f:
        data = f.read().splitlines()

    grid = parse_grid(data)
    print(find_x_mas(grid))


if __name__ == "__main__":
    main()
