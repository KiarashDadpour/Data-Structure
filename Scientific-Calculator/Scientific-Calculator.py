import math


class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.S = [0] * max_size  # create a vector with zeros
        self.num = 0

    def push(self, item):
        if self.num >= self.max_size:
            raise Exception("OverFlow")  # if the stack is full return massage and exit program
        self.S[self.num] = item
        self.num += 1

    def pop(self):
        if self.num <= 0:
            raise Exception("Empty")  # if the stack is empty return massage and exit program
        item = self.S[self.num - 1]
        self.num -= 1
        return item

    def is_empty(self):
        if self.num == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.num >= self.max_size:
            return True
        else:
            return False

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.S[self.num - 1]

    def display(self):
        if self.is_empty():
            return "Stack is empty"
        while not self.is_empty():
            print(self.pop())


def computing(a, operand, b):
    if operand == "+":
        return a + b
    elif operand == "-":
        return b - a
    elif operand == "*":
        return a * b
    elif operand == "/":
        if a == "0":
            print("ZeroDivisionError!!!")
            return None
        return b / a
    elif operand == "^":
        return b ** a


def to_radian(deg):
    radian = (deg / 180) * math.pi
    return radian


def advanced_computing(sign, num):
    if sign == "sin":
        rad = to_radian(num)
        return math.sin(rad)
    elif sign == "cos":
        rad = to_radian(num)
        return math.cos(rad)
    elif sign == "tan":
        rad = to_radian(num)
        return math.tan(rad)
    elif sign == "cot":
        rad = to_radian(num)
        return 1 / math.cos(rad)
    elif sign == "sqrt":
        return math.sqrt(num)
    elif sign == "log2":
        return math.log2(num)
    elif sign == "log10":
        return math.log10(num)


def main():
    numbers_stack = Stack(20)
    operator_stack = Stack(20)
    operator_list = ["+", "-", "*", "/", "^"]
    advance_operator_list = ["sin", "cos", "tan", "cot", "sqrt", "log2", "log10"]
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0, ')': 0}
    expression_list = str(input("Please enter calculation: ")).split()
    for char in range(0, len(expression_list)):
        if expression_list[char] is not None:

            if expression_list[char] == "(":
                operator_stack.push(expression_list[char])


            elif expression_list[char] == ")":
                while operator_stack.top() != "(":
                    operand1 = numbers_stack.pop()
                    operand2 = numbers_stack.pop()
                    operator = operator_stack.pop()
                    res = computing(float(operand1), operator, float(operand2))
                    numbers_stack.push(res)

                if operator_stack.top() == "(":
                    operator_stack.pop()


            elif expression_list[char] not in operator_list and expression_list[char] not in advance_operator_list:
                numbers_stack.push(expression_list[char])

            elif expression_list[char] in operator_list:
                if operator_stack.top() == 'Stack is empty':
                    operator_stack.push(expression_list[char])

                elif operator_stack.top() and priority[expression_list[char]] > priority[operator_stack.top()]:
                    operator_stack.push(expression_list[char])

                else:
                    operand1 = numbers_stack.pop()
                    operand2 = numbers_stack.pop()
                    operator = operator_stack.pop()
                    res = computing(float(operand1), operator, float(operand2))
                    numbers_stack.push(res)
                    operator_stack.push(expression_list[char])

            elif expression_list[char] in advance_operator_list:
                res = advanced_computing(expression_list[char], float(expression_list[char + 1]))
                numbers_stack.push(res)
                expression_list[char + 1] = None

    while not operator_stack.is_empty():
        operand1 = numbers_stack.pop()
        operand2 = numbers_stack.pop()
        operator = operator_stack.pop()
        res = computing(float(operand1), operator, float(operand2))
        numbers_stack.push(res)

    print(numbers_stack.top())


main()


# example : cos 120 * ( 2 + 3 ) / sqrt 36 ==> -0.4166666666666665
# example : log2 8 * sin 30 / cos 60 ==> 2.999999999999999
# example : exp 5 + ( sin 60 * cos 75 ) sqrt 7 ==> 2.869895179106604
