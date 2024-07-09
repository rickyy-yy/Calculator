from tkinter import *

main_body = Tk()  # The main window that contains buttons and input field


def add_1():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "1"
    else:
        input_display["text"] = text_rn + "1"


def add_2():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "2"
    else:
        input_display["text"] = text_rn + "2"


def add_3():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "3"
    else:
        input_display["text"] = text_rn + "3"


def add_4():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "4"
    else:
        input_display["text"] = text_rn + "4"


def add_5():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "5"
    else:
        input_display["text"] = text_rn + "5"


def add_6():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "6"
    else:
        input_display["text"] = text_rn + "6"


def add_7():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "7"
    else:
        input_display["text"] = text_rn + "7"


def add_8():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "8"
    else:
        input_display["text"] = text_rn + "8"


def add_9():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "9"
    else:
        input_display["text"] = text_rn + "9"


def add_0():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "0"
    else:
        input_display["text"] = text_rn + "0"


def add_plus():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "+"
    else:
        input_display["text"] = text_rn + "+"


def add_minus():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "-"
    else:
        input_display["text"] = text_rn + "-"


def add_multiply():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "x"
    else:
        input_display["text"] = text_rn + "x"


def add_divide():
    text_rn = input_display["text"]
    if text_rn in ["Enter number", "Invalid. Try again"]:
        input_display["text"] = "÷"
    else:
        input_display["text"] = text_rn + "÷"


def parse_input():
    valid = True
    expression = input_display["text"]
    if len(expression) == 0:
        pass
    else:
        previous_character = expression[0]
        if previous_character in ['+', '-', 'x', '÷']:
            input_display["text"] = "Invalid. Try again"
        else:
            index = 1
            while index < len(expression):
                if expression[index] == "0":
                    if previous_character == '÷':
                        input_display["text"] = "Invalid. Try again"
                        valid = False
                if expression[index] in ['+', '-', 'x', '÷']:
                    if previous_character in ['+', '-', 'x', '÷']:
                        input_display["text"] = "Invalid. Try again"
                        valid = False
                previous_character = expression[index]
                if index == len(expression) - 1:
                    if expression[index] in ['+', '-', 'x', '÷']:
                        input_display["text"] = "Invalid. Try again"
                        valid = False
                index += 1

            if valid:
                calculate(expression)


def calculate(expression):
    processed = []
    temp = ""
    for i in expression:
        if i in ['÷', 'x', '-', '+']:
            processed.append(temp)
            temp = ""
            processed.append(i)
        else:
            temp += i
    processed.append(temp)
    if len(processed) == 1:
        result = processed[0]
        input_display["text"] = str(result)
    elif len(processed) == 0:
        pass
    else:
        while '+' in processed or '-' in processed or 'x' in processed or '÷' in processed:
            if 'x' in processed or '÷' in processed:
                for i in processed:
                    if i in ['x', '÷']:
                        operator_index = processed.index(i)
                        operand_index_1 = operator_index - 1
                        operand_index_2 = operator_index + 1

                        operand_2 = int(processed.pop(operand_index_2))
                        operand_1 = int(processed.pop(operand_index_1))
                        if i == 'x':
                            result = operand_1 * operand_2
                        else:
                            result = int(operand_1 / operand_2)
                        processed[operator_index-1] = str(result)
            else:
                for i in processed:
                    if i in ['+', '-']:
                        operator_index = processed.index(i)
                        operand_index_1 = operator_index - 1
                        operand_index_2 = operator_index + 1

                        operand_2 = int(processed.pop(operand_index_2))
                        operand_1 = int(processed.pop(operand_index_1))
                        if i == '+':
                            result = operand_1 + operand_2
                        else:
                            result = operand_1 - operand_2
                        processed[operator_index-1] = str(result)



        input_display["text"] = str(result)


def del_last_char():
    expression = input_display["text"]
    expression = expression[:-1]
    input_display["text"] = expression


current_expression = "Enter number"
input_display = Label(main_body, text=current_expression, height=5, width=45, bg='#E1EDED')
input_display.grid(columnspan=4, row=0)

button_1 = Button(main_body, text="1", width=10, height=5, command=add_1, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_2 = Button(main_body, text="2", width=10, height=5, command=add_2, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_3 = Button(main_body, text="3", width=10, height=5, command=add_3, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_4 = Button(main_body, text="4", width=10, height=5, command=add_4, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_5 = Button(main_body, text="5", width=10, height=5, command=add_5, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_6 = Button(main_body, text="6", width=10, height=5, command=add_6, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_7 = Button(main_body, text="7", width=10, height=5, command=add_7, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_8 = Button(main_body, text="8", width=10, height=5, command=add_8, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_9 = Button(main_body, text="9", width=10, height=5, command=add_9, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_0 = Button(main_body, text="0", width=10, height=5, command=add_0, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_plus = Button(main_body, text="+", width=10, height=5, command=add_plus, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_minus = Button(main_body, text="-", width=10, height=5, command=add_minus, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_multiply = Button(main_body, text="x", width=10, height=5, command=add_multiply, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_divide = Button(main_body, text="÷", width=10, height=5, command=add_divide, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_equal = Button(main_body, text="=", width=10, height=5, command=parse_input, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")
button_backspace = Button(main_body, text="Del", width=10, height=5, command=del_last_char, borderwidth=0, bg="#e8e8e8", activebackground="#d6d6d6")

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_plus.grid(row=4, column=1)
button_minus.grid(row=4, column=2)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=3, column=3)
button_equal.grid(row=2, column=3)
button_backspace.grid(row=1, column=3)

main_body.configure(bg="#e8e8e8")
main_body.title("Calculator App")
main_body.resizable(width=False, height=False)
main_body.mainloop()
