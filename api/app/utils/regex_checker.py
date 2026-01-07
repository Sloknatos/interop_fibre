import re

def is_code_check_regex(code: str) -> bool:
    pattern = r"^[A-Z0-9]{4}$"
    return True if re.match(pattern, code) else False