def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    while True:
            our_case = input("Enter the string in camelCase or PascalCase: ")
            
            if our_case.strip() and our_case.replace(" ", "").isalpha():
                break
            print("Error! Please enter a non-empty string with no number or symbols like '_'. Please enter the string only in camelCase or PascalCase)")
    
    print(convert_to_snake_case(our_case))
    
main()
