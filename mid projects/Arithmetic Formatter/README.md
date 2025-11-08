# Arithmetic Arranger

## 📋 Project Overview

This Python program formats arithmetic problems vertically, similar to how they appear in elementary school worksheets. It takes addition and subtraction problems and displays them in a neat, aligned format with optional answers.

## 🎯 Purpose

This project demonstrates:

- String manipulation and formatting in Python
- Input validation and error handling
- List processing and alignment
- Creating user-friendly console applications
- Building educational tools for math practice

## 📊 Example Output

### Input
```
32 + 698
3801 - 2
45 + 43
```

### Output
```
   32      3801      45
+ 698    -    2    + 43
-----    ------    ----
  730      3799      88
```

## 🔧 How It Works

The program consists of two main functions:

### 1. `arithmetic_arranger(problems, show_answers=True)`

**Purpose**: Formats a list of arithmetic problems into vertical arrangement.

**Parameters**:
- `problems` (list): List of arithmetic expressions as strings (e.g., `["32 + 8", "1 - 3801"]`)
- `show_answers` (bool): Whether to display answers (default: True)

**Returns**: Formatted string with arranged problems, or error message if validation fails.

**Validation Rules**:
1. Maximum 5 problems at a time
2. Each problem must have exactly 3 parts: number, operator, number
3. Only `+` and `-` operators allowed
4. Numbers must contain only digits
5. Numbers cannot exceed 4 digits

**Formatting Logic**:
- Calculates width based on longest number + 2 spaces
- Right-aligns first number
- Formats operator with space and right-aligned second number
- Creates dashes equal to width
- Calculates and formats answer
- Joins all problems with 4 spaces between them

### 2. `main()`

**Purpose**: Provides interactive interface for entering arithmetic problems.

**Features**:
- Allows entering up to 5 expressions
- Input format: `32 + 698`
- Commands:
  - `0` - finish entering problems
  - `1` - skip to next expression
- Validates that at least one problem was entered
- Displays formatted results with answers

## 💡 Key Python Concepts Used

### String Methods
- **`.split()`** - Parses expression into components
- **`.strip()`** - Removes whitespace from input
- **`.isdigit()`** - Validates numeric input
- **`.rjust(width)`** - Right-aligns text within specified width
- **`.join()`** - Combines list elements with separator

### List Processing
- Four parallel lists track different output lines:
  - `first_line` - Top numbers
  - `second_line` - Operators and bottom numbers
  - `dash_line` - Separator dashes
  - `answer_line` - Calculated results

### Conditional Logic
- Multiple validation checks with early returns
- Operator-based calculation (addition vs subtraction)
- Optional answer display

## 🧪 Valid Input Examples

```
Valid expressions:
32 + 8
1 - 3801
9999 + 9999
45 + 43
123 - 49
```

## ❌ Error Cases

The program handles these error conditions:

### Too Many Problems
```python
# More than 5 problems
["1+1", "2+2", "3+3", "4+4", "5+5", "6+6"]
# Returns: "Error: Too many problems."
```

### Invalid Format
```python
# Missing operator or number
"32 8"
# Returns: "Error: Invalid problem format."
```

### Invalid Operator
```python
# Multiplication or division
"32 * 8"
# Returns: "Error: Operator must be '+' or '-'."
```

### Non-Numeric Input
```python
# Letters in numbers
"3a + 8"
# Returns: "Error: Numbers must only contain digits."
```

### Numbers Too Long
```python
# More than 4 digits
"12345 + 1"
# Returns: "Error: Numbers cannot be more than four digits."
```

## 🚀 Running the Program

### Interactive Mode
```
Arithmetic Formatter
Enter expressions like: 32 + 698
0 - finish, 1 - next
------------------------------
Expression 1: 32 + 698
0-finish, 1-next: 1
Expression 2: 3801 - 2
0-finish, 1-next: 1
Expression 3: 45 + 43
0-finish, 1-next: 0

========================================
   32      3801      45
+ 698    -    2    + 43
-----    ------    ----
  730      3799      88
```

## 📐 Alignment Algorithm

The program ensures proper alignment using:

1. **Width Calculation**:
   ```
   width = max(len(num1), len(num2)) + 2
   ```

2. **Right Justification**:
   - First number: padded to full width
   - Second number: padded to `width - 2` (accounting for operator + space)
   - Answer: padded to full width

3. **Spacing Between Problems**:
   - Each problem separated by 4 spaces (`"    "`)

## 🎓 Learning Outcomes

By studying this program, you'll understand:

- **String formatting** - Alignment and padding techniques
- **Input validation** - Multiple layers of error checking
- **List manipulation** - Building parallel data structures
- **User interaction** - Creating intuitive console interfaces
- **Mathematical operations** - String to integer conversion and calculation
- **Code organization** - Separating logic (arranger) from UI (main)

## 🔄 Program Flow

```
1. Start program
   ↓
2. Display instructions
   ↓
3. Loop (max 5 times):
   - Get expression input
   - Check for exit command (0)
   - Check for skip command (1)
   - Add valid expression to list
   - Ask for next action
   ↓
4. Validate at least one problem entered
   ↓
5. Call arithmetic_arranger()
   - Validate each problem
   - Format into lines
   - Calculate answers
   - Join all parts
   ↓
6. Display formatted result
```
