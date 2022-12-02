import pandas

def solution1() -> int:
    df = ""
    with open("input", "r") as input:
        elves = []
        elf = []
        for i in input.readlines():
            try:
                elf.append(int(i))
            except ValueError:
                elves.append(elf.copy())
                elf.clear()

        df = pandas.DataFrame(elves)

    return df.sum(axis='columns', skipna=True).max()


def solution2() -> int:
    df = ""
    with open("input", "r") as input:
        elves = []
        elf = []
        for i in input.readlines():
            try:
                elf.append(int(i))
            except ValueError:
                elves.append(elf.copy())
                elf.clear()

        df = pandas.DataFrame(elves)

    return df.sum(axis='columns', skipna=True).nlargest(3).sum()

if __name__ == "__main__":
    print(solution1())
    print(solution2())