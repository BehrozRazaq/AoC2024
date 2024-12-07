from copy import deepcopy


class Scene:
    def __init__(self, guard, dir, grid, visited) -> None:
        self.g_pos = guard
        self.g_dir = dir
        self.grid = grid
        self.visited = visited
        self.history = [[[] for _ in row] for row in grid]

    def turn(self, n_turns):
        possible_turns = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        return possible_turns[n_turns % 4], n_turns + 1

    def move_guard(self, n_turns):
        out_of_grid = lambda ax: ax < 0 or ax >= len(self.grid)
        move = lambda p, d: (p[0] + d[0], p[1] + d[1])
        if out_of_grid(self.g_pos[0]) or out_of_grid(self.g_pos[1]):
            return False, n_turns
        pot_r, pot_c = move(self.g_pos, self.g_dir)
        if out_of_grid(pot_r) or out_of_grid(pot_c):
            self.g_pos = (pot_r, pot_c)
            return False, n_turns
        if self.grid[pot_r][pot_c]:
            self.g_dir, n_turns = self.turn(n_turns)
            return True, n_turns
        else:
            if self.g_pos in self.history[pot_r][pot_c]:
                return False, -1
            self.history[pot_r][pot_c].append((self.g_pos[0], self.g_pos[1]))
            self.g_pos = (pot_r, pot_c)
            self.visited[pot_r][pot_c] = True
            return True, n_turns


def grid_alts(grid):
    pot_grids = []
    for i, row in enumerate(grid):
        for j, pos in enumerate(row):
            if not pos:
                pot_grid = deepcopy(grid)
                pot_grid[i][j] = True
                pot_grids.append(pot_grid)
    return pot_grids


def main():
    with open("6/input.txt", "r") as f:
        data = f.readlines()

    g_pos = (0, 0)
    g_dir = (-1, 0)
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
                g_pos = (r, c)
            row.append(False)
        visited.append(f_row)
        grid.append(row)
    pot_grids = grid_alts(grid)
    pot_visited = [deepcopy(visited) for g in pot_grids]
    pot_g_pos = [deepcopy(g_pos) for g in pot_grids]
    pot_g_dir = [deepcopy(g_dir) for g in pot_grids]
    import alive_progress

    with alive_progress.alive_bar(len(pot_grids)) as bar:
        n_loops = 0
        for g_pos, g_dir, grid, visited in zip(
            pot_g_pos, pot_g_dir, pot_grids, pot_visited
        ):
            scene = Scene(g_pos, g_dir, grid, visited)

            continue_ = True
            n_turns = 0
            while continue_:
                continue_, n_turns = scene.move_guard(n_turns)
                if n_turns < 0:
                    n_loops += 1
            bar()
    print(n_loops)


main()
