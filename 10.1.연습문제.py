# 1. 하나의 레이블과 2개의 버튼을 가지는 GUI프로그램을 작성하라.
#     레이블 : 간단한 GUI프로그램
#     버튼   : (1) 환영합니다. (2) 종료

# from tkinter import Tk, Label, Button

# def greet():
#     print("파이썬에 오신 것을 환영합니다.")
    
# window = Tk()
# label = Label(window, text="간단한 GUI프로그램! ")
# label.pack()

# greet_button = Button(window, text="환영합니다.", command=greet)
# greet_button.pack()

# close_button = Button(window, text="종료", command=window.quit)
# close_button.pack()

# window.mainloop()

# 2. 숫자를 입력하고 "더하기" 버튼을 누르면 합계에 더해지고 "빼기"버튼을 누르면 합계에서 빼지는 계산기를 GUI로 작성하라.
# 사용자가 입력하면 값을 entry.get()으로 읽어서 정수로 변환한 후에 변수 total에 합친다. 이 값을 레이블에 표시하면 된다.

# from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

# def update_add():
#     update("add")

# def update_subtract():
#     update("subtract")

# def update_reset():
#     update("reset")

# window = Tk()
# total = 0
# sum = Label(window)
# sum.grid(row=0, column=1, columnspan=2)

# label = Label(window, text="현재 합계: ")
# label.grid(row=0, column=0)

# entry = Entry(window)
# entry.grid(row=1, column=0, columnspan=3)

# add_button = Button(window, text="더하기(+)", command=update_add)
# subtract_button = Button(window, text="빼기(-)", command=update_subtract)
# reset_button = Button(window, text="초기화", command=update_reset)

# add_button.grid(row=2, column=0)
# subtract_button.grid(row=2, column=1)
# reset_button.grid(row=2, column=2)

# def update(method):
#     global total
#     if method == "add":
#         total += int(entry.get())
#     elif method == "subtract":
#         total -= int(entry.get())
#     else:
#         total = 0
#     sum['text'] = str(total)
#     entry.delete(0, END)
# window.mainloop()

# 3. 숫자 맞추기 게임을 GUI 방식으로 프로그래밍 하자.

# import random
# from tkinter import *

# window = Tk()
# secret_number = random.randint(1, 100)
# guess = None
# num_guesses = 0

# def guess_number():
#     global num_guesses
#     guess = int(entry.get())
#     num_guesses += 1
#     if guess == secret_number:
#         message = "축하합니다.!"
#     elif guess < secret_number:
#         message = "너무 낮아요!!"
#     else:
#         message = "너무 높아요!!"
#     labe['text'] = message
    
# def reset():
#     global num_guesses
#     entry.delete(0, END)
#     secret_number = random.randint(1, 100)
#     guess = 0
#     message = "1부터 100사이의 숫자를 추측하시오"
#     labe['text'] = message
    
# message = "1부터 100사이의 숫자를 추측하시오"
# labe = Label(window, text=message)
# entry = Entry(window)

# guess_button = Button(window, text="숫자를 입력", command=guess_number)
# reset_button = Button(window, text="게임을 다시 실행", command=reset)

# labe.grid(row=0, column=0, columnspan=2, sticky=W+E)
# entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
# guess_button.grid(row=2, column=0)
# reset_button.grid(row=2, column=1)

# window.mainloop()

# 4. 인치를 센티미터로 변환하는 프로그램을 작성해보자.

# from tkinter import *

# def do_convert():
#     inch_val = float(cvt_from.get())
#     centimeters_val = inch_val * 2.54
#     cvt_to.set('%s 센티미터' % centimeters_val)
    
# root = Tk()
# cvt_from = StringVar()
# cvt_to = StringVar()

# lbl = Label(root, text="인치를 센티미터로 변환하는 프로그램")
# lbl.grid(row=0, column=0, columnspan=2)
# from_lbl = Label(root, text='인치를 입력하시오: ')
# from_lbl.grid(row=1, column=0)
# from_entry = Entry(root, textvariable=cvt_from)
# from_entry.grid(row=1, column=1)

# to_lbl = Label(root, text='변환결과: ')
# to_lbl.grid(row=2, column=0)
# result_lbl = Label(root, textvariable=cvt_to)
# result_lbl.grid(row=2, column=1)

# convert_btn = Button(root, text='변환!', command=do_convert)
# convert_btn.grid(row=3, column=1)

# root.mainloop()