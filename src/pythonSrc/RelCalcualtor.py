import math

def dystrybunataFt(brokenElementsAfterTime: dict[int, int], amountOfElementsTotal: int) -> dict[int, float]:
    if amountOfElementsTotal <= 0:
        raise ValueError("Liczba elementów musi być większa od zera")

    result: dict[int, float] = {}
    sorted_times = sorted(brokenElementsAfterTime.keys())

    for time in sorted_times:
        cumulative = sum(brokenElementsAfterTime.get(t, 0) for t in range(sorted_times[0], time + 1))
        ft = cumulative / amountOfElementsTotal
        result[time] = min(max(ft, 0.0), 1.0)
        if math.isnan(result[time]) or math.isinf(result[time]) or result[time] < 0:
            result[time] = 0.0
    return result


def funkcjaNiezawdnosciRt(brokenElementsAfterTime: dict[int, int], amountOfElementsTotal: int) -> dict[int, float]:
    if amountOfElementsTotal <= 0:
        raise ValueError("Liczba elementów musi być większa od zera")

    result: dict[int, float] = {}
    sorted_times = sorted(brokenElementsAfterTime.keys())

    for time in sorted_times:
        broken_sum = sum(brokenElementsAfterTime.get(t, 0) for t in range(sorted_times[0], time + 1))
        rt = (amountOfElementsTotal - broken_sum) / amountOfElementsTotal
        result[time] = max(min(rt, 1.0), 0.0)
        if math.isnan(result[time]) or math.isinf(result[time]) or result[time] < 0:
            result[time] = 0.0
    return result


# zakładam, że delta t to 1h i są po kolei
def funkcjaGestaft(brokenElementsAfterTime: dict[int, int], amountOfElementsTotal: int) -> dict[int, float]:
    if amountOfElementsTotal <= 0:
        raise ValueError("Liczba elementów musi być większa od zera")

    result: dict[int, float] = {}
    sorted_times = sorted(brokenElementsAfterTime.keys())

    prevTime = sorted_times[0]
    for time in sorted_times[1:]:
        delta_t = time - prevTime if time > prevTime else 1
        if amountOfElementsTotal * delta_t == 0:
            value = 0.0
        else:
            value = brokenElementsAfterTime.get(time, 0) / (amountOfElementsTotal * delta_t)

        if math.isnan(value) or math.isinf(value) or value < 0:
            value = 0.0

        result[time] = value
        prevTime = time
    return result


def funkcjaIntensywnoscilambdat(brokenElementsAfterTime: dict[int, int], amountOfElementsTotal: int) -> dict[int, float]:
    if amountOfElementsTotal <= 0:
        raise ValueError("Liczba elementów musi być większa od zera")

    result: dict[int, float] = {}
    sorted_times = sorted(brokenElementsAfterTime.keys())

    prevTime = 0
    for time in sorted_times:
        mti = brokenElementsAfterTime.get(time, 0)
        sumPrevious = sum(brokenElementsAfterTime.get(t, 0) for t in range(sorted_times[0], time))
        denominator = amountOfElementsTotal - sumPrevious

        if denominator <= 0:
            value = 0.0
        else:
            value = mti / denominator

        if math.isnan(value) or math.isinf(value) or value < 0:
            value = 0.0

        result[time] = value
        prevTime = time
    return result


def rozkladTrwalosciEta(brokenElementsAfterTime: dict[int, int], amountOfElementsTotal: int) -> float:
    dystrybunata = dystrybunataFt(brokenElementsAfterTime, amountOfElementsTotal)
    sorted_times = sorted(brokenElementsAfterTime.keys())
    suma = 0.0

    for i, time in enumerate(sorted_times[:-1]):
        next_time = sorted_times[i + 1]
        ft_curr = dystrybunata.get(time, 0.0)
        ft_next = dystrybunata.get(next_time, ft_curr)
        dystrybunata_diff = ft_next - ft_curr

        if math.isnan(dystrybunata_diff) or math.isinf(dystrybunata_diff) or dystrybunata_diff < 0:
            dystrybunata_diff = 0.0

        suma += time * dystrybunata_diff

    return suma
