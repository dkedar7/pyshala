# Writing Lessons for PyShala

This guide explains how to create lessons for PyShala. Use this as a reference for manually creating lessons or as a prompt for LLMs to generate lessons automatically.

## Directory Structure

Lessons are organized into **modules** (folders) containing **lessons** (YAML files):

```
lessons/
├── module_id/                    # Module folder (use snake_case)
│   ├── module.yaml               # Module metadata (optional)
│   ├── 01_lesson_id.yaml         # Lesson file
│   ├── 02_another_lesson.yaml    # Another lesson
│   └── data.csv                  # Optional data files
└── another_module/
    ├── module.yaml
    └── 01_intro.yaml
```

## Module Configuration

Create a `module.yaml` file in each module folder:

```yaml
name: "Python Basics"
description: "Learn fundamental Python concepts including variables, data types, and basic operations"
order: 1  # Determines module order on home page (lower = first)

# Optional: Explicitly list lessons in order
# If omitted, lessons are sorted alphabetically by filename
lessons:
  - 01_hello_world.yaml
  - 02_variables.yaml
  - 03_data_types.yaml
```

### Module Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Display name for the module |
| `description` | Yes | Brief description shown on module card |
| `order` | No | Sort order (default: 0) |
| `lessons` | No | Ordered list of lesson filenames |

## Lesson Configuration

Each lesson is a YAML file with the following structure:

```yaml
title: "Hello, World!"
description: "Write your first Python program"
order: 0

instructions: |
  # Hello, World!

  Every programmer's journey begins with a simple program that displays
  "Hello, World!" on the screen.

  ## The print() Function

  In Python, we use the `print()` function to display text:

  ```python
  print("Hello, World!")
  ```

  The text inside the quotes is called a **string**.

  ## Your Task

  Write a program that prints exactly: `Hello, World!`

starter_code: |
  # Write your code below


test_cases:
  - description: "Prints 'Hello, World!'"
    stdin: ""
    expected_output: "Hello, World!"
```

### Lesson Fields

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Lesson title displayed in header |
| `description` | No | Short description for lesson list |
| `order` | No | Sort order within module (default: 0) |
| `instructions` | Yes | Markdown content explaining the lesson |
| `starter_code` | No | Initial code in the editor |
| `test_cases` | Yes | List of test cases (at least one) |
| `instructions_file` | No | External markdown file for instructions |
| `data_files` | No | List of data files to include |

## Writing Instructions

Instructions use **Markdown** format. Best practices:

### Structure

```yaml
instructions: |
  # Main Topic

  Brief introduction to the concept.

  ## Key Concept 1

  Explanation with example:

  ```python
  # Example code
  x = 5
  print(x)
  ```

  ## Key Concept 2

  More explanation...

  ## Your Task

  Clear instructions on what the learner should do.

  **Expected output:**
  ```
  Expected output here
  ```
```

### Markdown Features Supported

- Headers (`#`, `##`, `###`)
- Code blocks (``` python ```)
- Inline code (`` `code` ``)
- Bold (`**text**`)
- Italic (`*text*`)
- Lists (ordered and unordered)
- Tables
- Links

### External Instructions File

For longer instructions, use a separate markdown file:

```yaml
title: "Complex Lesson"
instructions_file: "complex_lesson_instructions.md"
starter_code: |
  # Your code here
test_cases:
  - description: "Test"
    expected_output: "result"
```

## Test Cases

Test cases validate the learner's code by comparing output.

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
  - description: "Doubles the input number"
    stdin: "5"
    expected_output: "10"

  - description: "Handles negative numbers"
    stdin: "-3"
    expected_output: "-6"
```

### Hidden Test Cases

Hidden tests validate without showing details to learners:

```yaml
test_cases:
  - description: "Basic test"
    stdin: "5"
    expected_output: "25"

  - description: "Edge case (hidden)"
    stdin: "0"
    expected_output: "0"
    hidden: true
```

### Test Case Fields

| Field | Required | Description |
|-------|----------|-------------|
| `description` | Yes | What this test verifies |
| `stdin` | No | Input provided to the program (default: "") |
| `expected_output` | Yes | Expected stdout (whitespace-trimmed) |
| `hidden` | No | Hide test details from learner (default: false) |

### Output Matching

- Trailing whitespace is trimmed from both actual and expected output
- Newlines within output are preserved
- Comparison is exact (case-sensitive)

## Data Files

Include CSV, JSON, or other files for lessons:

```yaml
title: "Reading CSV Files"
instructions: |
  # Working with CSV Files

  The file `sales.csv` is available in your working directory.

  ```python
  import csv

  with open('sales.csv') as f:
      reader = csv.reader(f)
      for row in reader:
          print(row)
  ```

