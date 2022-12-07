
def handlefolders(name, inputindex, input):
    folder = {}

    while True and inputindex < len(input):
        row = input[inputindex].strip().split(" ")

        if row[0] == "$":
            if row[1] == "cd":
                if row[2] != ".." and row[2] != "/":
                    inputindex, folder[row[2]] = handlefolders(row[2], inputindex + 1, input)
                elif row[2] == "..":
                    break
        else:
            try:
                folder[row[1]] = int(row[0])
            except ValueError:
                pass
        inputindex += 1
    

    return inputindex, folder


def calcsizes(path):
    filesize = 0

    for key, value in path.items():
        if isinstance(value, dict):
            filesize += calcsizes(value)
        else:
            filesize += value

    path.update({"size": filesize})

    return filesize


def findmaxsize(path, maxsize, base):
    for key, value in path.items():
        if isinstance(value, dict):
            if value.get("size") <= maxsize:
                base += value.get("size")
            base = findmaxsize(value, maxsize, base)

    return base


def findfoldertoremove(path, minsize, smallestsufficient):
    for key, value in path.items():
        if isinstance(value, dict):
            if value.get("size") < smallestsufficient and value.get("size") > minsize:
                smallestsufficient = value.get("size")
            elif value.get("size") < minsize: # no need to go deeper
                continue
            smallestsufficient = findfoldertoremove(value, minsize, smallestsufficient)

    return smallestsufficient


def solution1() -> int:
    with open("input", "r") as input:
        inputarr = input.readlines()
        inputindex = 0
        ospath = {}
        row = inputarr[inputindex].strip().split(" ")
        
        if row[0] == "$":
            if row[1] == "cd":
                if row[2] == "/":
                    inputindex, ospath["."] = handlefolders("/", inputindex, inputarr)       

        calcsizes(ospath["."])        
        score = findmaxsize(ospath, 100000, 0)

        return score


def solution2() -> int:
    osfilesystemsize = 70000000
    minupdatesize = 30000000

    with open("input", "r") as input:
        inputarr = input.readlines()
        inputindex = 0
        ospath = {}
        row = inputarr[inputindex].strip().split(" ")
        
        if row[0] == "$":
            if row[1] == "cd":
                if row[2] == "/":
                    inputindex, ospath["."] = handlefolders("/", inputindex, inputarr)
                    
        calcsizes(ospath["."])    
        score = findfoldertoremove(ospath, minupdatesize - (osfilesystemsize - ospath["."].get("size")), osfilesystemsize+1)

        return score


if __name__ == "__main__":
    print (solution1())
    print (solution2())
