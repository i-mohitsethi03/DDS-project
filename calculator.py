import re

def precedence(op):
    """Determines the precedence of an operator."""
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    return 0

def apply_op(op, b, a):
    """Applies an operator to two operands."""
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    return 0

def tokenize(expression):
    """Splits the expression into a list of numbers, operators, and parentheses."""
    # This regex handles integers, decimals, and operators
    tokens = re.findall(r'[+\-*/()]|\d+\.\d+|\d+', expression)
    return tokens

def infix_to_postfix(expression):
    """Converts an infix expression to a postfix expression."""
    output = []
    operators = []
    
    tokens = tokenize(expression)
    
    for token in tokens:
        if token.isdigit() or (token.replace('.', '', 1).isdigit() and token.count('.') < 2):
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if operators and operators[-1] == '(':
                operators.pop()
        else:  # It's an operator
            while (operators and operators[-1] != '(' and 
                   precedence(operators[-1]) >= precedence(token)):
                output.append(operators.pop())
            operators.append(token)
            
    while operators:
        output.append(operators.pop())
        
    return output

def evaluate_postfix(postfix_expression):
    """Evaluates a postfix expression."""
    values = []
    for token in postfix_expression:
        if token.isdigit() or (token.replace('.', '', 1).isdigit() and token.count('.') < 2):
            values.append(float(token))
        else:
            op = token
            if len(values) < 2:
                raise ValueError("Invalid postfix expression.")
            operand2 = values.pop()
            operand1 = values.pop()
            values.append(apply_op(op, operand2, operand1))
            
    if len(values) != 1:
        raise ValueError("Invalid postfix expression.")
    
    return values[0]

def main():
    print("--- Expression Calculator ---")
    print("Enter a mathematical expression (e.g., 3 + 4 * (2 - 1)).")
    print("Enter 'exit' to quit.")
    
    while True:
        expression = input("Enter expression: ")
        if expression.lower() == 'exit':
            break
            
        try:
            postfix_exp = infix_to_postfix(expression)
            print(f"Postfix expression: {' '.join(postfix_exp)}")
            result = evaluate_postfix(postfix_exp)
            print(f"Result: {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
