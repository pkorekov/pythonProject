

from src.functions import read_json



def test_read_json(path_to_test_json, expected_result_for_read_json_test):
    assert read_json(path_to_test_json) == expected_result_for_read_json_test

