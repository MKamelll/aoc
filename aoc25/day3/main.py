import sys

# gave up and asked chatgpt and
# it turns out i couldn't be further from the actual solution
def get_max2(line: str):
    result = []
    k = 12

    b = 0
    while k > 0:
        e = len(line) - k + 1

        best = 0
        best_i = b
        for i in range(b, e):
            if int(line[i]) > best:
                best = int(line[i])
                best_i = i

        result.append(best)
        b = best_i + 1
        k -= 1

    return int("".join(str(i) for i in result))


def solve_2(lines: list[str]):
    maxes = []
    for line in lines:
        maxes.append(get_max2(line))

    return maxes


def get_max(line: str):
    curr_max = 0
    for i, _ in enumerate(line):
        if i+1 < len(line):
            j = i + 1
            while j < len(line):
                if int(line[i] + line[j]) > curr_max:
                    curr_max = int(line[i] + line[j])
                j += 1
    return curr_max


def solve_1(lines: list[str]):
    maxes = []
    for line in lines:
        maxes.append(get_max(line))

    return maxes


def main(filename: str):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())

    result = sum(solve_2(lines))
    print(result)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise "Not enough arguments"

    file_name = sys.argv[1]
    main(file_name)
