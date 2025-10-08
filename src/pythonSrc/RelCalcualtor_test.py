import pytest
from RelCalcualtor import dystrybunataFt



brokenElemntsAfterTime: dict[int,int ] = {
    1:0,
    2:3,
    3:3,
    4:5,
    5:8,
    6:7,
    7:6,
    8:2,
    9:1,
    10:0
    }
totalElemets = 35


def round_dict_values(d: dict) -> dict:
    return {k: round(v, 3) for k, v in d.items()}


def test_dystrybunataFt():
    result = dystrybunataFt(brokenElemntsAfterTime,totalElemets)
    expected = {1:0,
                2:0.086,
                3:0.171,
                4:0.314,
                5:0.543,
                6:0.743,
                7:0.914,
                8:0.971,
                9:1,
                10:1  
                }
    print(result)
    result = round_dict_values(result)
    for k, v in result.items():
        print(k, v)
    assert result == expected


def test_funkcjaNiezawdnosciRt():
    result = funkcjaNiezawdnosciRt(brokenElemntsAfterTime)
    expected = {1:1,
                2:0.914,
                3:0.828,
                4:0.686,
                5:0.457,
                6:0.257,
                7:0.086,
                8:0.029,
                9:0,
                10:0  
                }
    assert result == expected


def test_funkcjaGestaft():
        result = funkcjaGestaft(brokenElemntsAfterTime)
        expected = {1:0,
                    2:0.086,
                    3:0.086,
                    4:0.143,
                    5:0.228,
                    6:0.2,
                    7:0.171,
                    8:0.057,
                    9:0.0286, 
                    }
        assert result == expected
    

def test_funkcjaIntensywnoscilambdat():
        result = funkcjaIntensywnoscilambdat(brokenElemntsAfterTime)
        expected = {1:0,
                    2:0.086,
                    3:0.095,
                    4:0.172,
                    5:0.323,
                    6:0.437,
                    7:0.667,
                    8:0.607,
                    9:1.0, 
                    }
        assert result == expected


def test_rozkladTrwalosciEta():
    result = rozkladTrwalosciEta(brokenElemntsAfterTime)
    assert result == 4.3