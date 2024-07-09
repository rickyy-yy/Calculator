from tkinter import *

main_body = Tk()  # The main window that contains buttons and input field


def add_1():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "1"
    else:
        input_display["text"] = text_rn + "1"


def add_2():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "2"
    else:
        input_display["text"] = text_rn + "2"


def add_3():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "3"
    else:
        input_display["text"] = text_rn + "3"


def add_4():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "4"
    else:
        input_display["text"] = text_rn + "4"


def add_5():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "5"
    else:
        input_display["text"] = text_rn + "5"


def add_6():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "6"
    else:
        input_display["text"] = text_rn + "6"


def add_7():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "7"
    else:
        input_display["text"] = text_rn + "7"


def add_8():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "8"
    else:
        input_display["text"] = text_rn + "8"


def add_9():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "9"
    else:
        input_display["text"] = text_rn + "9"


def add_0():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "0"
    else:
        input_display["text"] = text_rn + "0"


def add_plus():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "+"
    else:
        input_display["text"] = text_rn + "+"


def add_minus():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "-"
    else:
        input_display["text"] = text_rn + "-"


def add_multiply():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "x"
    else:
        input_display["text"] = text_rn + "x"


def add_divide():
    text_rn = input_display["text"]
    if text_rn == "Enter number":
        input_display["text"] = "÷"
    else:
        input_display["text"] = text_rn + "÷"

current_expression = "Enter number"
input_display = Label(main_body, text=current_expression, height=5, width=45, bg='#e1eded')
input_display.grid(columnspan=4, row=0)

button_1 = Button(main_body, text="1", width=10, height=5, command=add_1)
button_2 = Button(main_body, text="2", width=10, height=5, command=add_2)
button_3 = Button(main_body, text="3", width=10, height=5, command=add_3)
button_4 = Button(main_body, text="4", width=10, height=5, command=add_4)
button_5 = Button(main_body, text="5", width=10, height=5, command=add_5)
button_6 = Button(main_body, text="6", width=10, height=5, command=add_6)
button_7 = Button(main_body, text="7", width=10, height=5, command=add_7)
button_8 = Button(main_body, text="8", width=10, height=5, command=add_8)
button_9 = Button(main_body, text="9", width=10, height=5, command=add_9)
button_0 = Button(main_body, text="0", width=10, height=5, command=add_0)
button_plus = Button(main_body, text="+", width=10, height=5, command=add_plus)
button_minus = Button(main_body, text="-", width=10, height=5, command=add_minus)
button_multiply = Button(main_body, text="x", width=10, height=5, command=add_multiply)
button_divide = Button(main_body, text="÷", width=10, height=5, command=add_divide)
button_equal = Button(main_body, text="=", width=10, height=5)
button_backspace = Button(main_body, text="Del", width=10, height=5)

button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_plus.grid(row=4,column=1)
button_minus.grid(row=4,column=2)
button_multiply.grid(row=4,column=3)
button_divide.grid(row=3,column=3)
button_equal.grid(row=2,column=3)
button_backspace.grid(row=1,column=3)


main_body.mainloop()
