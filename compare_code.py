import Levenshtein

def compare_code(candidate_code, correct_code):
    # Calculate the Levenshtein distance for the entire code
    code_distance = Levenshtein.distance(candidate_code, correct_code)
    print("Levenshtein distance for the entire code:", code_distance)
    print()

    # Split the codes into lines
    candidate_lines = candidate_code.split('\n')
    correct_lines = correct_code.split('\n')

    # Compare line by line
    for i, (candidate_line, correct_line) in enumerate(zip(candidate_lines, correct_lines)):
        if candidate_line != correct_line:
            print(f"Line {i + 1} has an issue:")
            print("Candidate code:", candidate_line)
            print("Correct code:", correct_line)
            print("Levenshtein distance:", Levenshtein.distance(candidate_line, correct_line))
            print()

# Example usage
candidate_code = '''
def add_numbers(a, b):
    return a + b

de multiply_numbers(a, b):
    return a - b
'''

correct_code = '''
def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b
'''


compare_code(candidate_code, correct_code
