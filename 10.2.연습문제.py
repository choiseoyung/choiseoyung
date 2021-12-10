# 5. 데이터를 입력받을 때 사용할 수 있는 GUI 화면을 만들어봅시다.
# 이름, 직업, 국적을 입력할 수 있게한 다음. 보여주기를 통해서 화면에 출력할 수 있도록 합니다.
# 종료버튼을 클릭하면 종료되게 합니다.

# from tkinter import *
# fields = '이름', '직업', '국적'

# def fetch(entries):
#     for entry in entries:
#         field = entry[0]
#         text = entry[1].get()
#         print('%s: "%s"' % (field, text))
        
# def makeform(root, fields):
#     entries = []
#     for field in fields:
#         row = Frame(root)
#         lab = Label(row, width=15, text=field)
#         ent = Entry(row)
#         row.pack(side=TOP, fill=X)
#         lab.pack(side=LEFT)
#         ent.pack(side=RIGHT, expand=YES, fill=X)
#         entries.append((field, ent))
#     return entries

# root = Tk()
# ents = makeform(root, fields)
# root.bind('<Return>', (lambda event, e=ents: fetch(e)))
# b1 = Button(root, text='보여주기', command=(lambda e=ents: fetch(e)))
# b1.pack(side=LEFT, padx=5, pady=5)
# b2 = Button(root, text='종료하기', command=root.quit)
# b2.pack(side=LEFT, padx=5, pady=5)
# root.mainloop()

# 6. 로그인 GUI 화면을 만들어봅시다.

# from tkinter import *

# window = Tk()
# label1 = Label(window, text='로그인 하세요!!!', font=("Helvetica", 20))
# label1.pack()

# label2 = Label(window, text='아이디')
# label2.pack()

# entry1= Entry(window)
# entry1.pack()

# label2 = Label(window, text='패스워드')
# label2.pack()
# entry2 = Entry(window)
# entry2.pack()

# button1 = Button(window, text='로그인')
# button1.pack()
# window.mainloop()
# 로그인 화면 만든 것임. 실제 동작은 하지 않는다.

# 7. 가위 바위 보 게임을 GUI버전으로 만들어보겠습니다. 가위, 바위, 보의 이미지는 먼저 준비해야하며, 현재 코드파일의 위치에 있어야 한다.

# from random import *
# from tkinter import *

# # 선택하는 부분
# def user_choice_rock():
#     user_choice = "rock"
#     turn(user_choice)
#     user_image.configure(image=rock_image)

# def user_choice_paper():
#     user_choice = "paper"
#     turn(user_choice)
#     user_image.configure(image=paper_image)

# def user_choice_scissors():
#     user_choice = "scissors"
#     turn(user_choice)
#     user_image.configure(image=scissors_image)
    
# 게임
# def turn(user_choice):
#     oppo =['rock', 'paper', 'scissors']
#     oppo_choice=oppo[randint(0, 2)]
#     if(oppo_choice=='rock'):
#         oppo_image.configure(image=rock_image)
#         if(user_choice=='paper'):
#             turn_result.configure(text="사용자 승", fg="green")
#             compare.configure(text=">>>>>")
#         elif(user_choice=='scissors'):
#             turn_result.configure(text="컴퓨터 승!", fg="red")
#             compare.configure(text="<<<<<")
#         else:
#             turn_result.configure(text="무승부", fg="gray")
#             compare.configure(text="=====")
#     elif(oppo_choice=='paper'):
#         oppo_image.configure(image=paper_image)
#         if(user_choice=='scissors'):
#             turn_result.configure(text="사용자 승!", fg="green")
#             compare.configure(text=">>>>>")
#         elif(user_choice=='rock'):
#             turn_result.configure(text="컴퓨터 승!", fg="red")
#             compare.configure(text="<<<<<")
#         else:
#             turn_result.configure(text="무승부", fg="gray")
#             compare.configure(text="=====")
            
#     elif(oppo_choice=='scissors'):
#         oppo_image.configure(image=scissors_image)
#         if(user_choice=='rock'):
#             turn_result.configure(text="사용자가 이겼습니다.!", fg="green")
#             compare.configure(text=">>>>>")
#         elif(user_choice=='paper'):
#             turn_result.configure(text="에고 컴퓨터가 이겼군요.!", fg="gray")
#             compare.configure(text="<<<<<")
#         else:
#             turn_result.configure(text="무승부", fg="gray")
#             compare.configure(text="=====")
            
#메인 프로그램 부분

# main_window = Tk()
# rock_button = Button(main_window, width=20, text="바위", justify=CENTER, command=user_choice_rock, activebackground='black', activeforeground='white')

# paper_button = Button(main_window, width=20, text="보", justify=CENTER, command=user_choice_paper, activebackground='black', activeforeground='white')

# scissors_button = Button(main_window, width=20, text="가위", justify=CENTER, command=user_choice_scissors, activebackground='black', activeforeground='white')

# rock_image = PhotoImage(file="d:/rock.gif")  # 이 부분은 코딩이 끝난 뒤에 맞춰줄 예정
# paper_image = PhotoImage(file="d:/paper.gif")  # 이 부분은 코딩이 끝난 뒤에 맞춰줄 예정
# scissors_image = PhotoImage(file="d:/scissors.gif")  # 이 부분은 코딩이 끝난 뒤에 맞춰줄 예정

# user_image = Label(text="사용자", image=rock_image)
# user_image.image = rock_image

# compare = Label(main_window, justify=CENTER, font=("Helvetica", 20))
# oppo_image = Label(text="컴퓨터", image=paper_image)
# oppo_image.image = paper_image
# turn_result = Label(main_window, width=20, justify=CENTER, font=("Helvetica", 20))

# 그리드 생성
# rock_button.grid(row=5, column=1)
# paper_button.grid(row=5, column=2)
# scissors_button.gird(row=5, column=3)
# user_image.grid(row=3, column=1)
# compare.grid(row=3, coumn=2)
# oppo_image.grid(row=3, column=3)
# turn_result.grid(row=4, column=2)

# 메인 루프 처리(GUI화면을 띄운 상태로...)
# main_window.mainloop()
