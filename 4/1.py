def parse_grid(grid_txt: str):
    grid = []
    for row in grid_txt:
        grid.append([c for c in row])
    return grid


def get_neighbour_offsets(grid, r, c):
    norm = lambda left, right: (int(left / 3), int(right / 3))

    dirs = [(-3, -3), (-3, 0), (-3, 3), (0, -3), (0, 3), (3, -3), (3, 0), (3, 3)]
    potentials = []
    for r_off, c_off in dirs:
        pot_r, pot_c = r + r_off, c + c_off
        if pot_r >= 0 and pot_r < len(grid) and pot_c >= 0 and pot_c < len(grid):
            potentials.append(norm(r_off, c_off))

    return potentials


def is_as(grid, r, c, r_off, c_off):
    r, c = r + r_off, c + c_off
    if grid[r][c] == "A":
        r, c = r + r_off, c + c_off
        if grid[r][c] == "S":
            return True
    return False


def find_xmas(grid):
    n_xmas = 0
    xmasses = []
    for r, row in enumerate(grid):
        for c, letter in enumerate(row):
            if letter != "X":
                continue

            potential_ms = get_neighbour_offsets(grid, r, c)

            for r_off, c_off in potential_ms:
                pot_r, pot_c = r + r_off, c + c_off

                if grid[pot_r][pot_c] == "M":
                    if is_as(grid, pot_r, pot_c, r_off, c_off):
                        xmasses.append((r, c, r_off, c_off))
                        n_xmas += 1
    return n_xmas


def main():
    with open("4/input.txt") as f:
        data = f.read().splitlines()

    grid = parse_grid(data)
    print(find_xmas(grid))


if __name__ == "__main__":
    main()
