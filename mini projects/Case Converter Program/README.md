# Case Converter: Camel/Pascal to Snake Case

## 📋 Project Overview

This project implements a Python program that converts strings from **Camel Case** or **Pascal Case** formatting into **Snake Case** formatting. The program includes input validation and uses elegant Python features like list comprehensions for efficient string transformation.

## 📚 Case Formats Explained

### Camel Case
- **Format**: First word lowercase, subsequent words capitalized, no spaces
- **Example**: `myVariableName`, `userName`, `getData`
- **Common in**: JavaScript, Java (for variables and methods)

### Pascal Case
- **Format**: All words capitalized, no spaces
- **Example**: `MyClassName`, `UserProfile`, `GetData`
- **Common in**: C#, Java (for class names), React components

### Snake Case
- **Format**: All lowercase, words separated by underscores
- **Example**: `my_variable_name`, `user_name`, `get_data`
- **Common in**: Python, Ruby, SQL (for variables and functions)

## 💡 Example Conversions

```
Input                   →  Output
─────────────────────────────────────────────
myVariableName          →  my_variable_name
userName                →  user_name
getData                 →  get_data

MyClassName             →  my_class_name
UserProfile             →  user_profile
GetUserData             →  get_user_data
HTMLParser              →  htmlparser
XMLHttpRequest          →  xmlhttp_request
```

## 🎓 Key Python Concepts Used

### List Comprehension
- Concise way to create lists from iterables
- Uses conditional expressions for character-by-character transformation
- More readable than traditional loops
- Pythonic approach to string transformation

### String Methods
- **`.isupper()`** - Checks if character is uppercase
- **`.lower()`** - Converts character to lowercase
- **`.strip('_')`** - Removes leading/trailing underscores
- **`.isalpha()`** - Validates alphabetic characters
- **`.join()`** - Combines list elements into string

### Input Validation Pattern
The program uses a continuous loop that prompts for input until valid data is received, with clear error messages for invalid entries.

## 🧪 Testing the Program

### Valid Inputs
```
Input: myVariable
Output: my_variable

Input: MyClass
Output: my_class

Input: getHTMLContent
Output: get_htmlcontent

Input: UserProfileData
Output: user_profile_data
```

### Invalid Inputs (will show error)
```
Input: my_variable (contains underscore)
Input: user123Name (contains numbers)
Input: getData! (contains special characters)
Input: [empty string]
Input: "hello world" (contains spaces)
```
