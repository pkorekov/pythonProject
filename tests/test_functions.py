
from src.functions import read_json, sort_data, format_from_account, format_to_account, format_date



def test_read_json(path_to_test_json, expected_result_for_read_json_test):
    assert read_json(path_to_test_json) == expected_result_for_read_json_test

def test_sort_data(data_for_sort, expected_result_for_sort):
    assert sort_data(data_for_sort) == expected_result_for_sort


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

def test_format_date():
    formatted_date = format_date('2023-05-20T08:30:00')
    assert format_date('2019-02-14T17:38:09.910336') == '14.02.2019'
    assert format_date('2018-08-14T05:42:30.104666') == '14.08.2018'
    assert format_date('2019-03-29T10:57:20.635567') == '29.03.2019'
    assert format_date('2019-06-16T22:17:01.825020') == '16.06.2019'
