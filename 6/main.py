def findMarker(input, span: int) -> int:
    marker = 0
    markerbuffer = []
    cursor = 1
    valuefound = False
    bufferlen = 512

    while True and not valuefound:
        data = list(input.read(bufferlen))
        if not data:
            break
        
        for characterindex, char in enumerate(data):
            markerbuffer.insert(0, char)

            if len(markerbuffer) == span:
                for markerindex, markerchar0 in enumerate(markerbuffer):
                    end = False
                    for markerindex1, markerchar1 in enumerate(markerbuffer):
                        if markerindex == markerindex1:
                            continue
                        elif markerchar0 == markerchar1:
                            end = True
                            break
                    if end:
                        break
                    elif markerindex + 1 == len(markerbuffer):
                        marker = cursor + characterindex
                        valuefound = True
                        break
                markerbuffer.pop()
            if valuefound:
                break
        cursor += bufferlen

    return marker


def solution1() -> int:
    with open("input", "r") as input:
        return findMarker(input, 4)


def solution2() -> int:
    with open("input", "r") as input:
        return findMarker(input, 14)

if __name__ == "__main__":
    print (solution1())
    print (solution2())