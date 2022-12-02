

def solution1() -> int:
    def win(round: list[str]) -> bool:
        if round[0] == "A" and round[1] == "Y":
            return True
        elif round[0] == "B" and round[1] == "Z":
            return True
        elif round[0] == "C" and round[1] == "X":
            return True
        
        return False

    def draw(round: list[str]) -> bool:
        if round[0] == "A" and round[1] == "X":
            return True
        elif round[0] == "B" and round[1] == "Y":
            return True
        elif round[0] == "C" and round[1] == "Z":
            return True
        
        return False

    def shapescore(round: list[str]) -> int:
        shape = round[1]
        if shape == "Y":
            return 2
        elif shape == "Z":
            return 3
        elif shape == "X":
            return 1

        return 0

    with open("input", "r") as input:
        rounds = [i.strip().split(" ") for i in input.readlines()]
        scores = 0
        for r in rounds:
            if win(r):
                scores += 6
            elif draw(r):
                scores += 3

            scores += shapescore(r)

        return (scores)


def solution2() -> int:
    def win(round: list[str]) -> bool:
        if round[1] == "Z":
            return True
        
        return False

    def draw(round: list[str]) -> bool:
        if round[1] == "Y":
            return True
        
        return False

    def getShape(round: list[str], wdl: str) -> str:
        shape = round[0]
        if wdl == "W":
            if shape == "A":
                return "B"
            elif shape == "B":
                return "C"
            elif shape == "C":
                return "A"
        elif wdl == "D":
            if shape == "A":
                return "A"
            elif shape == "B":
                return "B"
            elif shape == "C":
                return "C"
        elif wdl == "L":
            if shape == "A":
                return "C"
            elif shape == "B":
                return "A"
            elif shape == "C":
                return "B"

    def shapescore(shape:str) -> int:
        if shape == "B":
            return 2
        elif shape == "C":
            return 3
        elif shape == "A":
            return 1

        return 0

    with open("input", "r") as input:
        rounds = [i.strip().split(" ") for i in input.readlines()]
        scores = 0
        for r in rounds:
            wdl = ""
            if win(r):
                scores += 6
                wdl = "W"
            elif draw(r):
                scores += 3
                wdl = "D"
            else:
                wdl = "L"

            shape = getShape(r, wdl)

            scores += shapescore(shape)

        return scores

if __name__ == "__main__":
    print (solution1())
    print (solution2())