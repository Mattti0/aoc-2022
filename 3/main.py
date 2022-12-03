
def solution1() -> int:
    with open("input", "r") as input:
        score = 0
        elves = [x.split() for x in [i.strip() for i in input.readlines()]]

        for e in elves:
            i = list(e[0])
            e1 = i[:int(len(i)/2)]
            e2 = i[int(len(i)/2):]
            
            for c in e1:
                if c in e2:
                    if ord(c) >= 97 and ord(c) <= 122:
                        score += ord(c) - ord('a') + 1
                    elif ord(c) >= 65 and ord(c) <= 90:
                        score += ord(c) - ord('A') + 27
                    break

        return score


def solution2() -> int:
    def getScore(c: str) -> int:
        score = 0
        if ord(c) >= 97 and ord(c) <= 122:
            score += ord(c) - ord('a') + 1
        elif ord(c) >= 65 and ord(c) <= 90:
            score += ord(c) - ord('A') + 27

        return score

    def lookChars(o0, o1, o2) -> str:
        for c in list(o0[0]):
            if c in o1[0] and c in o2[0]:
                return c


    with open("input", "r") as input:
        score = 0
        elves = [x.split() for x in [i.strip() for i in input.readlines()]]

        for i in range(0, len(elves), 3):
            x = elves[i:i+3]
            ch = lookChars(x[0], x[1], x[2])
            score += getScore(ch)


        return score

if __name__ == "__main__":
    print (solution1())
    print (solution2())