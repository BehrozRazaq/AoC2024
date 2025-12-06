data = """""".splitlines()

import numpy as np
import numpy.typing as npt

size = len(data) - 1
a_map = np.array([[char for char in row] for row in data])
frequency_positions = {}
for r_i in range(len(a_map)):
    for c_i in range(len(a_map[r_i])):
        node = a_map[r_i][c_i]
        if node == ".":
            continue

        if node not in frequency_positions:
            frequency_positions[node] = []
        frequency_positions[node].append(np.array([r_i, c_i]))


def pos_on_board(pos: npt.NDArray):
    return (pos <= np.array([size, size])).all() and (pos >= np.array([0, 0])).all()


antinodes = []
for frequency, positions in frequency_positions.items():
    for l_pos in positions:
        for r_pos in positions:
            if (l_pos == r_pos).all():
                continue

            pot_anode = l_pos + l_pos - r_pos
            if not pos_on_board(pot_anode):
                continue
            exists = any([(pot_anode == node).all() for node in antinodes])
            if exists:
                continue
            antinodes.append(pot_anode)
print(len(antinodes))
