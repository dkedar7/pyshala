# Quiz Lessons

Quiz lessons test knowledge with multiple choice questions (MCQ) and text-based questions.

## Basic Structure

```yaml
title: "Python Basics Quiz"
type: "quiz"
description: "Test your understanding"
order: 5

instructions: |
  # Python Basics Quiz

  Answer the following questions.

questions:
  - id: "q1"
    type: "mcq"
    text: "What function displays output?"
    options:
      - id: "a"
        text: "echo()"
      - id: "b"
        text: "print()"
    correct: ["b"]
```

## Question Types

### Single-Select MCQ

Radio buttons where learners select **one** answer:

```yaml
- id: "q1"
  type: "mcq"
  text: "What is the correct way to create a variable?"
  multi_select: false  # or omit (default)
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

### Multi-Select MCQ

Checkboxes where learners select **multiple** answers:

```yaml
- id: "q2"
  type: "mcq"
  text: "Which are valid Python data types? (Select all)"
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
  correct: ["a", "c", "d"]
```

!!! note "Multi-Select Indicator"
    Always indicate in the question text that multiple answers are expected (e.g., "Select all that apply").

### Text Input

Free-form text with case-insensitive matching:

```yaml
- id: "q3"
  type: "text"
  text: "What symbol starts a comment in Python?"
  correct: ["#", "hash", "pound"]
```

## Question Fields

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Unique identifier (e.g., "q1") |
| `type` | Yes | `"mcq"` or `"text"` |
| `text` | Yes | The question text |
| `options` | MCQ only | List of answer options |
| `multi_select` | MCQ only | Allow multiple answers (default: false) |
| `correct` | Yes | List of correct answer(s) |

### Option Fields

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Unique identifier (e.g., "a", "b") |
| `text` | Yes | Option text displayed to learner |

## Answer Validation

- **MCQ**: Exact match of selected option IDs
- **Multi-select**: All correct options must be selected (order doesn't matter)
- **Text**: Case-insensitive match against any answer in `correct` list
- **Whitespace**: Leading/trailing whitespace is trimmed

## Complete Example

```yaml title="05_control_flow_quiz.yaml"
title: "Control Flow Quiz"
type: "quiz"
description: "Test your knowledge of if statements and loops"
order: 10

instructions: |
  # Control Flow Quiz

  This quiz covers conditional statements and loops.

  **Tips:**
  - Read each question carefully
  - For multi-select, choose ALL correct answers
  - Text answers are not case-sensitive

questions:
  - id: "q1"
    type: "mcq"
    text: "Which keyword starts a conditional statement?"
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

## Tips

### Writing Good Questions

- **One concept per question** - Don't test multiple things
- **Clear wording** - Avoid tricky or ambiguous phrasing
- **Plausible distractors** - Wrong answers should be common mistakes

### MCQ Best Practices

```yaml
# Good MCQ - tests understanding
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

# Bad MCQ - subjective/unclear
- id: "q1"
  type: "mcq"
  text: "Which is best?"
  options:
    - id: "a"
      text: "A"
    - id: "b"
      text: "B is correct because it's better"
  correct: ["b"]
```

### Text Question Best Practices

```yaml
# Good - short, definitive answer
- id: "q1"
  type: "text"
  text: "What keyword defines a function?"
  correct: ["def"]

# Good - multiple acceptable answers
- id: "q2"
  type: "text"
  text: "What is the boolean value for true?"
  correct: ["True", "true", "TRUE"]

# Bad - too open-ended
- id: "q3"
  type: "text"
  text: "Explain what a variable is"
  correct: ["..."]  # Impossible to validate
```

### Multi-Select Guidelines

- Have 2-3 correct answers (not just 1, not all)
- Test related concepts together
- Clearly indicate multiple selection is expected
