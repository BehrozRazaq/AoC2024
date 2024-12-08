def add(a, b):
    return a + b


def mult(a, b):
    return a * b


def concat(a, b):
    return int(str(a) + str(b))


def test_possible(test: int, terms: list[int], res):
    if not terms:
        return any([test == r for r in res])

    operators = [add, mult, concat]
    prev = res.copy()
    res = []
    for op in operators:
        for val in prev:
            res.append(op(val, terms[0]))
    return test_possible(test, terms[1:], res)


def main():
    with open("7/input.txt", "r") as f:
        data = f.readlines()

    res = 0
    for line in data:
        line = line.split()
        test = int(line[0][:-1])
        terms = [int(i) for i in line[1:]]

        if test_possible(test, terms[1:], [terms[0]]):
            res += test
    print(res)


main()
