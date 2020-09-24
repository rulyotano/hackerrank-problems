from common.binary_search import binary_search, is_insert_index

fakeRandomList = [1, 5, 7, 10, 16, 21, 33, 45, 46, 47, 50]
fakeSmall = [1, 5, 11, 16]
fakeSmallOdd = [1, 5, 11]
fakeTwo = [5, 11]


def test_should_return_minus_one_when_no_found():
    assert binary_search(fakeSmall, lambda a, _: 6 - a) == -1


def test_should_no_found_greater():
    assert binary_search(fakeSmall, lambda a, _: 20 - a) == -1


def test_should_no_found_lower():
    assert binary_search(fakeSmall, lambda a, _: 0 - a) == -1


def test_should_return_the_index_of_the_found_item():
    assert binary_search(fakeSmall, lambda a, _: 11 - a) == 2


def test_should_return_the_of_item_in_the_middle():
    assert binary_search(fakeSmallOdd, lambda a, _: 5 - a) == 1


def test_should_return_item_5():
    assert binary_search(fakeTwo, lambda a, _: 5 - a) == 0


def test_should_return_item_11():
    assert binary_search(fakeTwo, lambda a, _: 11 - a) == 1


def test_should_return_empty():
    assert binary_search([], lambda a, _: 11 - a) == -1


def test_find_best_index_to_insert():
    assert binary_search(fakeTwo, lambda item,
                         index: is_insert_index(7, fakeTwo, index)) == 1


def test_find_best_index_to_insert_should_be_0():
    assert binary_search(fakeTwo, lambda item,
                         index: is_insert_index(3, fakeTwo, index)) == 0


def test_find_best_index_to_insert_at_the_end_should_be_minus_one():
    assert binary_search(fakeTwo, lambda item,
                         index: is_insert_index(20, fakeTwo, index)) == -1
