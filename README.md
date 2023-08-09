# Code Comparison Tutorial
Welcome to the Code Comparison Tutorial! This tutorial will guide you through the process of comparing two code snippets and identifying differences using the powerful Levenshtein distance algorithm. Get ready to level up your code comparison skills!
## Technical Overview
The code comparison tutorial utilizes the Levenshtein distance algorithm to measure the differences between lines of code. The Levenshtein distance is a metric that calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to transform one string into another.
### Levenshtein Distance Calculation
The `compare_code` function in the `compare_code.py` file is the heart of the code comparison process. It takes two code snippets, `candidate_code` and `correct_code`, as input and performs the following steps:
  1. Install Levenshtein library first.
```bash
pip install python-Levenshtein
```
  2. Calculate the Levenshtein distance for the entire code: The `Levenshtein.distance` function is used to calculate the Levenshtein distance between the `candidate_code` and `correct_code` strings. This provides an overall measure of the differences between the two code snippets.
  3. Split the codes into lines: The `candidate_code` and `correct_code` strings are split into individual lines using the `split` method with the newline character (`'\n'`) as the delimiter. This allows for line-by-line comparison.
  4. Compare line by line: The code iterates over the lines of both `candidate_code` and `correct_code `using the `enumerate` function combined with `zip`. For each line, it checks if there is a difference between the `candidate_line` and `correct_line`.
  5. Print differences: If a difference is found, the code prints the line number, the `candidate_line`, the `correct_line`, and the Levenshtein distance between them. This provides detailed information about the discrepancies between the code snippets.


## Example Usage
To demonstrate the code comparison process, an example usage is provided in the compare_code.py file. It compares two code snippets, candidate_code and correct_code, and displays the differences, including line numbers and any whitespace discrepancies.

## Getting Started
To get started with the code comparison tutorial, follow the instructions below:

1. Clone the repository:
```bash
git clone https://.git
```

2. Navigate to the project directory:
```bash
cd code-comparison-tutorial
```
3. Open the `compare_code.py` file and replace the `candidate_code` and `correct_code` variables with your own code snippets.

4. Run the code:
```bash
python compare_code.py
```
5. Observe the magic as the code compares the two code.

Let's dive into the exciting world of code comparison and take your skills to the next level!

Happy Coding

Please let me know if there's anything else I can assist you with!
