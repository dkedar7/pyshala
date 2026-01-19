# Writing Lessons for PyShala

This guide explains how to create lessons for PyShala. Use this as a reference for manually creating lessons or as a prompt for LLMs to generate lessons automatically.

## Lesson Types

PyShala supports two types of lessons:

| Type | Description | Use Case |
|------|-------------|----------|
| **Code** | Interactive coding exercises with a code editor | Teaching programming concepts through practice |
| **Quiz** | Multiple choice (MCQ) and text-based questions | Testing knowledge, reviewing concepts, assessments |

## Directory Structure

Lessons are organized into **modules** (folders) containing **lessons** (YAML files):

```
lessons/
├── config.yaml                   # App configuration (optional)
├── module_id/                    # Module folder (use snake_case)
│   ├── module.yaml               # Module metadata (optional)
│   ├── 01_lesson_id.yaml         # Lesson file
│   ├── 02_another_lesson.yaml    # Another lesson
│   └── data.csv                  # Optional data files
└── another_module/
    ├── module.yaml
    └── 01_intro.yaml
```

## App Configuration

Customize the app's title, subtitle, and navigation by creating a `config.yaml` file in your lessons directory:

```yaml
# App identity
title: "PyShala"
subtitle: "Learn Python, One Lesson at a Time"
description: "Interactive lessons with hands-on coding exercises and instant feedback"

# Navigation
about_url: "https://github.com/dkedar7/pyshala"
about_text: "About"

# Branding (icon name from Lucide icons)
icon: "graduation-cap"
```

### Config Fields

