

def dystrybunataFt(brokenElementsAfterTime:dict[int, int], amountOfElementsTotal: int)-> dict[int, float]:
    result: dict[int, float] = {}
    for time, broken in brokenElementsAfterTime.items():
        result[time]= sum(brokenElementsAfterTime[t] for t in range(1, time+1))/(amountOfElementsTotal)
    return result

def funkcjaNiezawdnosciRt(brokenElementsAfterTime:dict[int, int])-> dict[int, float]:
    result: dict[int, float] = {}
    for time, broken in brokenElementsAfterTime.items():
        result[time]= sum(brokenElementsAfterTime[t] for t in range(1, time+1))/(amountOfElementsTotal)
    return result


def funkcjaGestaft(brokenElementsAfterTime:dict[int, int])-> dict[int, float]:
    return {
        1: 10,
        2: 3,
        3: 22
    }



def funkcjaIntensywnoscilambdat(brokenElementsAfterTime:dict[int, int])-> dict[int, float]:
    return {
        1: 10,
        2: 3,
        3: 22
    }


def rozkladTrwalosciEta(brokenElementsAfterTime:dict[int, int])-> float:
    return 0.5
