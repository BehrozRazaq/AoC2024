class Block:
    def __init__(self, file_id: str, start: int, size: int) -> None:
        self.file_id = file_id
        self.start = start
        self.size = size

    def __eq__(self, value: str) -> bool:
        return self.file_id == value

    def __lt__(self, other):
        return self.start < other.start

    def is_empty(self) -> bool:
        return self.file_id == "."

    def calc_check_sum(self):
        check_sum = 0
        if self.file_id == ".":
            return check_sum
        for i in range(self.start, self.start + self.size):
            check_sum += int(self.file_id) * i
        return check_sum

    def __repr__(self) -> str:
        return f"{self.start} {self.file_id} {self.size}"

    def __str__(self) -> str:
        return str(self.file_id) * self.size


def parse_blocks(memory: str) -> list[Block]:
    blocks = []
    index = 0
    id = 0
    for loop_i, size in enumerate(memory):
        size = int(size)
        if loop_i % 2 == 0:
            char = id
            id += 1
        else:
            char = "."
        blocks.append(Block(char, index, size))

        index += size
    return blocks


def traverse_blocks(blocks: list[Block]) -> list[Block]:
    left = 0
    right = len(blocks) - 1

    while left < right:

        while left < right and blocks[left] != ".":
            left += 1
            if left >= right:
                left = 0
                right -= 1
        while left < right and blocks[right] == ".":
            right -= 1
        l_block, r_block = blocks[left], blocks[right]

        if left < right and l_block.size < r_block.size:
            left += 1
            if left >= right:
                left = 0
                right -= 1
            continue
        if left < right and l_block.size >= r_block.size:
            if l_block.size == r_block.size:
                l_block.file_id = r_block.file_id
                r_block.file_id = "."
            else:
                diff = l_block.size - r_block.size
                tmp_index = r_block.start
                r_block.start = l_block.start
                l_block.start = tmp_index
                l_block.size = r_block.size

                blocks.append(Block(".", r_block.start + r_block.size, diff))
                blocks.sort()

            left = 0
            right -= 1
    return blocks


def checksum(blocks: list[Block]) -> int:
    return sum([block.calc_check_sum() for block in blocks])


def main():
    data = "2333133121414131402"
    blocks = parse_blocks(data)
    blocks = traverse_blocks(blocks)

    print(f"Checksum:  {checksum(blocks)}")


if __name__ == "__main__":
    main()