| Field | Default | Description |
|-------|---------|-------------|
| `title` | "PyShala" | App name displayed in the navbar |
| `subtitle` | "Learn Python, One Lesson at a Time" | Heading shown on the home page |
| `description` | "Interactive lessons with hands-on coding exercises and instant feedback" | Subtext under the subtitle |
| `about_url` | "https://github.com/dkedar7/pyshala" | URL for the About link |
| `about_text` | "About" | Text for the About link |
| `icon` | "graduation-cap" | Lucide icon name for the navbar (see [Lucide Icons](https://lucide.dev/icons)) |

### Config File Location

PyShala searches for `config.yaml` in the following order:

1. Path specified in `PYSHALA_CONFIG` environment variable
2. `config.yaml` in the lessons directory (`LESSONS_PATH`)
3. `config.yaml` in the current working directory
4. `lessons/config.yaml` relative to the current directory

If no config file is found, default values are used.

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
| `type` | No | Lesson type: `"code"` (default) or `"quiz"` |
| `description` | No | Short description for lesson list |
| `order` | No | Sort order within module (default: 0) |
| `instructions` | Yes | Markdown content explaining the lesson |
| `starter_code` | No | Initial code in the editor (code lessons only) |
| `test_cases` | No | List of test cases (code lessons only) |
| `questions` | No | List of quiz questions (quiz lessons only) |
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

## Quiz Lessons

Quiz lessons test learners' knowledge through multiple choice questions (MCQ) and text-based questions.

### Basic Quiz Structure

```yaml
title: "Python Basics Quiz"
type: "quiz"
description: "Test your understanding of Python fundamentals"
order: 5

instructions: |
  # Python Basics Quiz

  Answer the following questions to test what you've learned.

  - For multiple choice, select the best answer
  - For text questions, type your answer exactly

questions:
  - id: "q1"
    type: "mcq"
    text: "What function displays output in Python?"
    multi_select: false
    options:
      - id: "a"
        text: "echo()"
      - id: "b"
        text: "print()"
      - id: "c"
        text: "write()"
      - id: "d"
        text: "display()"
    correct: ["b"]

  - id: "q2"
    type: "text"
    text: "What is the output of: print(2 + 3)"
    correct: ["5"]
```

### Question Types

#### Multiple Choice - Single Select

Radio button style where learners select **one** answer:

```yaml
- id: "q1"
  type: "mcq"
  text: "What is the correct way to create a variable?"
  multi_select: false
  options:
    - id: "a"
      text: "var x = 5"
    - id: "b"
      text: "x = 5"
    - id: "c"
      text: "int x = 5"
    - id: "d"
      text: "let x = 5"
  correct: ["b"]
```

#### Multiple Choice - Multi Select

Checkbox style where learners can select **multiple** answers:

```yaml
- id: "q2"
  type: "mcq"
  text: "Which are valid Python data types? (Select all that apply)"
  multi_select: true
  options:
    - id: "a"
      text: "int"
    - id: "b"
      text: "string"
    - id: "c"
      text: "str"
    - id: "d"
      text: "float"
  correct: ["a", "c", "d"]  # Multiple correct answers
```

#### Text Input

Free-form text answers with case-insensitive matching:

```yaml
- id: "q3"
  type: "text"
  text: "What symbol starts a comment in Python?"
  correct: ["#", "hash", "pound"]  # Multiple acceptable answers
```

### Question Fields

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Unique identifier (e.g., "q1", "q2") |
| `type` | Yes | Question type: `"mcq"` or `"text"` |
| `text` | Yes | The question text |
| `options` | MCQ only | List of answer options |
| `multi_select` | MCQ only | `true` for checkboxes, `false` for radio (default: false) |
| `correct` | Yes | List of correct answer(s) |

### Option Fields (for MCQ)

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Unique identifier (e.g., "a", "b", "c") |
| `text` | Yes | The option text displayed to learner |

### Answer Validation

- **MCQ**: Exact match of selected option IDs (order doesn't matter for multi-select)
- **Text**: Case-insensitive match against any answer in the `correct` list
- **Whitespace**: Leading/trailing whitespace is trimmed before comparison

### Complete Quiz Example

```yaml
title: "Control Flow Quiz"
type: "quiz"
description: "Test your knowledge of if statements and loops"
order: 10

instructions: |
  # Control Flow Quiz

  This quiz covers conditional statements and loops in Python.

  **Tips:**
  - Read each question carefully
  - For multi-select questions, choose ALL correct answers
  - Text answers are not case-sensitive

questions:
  - id: "q1"
    type: "mcq"
    text: "Which keyword starts a conditional statement in Python?"
    multi_select: false
    options:
      - id: "a"
        text: "when"
      - id: "b"
        text: "if"
      - id: "c"
        text: "case"
      - id: "d"
        text: "switch"
    correct: ["b"]

  - id: "q2"
    type: "mcq"
    text: "Which are valid loop types in Python? (Select all)"
    multi_select: true
    options:
      - id: "a"
        text: "for"
      - id: "b"
        text: "while"
      - id: "c"
        text: "do-while"
      - id: "d"
        text: "foreach"
    correct: ["a", "b"]

  - id: "q3"
    type: "text"
    text: "What keyword exits a loop early?"
    correct: ["break"]

  - id: "q4"
    type: "text"
    text: "What keyword skips to the next iteration?"
    correct: ["continue"]

  - id: "q5"
    type: "mcq"
    text: "What does 'elif' stand for?"
    multi_select: false
    options:
      - id: "a"
        text: "else if"
      - id: "b"
        text: "else info"
      - id: "c"
        text: "element if"
      - id: "d"
        text: "evaluate if"
    correct: ["a"]
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

### Quiz Question Guidelines

1. **Clear, unambiguous wording** - Avoid tricky phrasing
2. **One concept per question** - Don't test multiple things at once
3. **Plausible distractors** - Wrong answers should be reasonable mistakes
4. **Consistent option length** - Similar length options prevent guessing
5. **Multiple acceptable answers for text** - Account for synonyms and variations

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

## LLM Prompt Templates

Use these prompts to generate lessons with an LLM.

### Code Lesson Prompt

```
Create a PyShala CODE lesson about [TOPIC].

Requirements:
- Title: Clear, concise lesson title
- Description: One sentence summary
- Instructions: Markdown with:
  - Concept explanation
  - Code examples
  - Clear task description
- Starter code: Minimal template with comments
- Test cases: At least 3, including edge cases and one hidden test

Format as YAML:

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
  - description: "Edge case"
    stdin: "..."
    expected_output: "..."
  - description: "Hidden test"
    stdin: "..."
    expected_output: "..."
    hidden: true
```

### Quiz Lesson Prompt

```
Create a PyShala QUIZ lesson about [TOPIC].

Requirements:
- Title: Clear quiz title
- Description: One sentence summary
- Instructions: Brief intro explaining the quiz
- Questions: 5-10 questions mixing:
  - MCQ single-select (most common misconceptions as distractors)
  - MCQ multi-select (for "select all that apply")
  - Text input (for keywords, symbols, short answers)
- Each question tests ONE concept
- Distractors should be plausible mistakes

Format as YAML:

title: "[Topic] Quiz"
type: "quiz"
description: "Test your understanding of [topic]"
order: N

instructions: |
  # [Topic] Quiz

  Answer the following questions to test your knowledge.

questions:
  - id: "q1"
    type: "mcq"
    text: "Question text?"
    multi_select: false
    options:
      - id: "a"
        text: "Option A"
      - id: "b"
        text: "Option B"
      - id: "c"
        text: "Option C"
      - id: "d"
        text: "Option D"
    correct: ["b"]

  - id: "q2"
    type: "mcq"
    text: "Select all that apply?"
    multi_select: true
    options:
      - id: "a"
        text: "Option A"
      - id: "b"
        text: "Option B"
      - id: "c"
        text: "Option C"
    correct: ["a", "c"]

  - id: "q3"
    type: "text"
    text: "What keyword does X?"
    correct: ["answer", "alternate_answer"]
```

### Complete Module Prompt

```
Create a complete PyShala module about [TOPIC] for [AUDIENCE].

The module should include:
1. Introduction lesson (code) - basic concept with guided exercise
2. Practice lesson (code) - 2-3 exercises with less scaffolding
3. Advanced lesson (code) - challenging problem
4. Quiz lesson - 5-8 questions reviewing all concepts

For each lesson, follow the appropriate format (code or quiz).
Ensure logical progression from simple to complex.
Test cases should cover edge cases and include hidden tests.
Quiz questions should test understanding, not just recall.

Start with module.yaml, then each lesson file.
```

## Building Effective Modules

This section provides guidance on structuring modules, choosing lesson types, and creating a cohesive learning experience.

### Module Structure Recommendations

A well-structured module follows a logical progression:

```
module/
├── 01_introduction.yaml      # Concept explanation (code)
├── 02_basic_practice.yaml    # Simple exercises (code)
├── 03_intermediate.yaml      # More complex tasks (code)
├── 04_advanced.yaml          # Challenging problems (code)
└── 05_module_quiz.yaml       # Knowledge check (quiz)
```

**Recommended pattern:**
1. **Introduce** - Explain the concept with examples
2. **Practice** - 2-4 coding exercises of increasing difficulty
3. **Assess** - End with a quiz to reinforce learning

### When to Use Each Lesson Type

| Lesson Type | Best For | Example Topics |
|-------------|----------|----------------|
| **Code** | Hands-on practice, problem-solving, syntax learning | Writing functions, debugging, algorithms |
| **Quiz** | Concept review, terminology, theory, quick assessments | Data types, keyword meanings, best practices |

**Use code lessons when:**
- Learners need to practice writing/modifying code
- The skill requires hands-on repetition
- You want to test problem-solving ability
- Output can be objectively verified

**Use quiz lessons when:**
- Testing recall of terminology or concepts
- Reviewing theory before practice
- Quick knowledge checks between sections
- Testing understanding of "why" not just "how"

### Designing Good Code Exercises

#### Start with Clear Learning Objectives

Before writing a lesson, ask:
- What specific skill should learners gain?
- What's the minimum code needed to demonstrate this skill?
- What mistakes are learners likely to make?

#### Progression of Difficulty

**Level 1 - Guided:** Provide most of the code, learner fills in one piece
```yaml
starter_code: |
  name = "Alice"
  # Print a greeting using the name variable
  print(_____)
```

**Level 2 - Scaffolded:** Provide structure, learner writes the logic
```yaml
starter_code: |
  # Get a number from user
  # Calculate and print its square
```

**Level 3 - Open:** Minimal guidance, learner designs solution
```yaml
starter_code: |
  # Your code here
```

#### Writing Effective Test Cases

**Cover the spectrum:**
```yaml
test_cases:
  # Basic case - what most learners will try first
  - description: "Basic input"
    stdin: "5"
    expected_output: "25"

  # Edge case - boundaries and special values
  - description: "Zero input"
    stdin: "0"
    expected_output: "0"

  # Negative case - common mistake scenario
  - description: "Negative number"
    stdin: "-3"
    expected_output: "9"

  # Hidden case - prevents hardcoding
  - description: "Larger number"
    stdin: "12"
    expected_output: "144"
    hidden: true
```

**Avoid these test case mistakes:**
- Testing only the "happy path"
- Using inputs that can be guessed from description
- Forgetting edge cases (0, empty string, negative numbers)
- Making all tests visible (encourages hardcoding)

### Designing Good Quiz Questions

#### MCQ Best Practices

**Good question characteristics:**
- Tests understanding, not just memorization
- Has one clearly correct answer (for single-select)
- Distractors are plausible but clearly wrong to those who understand

**Example of a good MCQ:**
```yaml
- id: "q1"
  type: "mcq"
  text: "What will print(type(3.14)) output?"
  options:
    - id: "a"
      text: "<class 'int'>"
    - id: "b"
      text: "<class 'float'>"
    - id: "c"
      text: "<class 'str'>"
    - id: "d"
      text: "<class 'number'>"
  correct: ["b"]
```

**Why it's good:**
- Tests understanding of data types
- Each distractor represents a common misconception
- Clear, unambiguous wording

**Example of a poor MCQ:**
```yaml
# BAD - Avoid this pattern
- id: "q1"
  type: "mcq"
  text: "Which is best?"  # Subjective
  options:
    - id: "a"
      text: "A"  # Too short, no context
    - id: "b"
      text: "B is the correct answer because it's better"  # Obviously correct
    - id: "c"
      text: "C"
    - id: "d"
      text: "None of the above"  # Lazy option
  correct: ["b"]
```

#### Multi-Select Guidelines

Use multi-select when multiple answers are genuinely correct:

```yaml
- id: "q1"
  type: "mcq"
  text: "Which are mutable data types in Python? (Select all)"
  multi_select: true
  options:
    - id: "a"
      text: "list"
    - id: "b"
      text: "tuple"
    - id: "c"
      text: "dict"
    - id: "d"
      text: "str"
  correct: ["a", "c"]
```

**Multi-select tips:**
- Clearly indicate that multiple answers are expected
- Have 2-3 correct answers (not just 1, not all)
- Test related concepts together

#### Text Question Guidelines

Text questions work best for:
- Short, definitive answers (keywords, symbols, numbers)
- Answers that have limited correct variations

```yaml
# Good text question
- id: "q1"
  type: "text"
  text: "What keyword defines a function in Python?"
  correct: ["def"]

# Good with multiple acceptable answers
- id: "q2"
  type: "text"
  text: "What symbol is used for comments?"
  correct: ["#", "hash", "hashtag", "pound"]

# Poor text question - too open-ended
- id: "q3"
  type: "text"
  text: "Explain what a variable is"  # Can't validate free-form explanations
  correct: ["..."]  # Impossible to anticipate all valid answers
```

### Module Planning Template

Use this template when planning a new module:

```
Module: [Topic Name]
Target Audience: [Beginner/Intermediate/Advanced]
Prerequisites: [Required knowledge]

Learning Objectives:
1. [Learner will be able to...]
2. [Learner will be able to...]
3. [Learner will be able to...]

Lesson Plan:
1. [Concept Intro] - Code lesson introducing the topic
2. [Basic Practice] - Code lesson with guided exercises
3. [Practice 2] - Code lesson with less scaffolding
4. [Challenge] - Code lesson with open-ended problem
5. [Review Quiz] - Quiz covering all concepts

Assessment Strategy:
- Code lessons test: [what skills]
- Quiz tests: [what knowledge]
```

### Example Module: Lists in Python

Here's how to structure a complete module:

```
lists_module/
├── module.yaml
├── 01_intro_to_lists.yaml       # Create and access lists
├── 02_list_operations.yaml      # append, remove, len
├── 03_list_iteration.yaml       # for loops with lists
├── 04_list_comprehensions.yaml  # Advanced (optional)
└── 05_lists_quiz.yaml           # Knowledge check
```

**module.yaml:**
```yaml
name: "Python Lists"
description: "Master Python lists: creation, manipulation, and iteration"
order: 3

lessons:
  - 01_intro_to_lists.yaml
  - 02_list_operations.yaml
  - 03_list_iteration.yaml
  - 04_list_comprehensions.yaml
  - 05_lists_quiz.yaml
```

**Quiz lesson (05_lists_quiz.yaml):**
```yaml
title: "Lists Quiz"
type: "quiz"
description: "Test your understanding of Python lists"
order: 4

instructions: |
  # Lists Knowledge Check

  Answer these questions to test what you've learned about Python lists.

questions:
  - id: "q1"
    type: "mcq"
    text: "How do you create an empty list?"
    multi_select: false
    options:
      - id: "a"
        text: "list = {}"
      - id: "b"
        text: "list = []"
      - id: "c"
        text: "list = ()"
      - id: "d"
        text: "list = ''"
    correct: ["b"]

  - id: "q2"
    type: "text"
    text: "What method adds an item to the end of a list?"
    correct: ["append", "append()", ".append", ".append()"]

  - id: "q3"
    type: "mcq"
    text: "Which operations are valid for lists? (Select all)"
    multi_select: true
    options:
      - id: "a"
        text: "Indexing with []"
      - id: "b"
        text: "Slicing with [:]"
      - id: "c"
        text: "Concatenation with +"
      - id: "d"
        text: "Division with /"
    correct: ["a", "b", "c"]

  - id: "q4"
    type: "text"
    text: "What is the index of the first element in a list?"
    correct: ["0", "zero"]

  - id: "q5"
    type: "mcq"
    text: "What does len([1, 2, 3]) return?"
    multi_select: false
    options:
      - id: "a"
        text: "2"
      - id: "b"
        text: "3"
      - id: "c"
        text: "[1, 2, 3]"
      - id: "d"
        text: "Error"
    correct: ["b"]
```

## Validation Checklist

Before deploying lessons, verify:

**For all lessons:**
- [ ] Module has `module.yaml` with name and description
- [ ] All lesson files are valid YAML
- [ ] Each lesson has title and instructions
- [ ] Instructions are clear and well-formatted
- [ ] Lessons are ordered correctly

**For code lessons:**
- [ ] Has at least one test case
- [ ] Test cases have description and expected_output
- [ ] Starter code runs without errors (even if incomplete)
- [ ] All referenced data files exist
- [ ] Edge cases are covered
- [ ] At least one hidden test case to prevent hardcoding

**For quiz lessons:**
- [ ] `type: "quiz"` is specified
- [ ] Each question has unique id
- [ ] MCQ questions have 3-4 options
- [ ] Correct answers are accurate
- [ ] Text questions have multiple acceptable answers where appropriate
- [ ] Multi-select questions clearly indicate multiple answers expected
