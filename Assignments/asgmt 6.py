def find_uppercase_chars():
    elements = input("Enter a list of elements separated by spaces: ").split()
    uppercase_chars = [char for element in elements for char in element if char.isupper()]
    return uppercase_chars
print(find_uppercase_chars())

def find_numeric_elements():
    elements = input("Enter a list of elements separated by spaces: ").split()
    numeric_elements = [element for element in elements if element.isdigit()]
    return numeric_elements
print(find_numeric_elements())

def replace_numeric_with_zero(elements):
    replaced_elements = [element if not element.isdigit() else '0' for element in elements]
    return replaced_elements
elements = ["Hello", "123", "World", "456", "789", "Python"]
print(replace_numeric_with_zero(elements))

import re
def validate_username(username):
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{2,19}$'
    return re.match(pattern, username) is not None
print(validate_username("Valid_Username123"))  # True
print(validate_username("InvalidUsername!@#"))  # False

def display_matched_elements(elements):
    pattern = re.compile(r'^[a-zA-Z]+$')
    matched_elements = [element for element in elements if pattern.match(element)]
    return matched_elements
elements = ["Hello", "123", "World", "456", "Python3", "Programming"]
print(display_matched_elements(elements))
