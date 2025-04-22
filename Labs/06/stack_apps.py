from stack import Stack


def check_delimiters(expr: str, delims: dict[str,str]) -> bool:
    stack = Stack()
    opening_delims = delims.keys()
    closing_delims = delims.values()
    same_char_delims = set(x for x in opening_delims if x == delims[x])

    for char in expr:
        if char in opening_delims:
            if char in same_char_delims and char in stack:
                stack.pop()
            else:
                stack.push(char)
        elif char in closing_delims:
            if stack.empty() or delims[stack.peek()] != char:
                return False
            stack.pop()

    return stack.empty()


def infix_to_postfix(expr: str) -> str:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    postfix = []
    stack = Stack()

    tokens = expr.split()

    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        elif token == '(' or stack.empty() or stack.peek() == '(':
            stack.push(token)
        elif token == ')':
            while not stack.empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            if not stack.empty() and stack.peek() == '(':
                stack.pop()
        elif token in precedence:
            while not stack.empty() and precedence.get(token, 0) <= precedence.get(stack.peek(), 0):
                postfix.append(stack.pop())
            stack.push(token)

    while not stack.empty():
        postfix.append(stack.pop())

    return ' '.join(postfix)
