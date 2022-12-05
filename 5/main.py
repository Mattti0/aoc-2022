import re # use regex to parse move commands

def getEmptyAreas(row):
    emptyareas = []
    emptystart = -1
    for i, item in enumerate(row):
        if item == "" and emptystart == -1:
            emptystart = i
        elif emptystart != -1 and item != "":
            emptyareas.append([emptystart, i-1])
            emptystart = -1
        elif i+1 == len(row) and item == "":
            emptyareas.append([emptystart, i])
    return emptyareas

def removeSpaces(row, emptyareas):
    for i in reversed(emptyareas):
        removecount = (i[1] - i[0]) - int((i[1] - i[0]) / 4)
        removefrom = i[1]
        for z in range(removecount):
            row.pop(removefrom)
            removefrom -= 1
    return row

def transposeArray(arr):
    transposed = []
    for i in arr[0]:
        transposed.append([]) # init new array to right size
    for row in arr:
        for i, col in enumerate(row):
            if col != "":
                transposed[i].insert(0, col)
    return transposed


def solution1() -> int:
    with open("input", "r") as input:
        score = 0
        stacks = []
        commands = []
        inputsection = 1
        for i in input.readlines():
            i = i.replace('\n' , '') 
            try:
                if inputsection == 1 and int(list(i.strip())[0]) == 1:
                    inputsection += 1
            except ValueError:
                pass

            if inputsection == 1:
                i = i.split(" ")
                stacks.append(i)
            elif inputsection == 2:
                row = [int(z) for z in re.findall(r'\d+', i)]
                commands.append(row)

        for x, r in enumerate(stacks):
            emptyareas = getEmptyAreas(r)
            r = removeSpaces(r, emptyareas)
            stacks[x] = r

        transposed = transposeArray(stacks)
        
        # move containers
        for com in commands:
            if len(com) == 3: # three command parameters
                for m in range(com[0]):
                    transposed[com[2] - 1].append(transposed[com[1] - 1].pop())

        result = ""
        for c in transposed:
            result += c.pop()
        print(result.replace("[", "").replace("]", ""))
        

        return score


def solution2() -> int:
    with open("input", "r") as input:
        score = 0
        stacks = []
        commands = []
        inputsection = 1
        for i in input.readlines():
            i = i.replace('\n' , '') 
            try:
                if inputsection == 1 and int(list(i.strip())[0]) == 1:
                    inputsection += 1
            except ValueError:
                pass

            if inputsection == 1:
                i = i.split(" ")
                stacks.append(i)
            elif inputsection == 2:
                row = [int(z) for z in re.findall(r'\d+', i)]
                commands.append(row)

        for x, r in enumerate(stacks):
            emptyareas = getEmptyAreas(r)
            r = removeSpaces(r, emptyareas)
            stacks[x] = r

        transposed = transposeArray(stacks)
        
        # move containers
        for com in commands:
            if len(com) == 3: # three command parameters
                containerstomove = []
                for m in range(com[0]):
                    containerstomove.insert(0, transposed[com[1] - 1].pop())
                transposed[com[2] - 1] += containerstomove

        result = ""
        for c in transposed:
            result += c.pop()
        print(result.replace("[", "").replace("]", ""))
        

        return score

if __name__ == "__main__":
    print("Solution 1:")
    print (solution1())
    print("Solution 2:")
    print (solution2())