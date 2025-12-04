def detect_ids(r: str):
    result = []
    b, e = r.split("-")
    for i in range(int(b), int(e)+1):
        curr = str(i)
        pat = ""
        for j, v in enumerate(curr):
            pat += v
            if j+1 < len(curr) and pat not in curr[j+1:]:
                break

        if pat[:-1]*2 == curr:
            result.append(i)

    return result


def solve_1(lines: list[str]):
    ranges = []
    for line in lines:
        r = [i for i in line.split(",") if len(i) > 0]
        ranges.extend(r)

    ids = [j for i in ranges for j in detect_ids(i)]
    return ids


def detect_ids_2(r: str):
    result = []
    b, e = r.split("-")
    for i in range(int(b), int(e)+1):
        curr = str(i)
        pat = ""
        found = False
        for j, v in enumerate(curr):
            pat += v
            if j+1 < len(curr) and pat in curr[j+1:]:
                for k in range(len(curr)+1):
                    if not found and pat*k == curr and len(pat*k) % len(curr) == 0:
                        result.append(int(curr))
                        found = True
                        break

    return result


def solve_2(lines: list[str]):
    ranges = []
    for line in lines:
        r = [i for i in line.split(",") if len(i) > 0]
        ranges.extend(r)

    ids = [j for i in ranges for j in detect_ids_2(i)]
    return ids


def main(filename: str):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())

    result = sum(solve_2(lines))
    print(result)


if __name__ == "__main__":
    test_f = "test.txt"
    input_f = "input.txt"
    main(input_f)
