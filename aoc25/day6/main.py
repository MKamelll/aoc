import sys


def solve_2(lines: list[str]):
    calcs = []
    lines, op = lines[:-1], lines[-1]
    op = [i for i in op if not i.isspace()]

    for i in range(len(lines[0])-1, -1, -1):
        calc = ""
        for j in range(len(lines)-1, -1, -1):
            calc += lines[j][i]
        calcs.append(calc[::-1])

    calcz = []
    calc = []
    for i, _ in enumerate(calcs):
        if calcs[i].isspace():
            calcz.append(calc)
            calc = []
        else:
            calc.append(calcs[i])
    calcz.append(calc)

    for i in range(len(calcz)):
        calcz[i].append(op[len(op)-1-i])

    results = []
    for i in calcz:
        if i[-1] == "*":
            result = 1
            for j in i[:-1]:
                result *= int(j)
            results.append(result)

        if i[-1] == "+":
            result = 0
            for j in i[:-1]:
                result += int(j)
            results.append(result)

    return sum(results)


def solve_1(lines: list[str]):
    calcs = []
    for i in range(len(lines[0])):
        calc = []
        for j in range(len(lines)):
            calc.append(lines[j][i])

        calcs.append(calc)

    results = []

    for i in calcs:
        if i[-1] == "*":
            result = 1
            for j in i[:-1]:
                result *= int(j)
            results.append(result)

        if i[-1] == "+":
            result = 0
            for j in i[:-1]:
                result += int(j)

            results.append(result)

    return sum(results)


def main():
    if len(sys.argv) < 2:
        raise Exception("not enough arguments")

    fname = sys.argv[1]
    lines = []
    lines2 = []
    with open(fname) as f:
        for line in f:
            cols = line.split(" ")
            lines.append([i.strip() for i in cols if len(i.strip()) > 0])

    with open(fname) as f:
        for line in f:
            cols = line.strip("\n")
            lines2.append(cols)

    result = solve_2(lines2)
    print(result)


if __name__ == "__main__":
    main()
