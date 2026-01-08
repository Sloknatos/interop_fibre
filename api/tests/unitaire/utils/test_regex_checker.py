from app.utils.regex_checker import is_code_check_regex


def describe_regex_checker():
    def it_return_true(mocker):
        mocker.patch('re.match', return_value=True)
        assert is_code_check_regex("text too long") == True
    def it_return_false(mocker):
        mocker.patch('re.match', return_value=False)
        assert is_code_check_regex("text") == False