
from src.functions import read_json, sort_data, format_from_account, format_to_account



def test_read_json(path_to_test_json, expected_result_for_read_json_test):
    assert read_json(path_to_test_json) == expected_result_for_read_json_test

def test_sort_data(data_for_sort, expected_result_for_sort):
    assert sort_data(data_for_sort) == expected_result_for_sort

#def test_mask_card_number(number_for_card, expected_result_for_card):
    #assert mask_card_number(number_for_card) == expected_result_for_card

def test_format_from_account():
    assert format_from_account('Счет 1234567890123456') == 'Счет 1234 56** **** 3456'
    assert format_from_account('Счет 12345678901234567890') == 'Счет 1234 56** **** 7890'
    assert format_from_account('МИР 1234567890123456') == 'МИР 1234 56** **** 3456'
    assert format_from_account('МИР 12345678901234567890') == 'МИР 1234 56** **** 7890'
    assert format_from_account('Visa Platinum 1234567890123456') == 'Visa Platinum 1234 56** **** 3456'
    assert format_from_account('Visa Platinum 12345678901234567890') == 'Visa Platinum 1234 56** **** 7890'
    assert format_from_account('Visa Classic 1234567890123456') == 'Visa Classic 1234 56** **** 3456'
    assert format_from_account('Visa Classic 12345678901234567890') == 'Visa Classic 1234 56** **** 7890'
    assert format_from_account('Visa Gold 1234567890123456') == 'Visa Gold 1234 56** **** 3456'
    assert format_from_account('Visa Gold 12345678901234567890') == 'Visa Gold 1234 56** **** 7890'

def test_format_to_account():
    assert format_to_account('Счет 1234567890123456') == 'Счет **3456'
    assert format_to_account('Счет 12345678901234567890') == 'Счет **7890'
    assert format_to_account('МИР 1234567890123456') == 'МИР **3456'
    assert format_to_account('МИР 12345678901234567890') == 'МИР **7890'
    assert format_to_account('Visa Platinum 1234567890123456') == 'Visa Platinum **3456'
    assert format_to_account('Visa Platinum 12345678901234567890') == 'Visa Platinum **7890'
    assert format_to_account('Visa Classic 1234567890123456') == 'Visa Classic **3456'
    assert format_to_account('Visa Classic 12345678901234567890') == 'Visa Classic **7890'
    assert format_to_account('Visa Gold 1234567890123456') == 'Visa Gold **3456'
    assert format_to_account('Visa Gold 12345678901234567890') == 'Visa Gold **7890'


