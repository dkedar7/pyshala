# Code Lessons

Code lessons provide an interactive editor where learners write and execute Python code.

## Basic Structure

```yaml
title: "Hello, World!"
description: "Your first Python program"
order: 0

instructions: |
  # Hello, World!

  Write a program that prints "Hello, World!"

  ```python
  print("Hello, World!")
  ```

starter_code: |
  # Write your code below


test_cases:
  - description: "Prints greeting"
    expected_output: "Hello, World!"
```

## Lesson Fields

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Lesson title |
| `description` | No | Short description |
| `order` | No | Sort order (default: 0) |
| `instructions` | Yes | Markdown content |
| `starter_code` | No | Initial code in editor |
| `test_cases` | Yes | List of test cases |
| `instructions_file` | No | External markdown file |
| `data_files` | No | List of data files |

## Test Cases

### Basic Test Case

```yaml
test_cases:
  - description: "Prints hello"
    stdin: ""
    expected_output: "hello"
```

### Test Case with Input

```yaml
test_cases:
  - description: "Doubles the number"
    stdin: "5"
    expected_output: "10"

  - description: "Handles negative"
    stdin: "-3"
    expected_output: "-6"
```

### Multiple Lines of Input

```yaml
test_cases:
  - description: "Adds two numbers"
    stdin: "5\n3"  # Two lines
    expected_output: "8"
```

### Hidden Test Cases

Hidden tests validate without showing details to learners:

```yaml
test_cases:
  - description: "Basic test"
    stdin: "5"
    expected_output: "25"

  - description: "Edge case"
    stdin: "0"
    expected_output: "0"
    hidden: true  # Not shown to learner
```

!!! tip "Anti-Cheating"
    Include at least one hidden test case to prevent learners from hardcoding answers.

### Test Case Fields

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| `description` | Yes | - | What the test verifies |
| `stdin` | No | "" | Input to the program |
| `expected_output` | Yes | - | Expected stdout |
| `hidden` | No | false | Hide test details |

### Output Matching

- Trailing whitespace is trimmed
- Newlines within output are preserved
- Comparison is exact (case-sensitive)

## Data Files

Include CSV, JSON, or other files:

```yaml
title: "Working with CSV"
instructions: |
  The file `sales.csv` is available in your working directory.

  ```python
  import csv
  with open('sales.csv') as f:
      reader = csv.reader(f)
      for row in reader:
          print(row)
  ```

data_files:
  - name: sales.csv
    path: sales.csv

test_cases:
  - description: "Calculates total"
    expected_output: "1500"
```

Place data files in the same directory as the lesson YAML.

## Complete Example

```yaml title="03_input_output.yaml"
title: "Input and Output"
description: "Get input from users"
order: 2

instructions: |
  # Input and Output

  Programs often need to interact with users.

  ## Getting Input

  Use `input()` to get text from the user:

  ```python
  name = input()
  print("Hello, " + name)
  ```

  ## Converting Input

  `input()` always returns a string. Convert to numbers:

  ```python
  age = int(input())
  next_year = age + 1
  print(next_year)
  ```

  ## Your Task

  Read a number from input, double it, and print the result.

starter_code: |
  # Read a number, double it, and print


test_cases:
  - description: "Doubles 5 to get 10"
    stdin: "5"
    expected_output: "10"

  - description: "Doubles 0 to get 0"
    stdin: "0"
    expected_output: "0"

  - description: "Handles larger numbers"
    stdin: "100"
    expected_output: "200"
    hidden: true
```

## Tips

### Starter Code

- Provide helpful comments
- Include structure for complex tasks
- Don't give away the solution

```yaml
# Good - gives structure without solution
starter_code: |
  # Get user input

  # Calculate result

  # Print output


# Bad - too much help
starter_code: |
  num = int(input())
  result = num * 2  # just uncomment
  # print(result)
```

### Instructions

- Start with concept explanation
- Show working examples
- End with clear task description
- Be explicit about expected output format

### Test Cases

- Start with simple cases
- Include edge cases (0, negative, empty)
- Add hidden tests for anti-cheating
- Use descriptive test names
