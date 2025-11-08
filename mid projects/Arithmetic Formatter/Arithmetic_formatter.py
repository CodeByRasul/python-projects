def arithmetic_arranger(problems, show_answers=True):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dash_line = []
    answer_line = []
    
    for problem in problems:
        parts = problem.split()
        
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        num1, operator, num2 = parts
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        max_length = max(len(num1), len(num2))
        width = max_length + 2
        
        first_line.append(num1.rjust(width))
        second_line.append(operator + ' ' + num2.rjust(max_length))
        dash_line.append('-' * width)
        
        if operator == '+':
            answer = str(int(num1) + int(num2))
        else:
            answer = str(int(num1) - int(num2))
        answer_line.append(answer.rjust(width))
    
    arranged_problems = "    ".join(first_line) + "\n"
    arranged_problems += "    ".join(second_line) + "\n"
    arranged_problems += "    ".join(dash_line)
    arranged_problems += "\n" + "    ".join(answer_line)
    
    return arranged_problems

def main():
    problems = []
    
    print("Arithmetic Formatter")
    print("Enter expressions like: 32 + 698")
    print("0 - finish, 1 - next")
    print("-" * 30)
    
    for i in range(5):
        problem = input(f"Expression {i+1}: ").strip()
        
        if problem == '0':
            break
        elif problem == '1':
            continue
        else:
            problems.append(problem)
        
        if i < 4:
            cmd = input("0-finish, 1-next: ").strip()
            if cmd == '0':
                break
    
    if not problems:
        print("No expressions entered!")
        return
    
    print("\n" + "=" * 40)
    result = arithmetic_arranger(problems, True)
    print(result)

if __name__ == "__main__":
    main()