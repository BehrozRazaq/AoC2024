data = """""".splitlines()

from operator import itemgetter
import numpy as np
import numpy.typing as npt

size = len(data) - 1
a_map = np.array([[char for char in row] for row in data])
frequency_positions = {}
n_antennas = 0
for r_i in range(len(a_map)):
    for c_i in range(len(a_map[r_i])):
        node = a_map[r_i][c_i]
        if node == ".":
            continue

        if node not in frequency_positions:
            frequency_positions[node] = []
        frequency_positions[node].append(np.array([r_i, c_i]))
        n_antennas += 1


def pos_on_board(pos: npt.NDArray):
    return (pos <= np.array([size, size])).all() and (pos >= np.array([0, 0])).all()


antinodes = []
for frequency, positions in frequency_positions.items():
    for l_pos in positions:
        for r_pos in positions:
            last_on_board = True
            if (l_pos == r_pos).all():
                continue
            move_vect = l_pos - r_pos
            new_l = l_pos
            while last_on_board:
                pot_anode = new_l + move_vect
                last_on_board = pos_on_board(pot_anode)
                if not last_on_board:
                    continue
                new_l = pot_anode
                exists = any([(pot_anode == node).all() for node in antinodes])
                if exists:
                    continue
                antinodes.append(pot_anode)


for values in frequency_positions.values():
    for value in values:
        exists = any([(value == node).all() for node in antinodes])
        if exists:
            continue
        antinodes.append(value)

print(np.array(antinodes))
print(len(antinodes))
