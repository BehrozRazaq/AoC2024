import re


def main():
    with open("3/input.txt", "r") as f:
        data = f.read()

    exp = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"

    matches = re.findall(exp, data)
    enabled = True
    sum_of_mults = 0
    for match in matches:
        if match[2] == "do()":
            enabled = True
        elif match[3] == "don't()":
            enabled = False
        else:
            if not enabled:
                continue
            sum_of_mults += int(match[0]) * int(match[1])
    print(sum_of_mults)


main()
