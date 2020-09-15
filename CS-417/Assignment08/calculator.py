from stack import *
from typing import List, Dict, Tuple, Any
import string

def tokenize(line: str,
             specials: str,
             whitespace: str) -> List[str]:
    '''
    Given an expression, breaks it up into tokens
    line:        a string
    specials:    single-character tokens (usually '+-*/=()')
    whitespace : characters that should be ignored (usually ' \t')

    Returns: a list of tokens
    '''

    IDLE       = 0
    OPERAND    = IDLE    + 1
    WHITESPACE = OPERAND + 1
    state = IDLE
    tokens = []
    for c in line:
        if state == IDLE:
            if c in whitespace:
                state = WHITESPACE
                continue
            elif c in specials:
                state = IDLE
                tokens.append(c)
            else:
                state = OPERAND
                operand = c
        elif state == OPERAND:
            if c in whitespace:
                state = WHITESPACE
                tokens.append(operand)
            elif c in specials:
                state = IDLE
                tokens.append(operand)
                tokens.append(c)
            else:
                state = OPERAND
                operand += c

        elif state == WHITESPACE:
            if c in whitespace:
                pass
            elif c in specials:
                state = IDLE
                tokens.append(c)
            else:
                state = OPERAND
                operand = c
    if state == OPERAND:
        tokens.append(operand)    

    return tokens

def precedence(operator: str) -> int:
    '''
    Precedence of operators.
    * / : highest
    + - : middle
    = () : lowest

    Returns a number (the precedence)
    '''
    if operator in "*/":
        return 2
    elif operator in "-+":
        return 1
    else:
        return 0

def lexer(tokens: List[str]) -> List[Tuple[str, Any]]:
    '''
    Given a list of tokens, perform lexical analysis, and classify them.

    Return a list of tuples.  Each tuple has two values (lexical_type, token)
    The lexical_type is 'number', 'variable', 'operator', or 'unknown'
    '''
    lexemes = []
    operators = "+-*/=()"
    for token in tokens:
        lex_type = 'unknown'
        lex_value = token
        if token in operators:
            lex_type = 'operator'
        else:
            try:
                x = float(token)
                lex_type = 'number'
            except ValueError:
                if (token[0] in string.ascii_letters or "_" and token[0] != " ") and (token[1:] in string.ascii_letters or string.digits or "_"):
                    lex_type = "variable"
                else:
                    lex_type = "unknown"
        lexemes.append( (lex_value, lex_type) )
    return lexemes

def to_postfix(infix_expression: str) -> List[str]:
    '''
    Convert an infix expression into a postfix expression (one string)
    Return a list of lexemes (each one is tuple (lexical_tupe, token))

    Proceed thus:
    - call tokenize to convert the infix_expression into a list of tokens
    - call lexer to classify the tokens into a list of lexemes
    - use a stack-based algorithm to convert the infix list
      into a postfix list of strings, and return that.
    '''
    s = Stack()
    postfix = []
    tokens = tokenize(infix_expression, "+-*/=()", " \t")
    infix_expression = lexer(tokens)
    for token, lex_type in infix_expression:
        if lex_type == "number":
            postfix.append(token)
        elif token == "(":
            s.push(token)
        elif token == ")":
            while ((s.empty() != True) and s.top() != '('):
                postfix.append(s.pop())
                print("Stack",s ,"\t postfix 2",postfix)
            if ((s.empty() != True) and s.top() != '('):
                pass
            else:
                if s.empty() == True:
                    break
                s.pop()
        else:
            while (s.empty() != True) and precedence(s.top()) >= precedence(token):
                postfix.append(s.pop())
                print("Stack",s ,"\t postfix 1",postfix)
            if lex_type == 'operator':
                s.push(token)
            else:
                postfix.append(token)
        print("Stack",s ,"\t postfix",postfix)
    while (s.empty() != True):
        postfix.append(s.pop())
    return postfix
    """
        if token == '(':
            s.push(token)
        elif lex_type == "operand":
            postfix.append(token)
        elif token == ')':
            while (s.empty() != True) and s.top() != '(':
                postfix.append(s.pop())
            s.pop(")")
        else:
            while (s.empty() != True) and precedence(s.top()) >= precedence(token):
                postfix.append(s.pop())
        print("Stack",s ,"\t postfix",postfix)
        s.push(token)
    """


def eval_postfix(postfix_expression: List[str],
                 symbol_table: Dict[str,float]) -> float:
    '''
    Evaluate a postfix expression.
    Inputs: the postfix expression (a list of strings)
            the symbol table (maps str names to floats)
    Output: a float (the expressions's value)

    Proceed as follows:
    - call lexer to classify the postfix expresion into a list of lexemes
    - use a stack-based algorithm to evaluate the expression.
    - when done, return the top of the stack.
    '''
    s = Stack()
    postfix_expression = lexer(postfix_expression)
    print(postfix_expression)
    for token, lex_type in postfix_expression:
        if lex_type == "operator":
            right_operand = s.pop()
            left_operand = s.pop()
            if token == "=":
                symbol_table[left_operand] = right_operand
                s.push(symbol_table[left_operand])
            if type(left_operand) != float:
                left_operand = symbol_table[left_operand]
            if type(right_operand) != float:
                right_operand = symbol_table[right_operand]
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
            try:
                s.push(float(token))
            except ValueError:
                if str(token) in symbol_table:
                    s.push(float(symbol_table[str(token)]))
                else:
                    s.push(token)
            
    if len(s) > 1:
        return "Too Many Operands"
    result = s.pop()
    return result

def main():
    symbol_table: Dict[str,float] = dict()
    while True:
        try:
            expression = input('>>> ')
        except EOFError:
            print()
            break

        if expression[0] == '#':
            # Comment line.  Print it, and ignore it.
            print(expression)
            continue

        postfix: List[Tuple[str,Any]] = to_postfix(expression)
        value: float = eval_postfix(postfix, symbol_table)
        print (value)

if __name__ == '__main__':
    main()

#RS
