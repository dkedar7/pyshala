# Writing Lessons

PyShala supports two types of lessons:

| Type | Description | Use Case |
|------|-------------|----------|
| **Code** | Interactive coding exercises with a code editor | Teaching programming through practice |
| **Quiz** | Multiple choice and text-based questions | Testing knowledge, assessments |

## Lesson Structure

All lessons are YAML files with these common fields:

```yaml
title: "Lesson Title"           # Required
type: "code"                    # "code" (default) or "quiz"
description: "Short summary"    # Optional
order: 0                        # Sort order (default: 0)

instructions: |                 # Required - Markdown content
  # Lesson Content

  Explanation goes here...
```

## Code vs Quiz

### Code Lessons

Best for:

- Hands-on practice
- Learning syntax
- Problem-solving skills
- Algorithm implementation

```yaml
type: "code"  # or omit (default)
starter_code: |
  # Write your code here

test_cases:
  - description: "Test case 1"
    stdin: "input"
    expected_output: "output"
```

### Quiz Lessons

Best for:

- Concept review
- Terminology recall
- Quick assessments
- Theory understanding

```yaml
type: "quiz"

questions:
  - id: "q1"
    type: "mcq"
    text: "Question?"
    options:
      - id: "a"
        text: "Option A"
    correct: ["a"]
```

## Markdown in Instructions

Instructions support full Markdown:

```yaml
instructions: |
  # Main Heading

  Regular paragraph text.

  ## Code Examples

  ```python
  print("Hello, World!")
  ```

  ## Lists

  - Item 1
  - Item 2

  ## Tables

  | Column 1 | Column 2 |
  |----------|----------|
  | Cell 1   | Cell 2   |

  ## Emphasis

  **Bold** and *italic* text.
```

## External Instructions

For longer content, use a separate file:

```yaml
title: "Complex Lesson"
instructions_file: "complex_lesson.md"  # Relative path
starter_code: |
  # Your code here

test_cases:
  - description: "Test"
    expected_output: "result"
```

## Next Steps

- [Code Lessons](code-lessons.md) - Full code lesson reference
- [Quiz Lessons](quiz-lessons.md) - Full quiz lesson reference
- [Best Practices](best-practices.md) - Tips for effective lessons
