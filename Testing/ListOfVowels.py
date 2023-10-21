def list_of_squares(n):
    d = dict()
    for i in range(1, n + 1):
        d[i] = i * i
    return d

def test_list_of_squares_positive():
    n = 5
    result = list_of_squares(n)
    expected = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert result == expected

def test_list_of_squares_zero():
    n = 0
    result = list_of_squares(n)
    expected = {}
    assert result == expected
