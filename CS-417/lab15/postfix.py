import console # Need this for testing, please don't remove this line

# Task 1: import the Stack class from the stack module
from stack import Stack
def is_operator(token):
    # Task 2: Identify operators
    if token in "+-*/=":
        return True
    else:
        return False

def eval_postfix(expression):
    s = Stack()
    for token in expression:
        if is_operator(token):

            # Task 3: handle an operator (and Task 7 is here too):
            # - pop into right_operand
            # - pop into left_operand
            # - add, subtract, multiply, or divide those two values, into result
            # - push result

            # REPLACE THIS LINE
            if s.empty():
                return "Too many Operator"
            right_operand = s.pop()
            if s.empty():
                return "Too many Operator"
            left_operand = s.pop()
            if token == "+":
                result = right_operand + left_operand
                s.push(result)
            elif token == "-":
                result = right_operand - left_operand
                s.push(result)
            elif token == "*":
                result = right_operand * left_operand
                s.push(result)
            elif token == "/":
                result = right_operand / left_operand
                s.push(result)
        else:

            # Task 4: handle an operand: (and Task 6 is here too)
            # - convert it into a float
            # - push it
            value = float(token)
            s.push(value)
            

    # Task 5: get the expression's value (and Task 8 is here too).
    # After all tokens have been processed, the expresion's value
    # will be at the top of the stack.
    # - pop into result
    # - return result

    if len(s) > 1:
        return "Too Many Operands"
    result = s.pop()
    return result

def main():
    for line in console.console('> '):
        tokens = line.rstrip('\n\r').split()
        result = eval_postfix(tokens)
        print (result)

if __name__ == '__main__':
    main()

