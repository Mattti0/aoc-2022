

def solution1() -> int:
    with open("input", "r") as input:
        forest = input.readlines()
        forest = [list(f.strip()) for f in forest]
        forest = [[int(tree) for tree in f] for f in forest]

        treesvisible = 0
        for rindex, row in enumerate(forest):
            for colindex, col in enumerate(row):
                if rindex == 0 or colindex == 0:
                    treesvisible += 1
                elif rindex + 1 == len(forest) or colindex +1 == len(row):
                    treesvisible += 1
                else:
                    visible = {
                        "top" : True,
                        "bottom" : True,
                        "left" : True,
                        "right" : True
                    }

                    for i in forest[:rindex]:
                        if i[colindex] >= col:
                            visible.update({"top" : False})
                            break
                    
                    for i in forest[rindex+1:]:
                        if i[colindex] >= col:
                            visible.update({"bottom" : False})
                            break
                    
                    for i in row[:colindex]:
                        if i >= col:
                            visible.update({"left" : False})
                            break
                    
                    for i in row[colindex+1:]:
                        if i >= col:
                            visible.update({"right" : False})
                            break
                    
                    if visible.get("top") \
                        or visible.get("bottom") \
                            or visible.get("left") \
                                or visible.get("right"):
                        treesvisible += 1


        return treesvisible


def solution2() -> int:
    with open("input", "r") as input:
        forest = input.readlines()
        forest = [list(f.strip()) for f in forest]
        forest = [[int(tree) for tree in f] for f in forest]

        score = 0
        for rindex, row in enumerate(forest):
            for colindex, col in enumerate(row):
                if rindex == 0 or colindex == 0:
                    continue
                elif rindex + 1 == len(forest) or colindex +1 == len(row):
                    continue
                else:
                    visible = {
                        "top" : 0,
                        "bottom" : 0,
                        "left" : 0,
                        "right" : 0
                    }
                    
                    for i in reversed(forest[:rindex]):
                        if i[colindex] < col:
                            visible["top"] += 1
                        else:
                            visible["top"] += 1
                            break
                    
                    for i in forest[rindex+1:]:
                        if i[colindex] < col:
                            visible["bottom"] += 1
                        else:
                            visible["bottom"] += 1
                            break

                    for i in reversed(row[:colindex]):
                        if i < col:
                            visible["left"] += 1
                        else:
                            visible["left"] += 1
                            break
                    
                    for i in row[colindex+1:]:
                        if i < col:
                            visible["right"] += 1
                        else:
                            visible["right"] += 1
                            break
                    
                    
                    compare = (visible["top"] * visible["bottom"] * visible["left"] * visible["right"])
                    if compare > score:
                        score = compare

        return score


if __name__ == "__main__":
    print (solution1())
    print (solution2())
