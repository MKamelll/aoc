import sys


def solve_2(lines: list[str]):
    sep_i = lines.index("")
    a1 = [[int(j) for j in i.split("-")] for i in lines[:sep_i]]

    ranges = []
    a1.sort()

    ranges.append(a1[0])

    for start, end in a1[1:]:

        if start <= ranges[-1][1]:
            ranges[-1][1] = max(ranges[-1][1], end)
        else:
            ranges.append([start, end])

    result = [(end - start)+1 for start, end in ranges]
    return sum(result)


def is_in_range(start: int, end: int, i: int):
    return start <= i <= end


def solve_1(lines: list[str]):
    sep_i = lines.index("")
    a1, a2 = [[int(j) for j in i.split("-")]
              for i in lines[:sep_i]], [int(i) for i in lines[sep_i+1:]]

    count = 0
    for i in a2:
        for j in a1:
            if is_in_range(j[0], j[1], i):
                count += 1
                break

    return count


def main():
    if len(sys.argv) < 2:
        raise Exception("not enough arguments")

    file_name = sys.argv[1]
    lines = []
    with open(file_name) as f:
        for line in f:
            lines.append(line.strip())

    result = solve_2(lines)
    print(result)


if __name__ == "__main__":
    main()
