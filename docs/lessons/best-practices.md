# Best Practices

## Module Structure

A well-structured module follows a logical progression:

```
module/
├── module.yaml
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

## When to Use Each Lesson Type

| Lesson Type | Best For | Example Topics |
|-------------|----------|----------------|
| **Code** | Hands-on practice, syntax, algorithms | Functions, loops, debugging |
| **Quiz** | Concept review, terminology, theory | Data types, keywords, best practices |

### Use Code Lessons When

- Learners need to practice writing code
- The skill requires hands-on repetition
- Testing problem-solving ability
- Output can be objectively verified

### Use Quiz Lessons When

- Testing recall of terminology
- Reviewing theory before practice
- Quick knowledge checks between sections
- Testing "why" not just "how"

## Designing Code Exercises

### Clear Learning Objectives

Before writing a lesson, ask:

- What specific skill should learners gain?
- What's the minimum code needed to demonstrate this skill?
- What mistakes are learners likely to make?

### Progression of Difficulty

=== "Level 1 - Guided"

    Provide most of the code, learner fills in one piece:

    ```yaml
    starter_code: |
      name = "Alice"
      # Print a greeting using the name variable
      print(_____)
    ```

=== "Level 2 - Scaffolded"

    Provide structure, learner writes the logic:

    ```yaml
    starter_code: |
      # Get a number from user

      # Calculate and print its square

    ```

=== "Level 3 - Open"

    Minimal guidance, learner designs solution:

    ```yaml
    starter_code: |
      # Your code here

    ```

### Effective Test Cases

**Cover the spectrum:**

```yaml
test_cases:
  # Basic case - what most learners try first
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

**Avoid these mistakes:**

- :x: Testing only the "happy path"
- :x: Using inputs guessable from description
- :x: Forgetting edge cases (0, empty string, negative)
- :x: Making all tests visible (encourages hardcoding)

## Designing Quiz Questions

### MCQ Best Practices

**Good question characteristics:**

- Tests understanding, not just memorization
- One clearly correct answer (single-select)
- Distractors are plausible but clearly wrong

**Example of a good MCQ:**

```yaml
- id: "q1"
  type: "mcq"
  text: "What will print(type(3.14)) output?"
  options:
    - id: "a"
      text: "<class 'int'>"      # Common misconception
    - id: "b"
      text: "<class 'float'>"    # Correct
    - id: "c"
      text: "<class 'str'>"      # Confusion with quotes
    - id: "d"
      text: "<class 'number'>"   # Doesn't exist
  correct: ["b"]
```

**Why it's good:**

- Tests understanding of data types
- Each distractor represents a common misconception
- Clear, unambiguous wording

### Text Question Guidelines

Text questions work best for:

- Short, definitive answers (keywords, symbols, numbers)
- Answers with limited correct variations

```yaml
# Good - short answer
- id: "q1"
  type: "text"
  text: "What keyword defines a function?"
  correct: ["def"]

# Good - multiple acceptable answers
- id: "q2"
  type: "text"
  text: "What symbol is used for comments?"
  correct: ["#", "hash", "hashtag", "pound"]

# Bad - too open-ended
- id: "q3"
  type: "text"
  text: "Explain what a variable is"
  correct: ["..."]  # Can't validate free-form text
```

## Module Planning Template

Use this template when planning:

```
Module: [Topic Name]
Target Audience: [Beginner/Intermediate/Advanced]
Prerequisites: [Required knowledge]

Learning Objectives:
1. Learner will be able to...
2. Learner will be able to...
3. Learner will be able to...

Lesson Plan:
1. [Intro] - Code lesson introducing the topic
2. [Practice] - Code lesson with guided exercises
3. [Practice 2] - Code lesson with less scaffolding
4. [Challenge] - Code lesson with open-ended problem
5. [Quiz] - Quiz covering all concepts

Assessment Strategy:
- Code lessons test: [what skills]
- Quiz tests: [what knowledge]
```

## Validation Checklist

### All Lessons

- [ ] Valid YAML syntax
- [ ] Has title and instructions
- [ ] Instructions are clear and well-formatted
- [ ] Ordered correctly in module

### Code Lessons

- [ ] At least one test case
- [ ] Test cases have description and expected_output
- [ ] Starter code runs without errors
- [ ] Edge cases covered
- [ ] At least one hidden test case

### Quiz Lessons

- [ ] `type: "quiz"` is specified
- [ ] Each question has unique id
- [ ] MCQ questions have 3-4 options
- [ ] Correct answers are accurate
- [ ] Text questions have multiple acceptable answers
- [ ] Multi-select indicates multiple answers expected
