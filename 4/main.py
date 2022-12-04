
def solution1() -> int:
    with open("input", "r") as input:
        score = 0
        pairs = [x.split(",") for x in [i.strip() for i in input.readlines()]]

        for pair in pairs:
            p0 = pair[0].split("-")
            p1 = pair[1].split("-")

            p0 = [int(p) for p in p0]
            p1 = [int(p) for p in p1]


            if p0[0] <= p1[0] and p0[1] >= p1[1]:
                score += 1
            elif p1[0] <= p0[0] and p1[1] >= p0[1]:
                score += 1

        return score


def solution2() -> int:
    with open("input", "r") as input:
        score = 0
        pairs = [x.split(",") for x in [i.strip() for i in input.readlines()]]

        for pair in pairs:
            p0 = pair[0].split("-")
            p1 = pair[1].split("-")

            p0 = [int(p) for p in p0]
            p1 = [int(p) for p in p1]


            if p0[0] <= p1[0] and p0[1] >= p1[1]:
                score += 1
            elif p1[0] <= p0[0] and p1[1] >= p0[1]:
                score += 1
            elif p0[0] >= p1[0]  and p0[0] <= p1[1]:
                score += 1
            elif p0[1] >= p1[0]  and p0[1] <= p1[1]:
                score += 1
            elif p1[0] >= p0[0]  and p1[0] <= p0[1]:
                score += 1
            elif p1[1] >= p0[0]  and p1[1] <= p0[1]:
                score += 1

        return score

if __name__ == "__main__":
    print (solution1())
    print (solution2())