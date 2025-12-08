import sys


def update_board(m: list[list[str]]):
    n_rows = len(m)
    n_cols = len(m[0])

    marks = []
    rolls = 0

    for row in range(n_rows):
        for col in range(n_cols):

            nbrs = 0

            if not m[row][col] == '@':
                continue

            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:

                    if i == j == 0:
                        continue

                    r = row + i
                    c = col + j

                    if 0 <= r < n_rows and 0 <= c < n_cols and m[r][c] == '@':
                        nbrs += 1

            if nbrs < 4:
                rolls += 1
                marks.append([row, col])

    for i in marks:
        m[i[0]][i[1]] = '.'

    return rolls, m


def solve_2(lines: list[str]):
    m = [[x for x in i]
         for i in lines]

    result = 0
    removed, m = update_board(m)
    result += removed
    while removed != 0:
        removed, m = update_board(m)
        result += removed

    return result


def solve_1(lines: list[str]):
    m = [[x for x in i]
         for i in lines]

    n_rows = len(m)
    n_cols = len(m[0])

    rolls = 0

    for row in range(n_rows):
        for col in range(n_cols):

            nbrs = 0

            if not m[row][col] == '@':
                continue

            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:

                    if i == j == 0:
                        continue

                    r = row + i
                    c = col + j

                    if 0 <= r < n_rows and 0 <= c < n_cols and m[r][c] == '@':
                        nbrs += 1

            if nbrs < 4:
                rolls += 1

    return rolls


def main():
    lines = []
    if len(sys.argv) < 2:
        raise "not enough aruments"

    fname = sys.argv[1]
    with open(fname) as f:
        for line in f:
            lines.append(line.strip())

    result = solve_2(lines)
    print(result)


if __name__ == "__main__":
    main()
