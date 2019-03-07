import re


check_re = re.compile(r"^[a-zA-Z0-9_]*$")

def check_path_valid(path):
    return check_re.match(path)
