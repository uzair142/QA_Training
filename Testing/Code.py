def count(sequence, item):
    count = 0
    for n in sequence:
        if n == item:
            count += 1
    return count

def test_count_integers():
    # Test the count function with a list of integers
    input_list = [1, 2, 2, 3, 4, 2, 5]
    item_to_count = 2
    assert count(input_list, item_to_count) == 3

def test_count_strings():
    # Test the count function with a list of strings
    input_list = ["apple", "banana", "cherry", "banana", "apple"]
    item_to_count = "apple"
    assert count(input_list, item_to_count) == 2
