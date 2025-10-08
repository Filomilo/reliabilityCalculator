

def dystrybunataFt(brokenElementsAfterTime:dict[int, int], amountOfElementsTotal: int)-> dict[int, float]:
    result: dict[int, float] = {}
    for time, broken in brokenElementsAfterTime.items():
        result[time]= sum(brokenElementsAfterTime[t] for t in range(1, time+1))/(amountOfElementsTotal)
    return result

def funkcjaNiezawdnosciRt(brokenElementsAfterTime:dict[int, int], amountOfElementsTotal: int)-> dict[int, float]:
    result: dict[int, float] = {}
    for time, broken in brokenElementsAfterTime.items():
        result[time]= (amountOfElementsTotal-sum(brokenElementsAfterTime[t] for t in range(1, time+1)))/(amountOfElementsTotal)
    return result



# zakładm żę delta t to 1h i są po kolei
def funkcjaGestaft(brokenElementsAfterTime:dict[int, int], amountOfElementsTotal: int)-> dict[int, float]:
    result: dict[int, float] = {}
    prevTime = 0
    keys = sorted(brokenElementsAfterTime.keys())[:-1]
    for time in keys:
        result[time]= (brokenElementsAfterTime[time])/(amountOfElementsTotal*(time-prevTime))
        prevTime = time
    return result



def funkcjaIntensywnoscilambdat(brokenElementsAfterTime:dict[int, int], amountOfElementsTotal: int)-> dict[int, float]:
    result: dict[int, float] = {}
    prevTime = 0
    keys = sorted(brokenElementsAfterTime.keys())[:-1]
    for time in keys:
        if(time==1):
             result[time]=0
        else:
            mti= brokenElementsAfterTime[time]
            sumPrevious= sum(brokenElementsAfterTime[t] for t in range(1, time))
            timeDiff = time - prevTime
            mianownik = amountOfElementsTotal - sumPrevious
            print(f"minanownik: {mianownik}, mti: {mti}, sumPrevious: {sumPrevious}, timeDiff: {timeDiff}, time: {time}, prevTime: {prevTime}")
            result[time]= (mti)/mianownik
        prevTime = time
    return result


def rozkladTrwalosciEta(brokenElementsAfterTime:dict[int, int], amountOfElementsTotal: int)-> float:
    dystrybunata: dict[int, float] = dystrybunataFt(brokenElementsAfterTime, amountOfElementsTotal)
    keys = sorted(brokenElementsAfterTime.keys())[:-1]
    suma =0
    for time in keys:
        dystrybunatadiff= dystrybunata[time+1]- dystrybunata[time]
        print(f"dystrybunatadiff: {dystrybunatadiff}, time: {time}")
        suma += time*dystrybunatadiff
        
    return suma