starter_code: |
  import csv

  # Read and process sales.csv


data_files:
  - name: sales.csv
    path: sales.csv

test_cases:
  - description: "Calculates total sales"
    expected_output: "1500"
```

Place the data file in the same directory as the lesson YAML:

```
lessons/
└── data_analysis/
    ├── module.yaml
    ├── 01_csv_basics.yaml
    └── sales.csv          # Referenced by data_files
```

## Complete Example

Here's a complete module with multiple lessons:

### Directory Structure

```
lessons/
└── python_basics/
    ├── module.yaml
    ├── 01_hello_world.yaml
    ├── 02_variables.yaml
    └── 03_input_output.yaml
```

### module.yaml

```yaml
name: "Python Basics"
description: "Start your Python journey with fundamental concepts"
order: 1

lessons:
  - 01_hello_world.yaml
  - 02_variables.yaml
  - 03_input_output.yaml
```

### 01_hello_world.yaml

```yaml
title: "Hello, World!"
description: "Your first Python program"
order: 0

instructions: |
  # Hello, World!

  Let's write your first Python program!

  ## The print() Function

  Use `print()` to display text on the screen:

  ```python
  print("Hello, World!")
  ```

  ## Your Task

  Print exactly: `Hello, World!`

starter_code: |
  # Type your code below


test_cases:
  - description: "Prints 'Hello, World!'"
    stdin: ""
    expected_output: "Hello, World!"
```

### 02_variables.yaml

```yaml
title: "Variables"
description: "Store and use data with variables"
order: 1

instructions: |
  # Variables

  Variables store data that you can use later in your program.

  ## Creating Variables

  ```python
  name = "Alice"
  age = 25
  height = 5.6
  ```

  ## Using Variables

  ```python
  print(name)    # Output: Alice
  print(age)     # Output: 25
  ```

  ## Your Task

  Create a variable called `message` with the value `"Python is fun!"`
  and print it.

starter_code: |
  # Create your variable and print it


test_cases:
  - description: "Prints the message"
    stdin: ""
    expected_output: "Python is fun!"
```

### 03_input_output.yaml

```yaml
title: "Input and Output"
description: "Get input from users and display results"
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

  `input()` always returns a string. Convert to numbers with `int()` or `float()`:

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

## Tips for Writing Good Lessons

### Content Guidelines

1. **Start simple** - Build complexity gradually
2. **One concept per lesson** - Focus on a single skill
3. **Show examples** - Include working code snippets
4. **Clear tasks** - Be explicit about expected output
5. **Multiple test cases** - Cover edge cases

### Test Case Guidelines

1. **Descriptive names** - "Handles negative numbers" not "Test 3"
2. **Start with basic cases** - Simple inputs first
3. **Include edge cases** - Zero, empty strings, boundaries
4. **Use hidden tests** - For anti-cheating or complex validation
5. **Match exact output** - Be precise about formatting

### Common Patterns

#### Echo input
```yaml
test_cases:
  - stdin: "hello"
    expected_output: "hello"
```

#### Calculation
```yaml
test_cases:
  - stdin: "5\n3"      # Two numbers on separate lines
    expected_output: "8"
```

#### Multiple outputs
```yaml
test_cases:
  - stdin: ""
    expected_output: |
      Line 1
      Line 2
      Line 3
```

#### No input required
```yaml
test_cases:
  - stdin: ""
    expected_output: "Fixed output"
```

## LLM Prompt Template

Use this prompt to generate lessons with an LLM:

```
Create a PyShala lesson about [TOPIC].

Requirements:
- Title: Clear, concise lesson title
- Description: One sentence summary
- Instructions: Markdown with:
  - Concept explanation
  - Code examples
  - Clear task description
- Starter code: Minimal template with comments
- Test cases: At least 3, including edge cases

Format as YAML following this structure:

title: "..."
description: "..."
order: N

instructions: |
  # Topic

  [Explanation]

  ## Your Task

  [What to do]

starter_code: |
  # Your code here


test_cases:
  - description: "..."
    stdin: "..."
    expected_output: "..."
```

## Validation Checklist

Before deploying lessons, verify:

- [ ] Module has `module.yaml` with name and description
- [ ] All lesson files are valid YAML
- [ ] Each lesson has title, instructions, and test_cases
- [ ] Test cases have description and expected_output
- [ ] Starter code runs without errors (even if incomplete)
- [ ] Instructions are clear and well-formatted
- [ ] All referenced data files exist
- [ ] Lessons are ordered correctly
