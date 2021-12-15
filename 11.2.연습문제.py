# 4. 객체를 파일에 저장할 수 있다. pickle모듈을 사용해서 정수 12, 실수 3.14, 리스트 [1,2,3,4,5]를 이진 파일
# 'test.dat'에 저장하였다가 다시 읽는 프로그램을 작성하고 테스트하라.
# pickle의 dump()를 이용한다.

# import pickle

# outfile = open("text.dat", "wb")
# pickle.dump(12, outfile)
# pickle.dump(3.14, outfile)
# pickle.dump([1, 2, 3, 4, 5], outfile)
# outfile.close()

# infile = open("test.dat", "rb")
# print(pickle.load(infile))
# print(pickle.load(infile))
# print(pickle.load(infile))
# infile.close()

# 5. 텍스트파일 " data.txt"에 실수값들이 저장되어 있다고 가정하자. 한 줄에 하나의 실수만 저장되어 있다.
#    23.0
#    51.0
#    68.5
#    82.9
#    103.2
# 이 파일을 읽어서 합계와 평균을 계산한 후에 이것을 "output.txt"파일에 다음과 같이 저장하는 프로그램을 저장한다.
#    합계 = 328.6
#    평균 = 65.72
#    파일에서 한 줄에 한 줄씩 읽는 것이 편리하다.
#    문자열을 실수로 변환하려면 float()함수를 사용한다.

# inFileName = input("입력 파일 이름: ")
# outFileName = input("출력 파일 이름: ")

# infile = open(inFileName, "r")
# outfile = open(outFileName, "w")

# total = 0.0
# count = 0

# line = infile.readline()
# while line != "":
#     value = float(line)
#     total = total + value
#     line = infile.readline()
    
# avg = total / count
# outfile.write("평균=" + str(avg) + "\n")

# infile.close()
# outfile.close()


# 6. tkinter를 사용하여 제공한 연습문제파일의 6번의 화면과 같이 사용자 인터페이스를 만들고, "추가" 버튼을 누르면
#    사용자가 입력한 이름과 전화번로 리스트가 파일 "phone_book.data"에 저장된다. "파일 읽기"를 누르면 파일
#    "phone_book.data"에서 이름과 전화번호를 읽어오는 프로그램을 작성하라.
# 엔트리 위젯에서 데이트를 읽어오려면 e.get()을 사용, 엔트리 위젯에 문자열을 쓰려면 e.insert(0, string)을 사용
# 지우려면 e.delet(0, END)를 사용. 프로그램 내부에선는 딕셔너리를 사용하여 사용자의 이름과 전화번호를 저장한다.
# 너리를 리스트로 변환한 후에 첫 번째 항목을 꺼내야 한다.

# import pickle
# from tkinter import *

# phone_book = {}
# current = 0
# name = ""
# phone = ""

# window = Tk()

# frame1 = Frame(window)
# frame1.pack()
# Label(frame1, text="이름       ").grid(row= 1, column = 1, sticky = W)
# nameEntry = Entry(frame1, textvariable = name, width = 30)
# nameEntry.grid(row = 1, column = 2)

# frame2 = Frame(window)
# frame2.pack()
# Label(frame2, text = "전화번호").grid(row = 1, column = 1, sticky = W)
# phoneEntry = Entry(frame2, textvariable = phone, width = 30)
# phoneEntry.grid(row=1, column=2)

# frame3 = Frame(window)
# frame3.pack()

# def save():
#     outfile = open("phonebook.dat", "wb")
#     pickle.dump(phone_book, outfile)
#     print("주소들이 파일에 저장되어 있습니다.")
#     outfile.close()
    
# def load():
#     infile = open("phonebook.dat", "rb")
#     phone_book = pickle.load(infile)
#     infile.colse()
#     print("파일에서 주소를 읽었습니다.")
#     go_first()
    
# def add():
#     phone_book[nameEntry.get()] = phoneEntry.get()
#     print(phone_book)
#     save()
    
# def go_first():
#     global current
#     current = 0
#     ks = list(phone_book)
#     print(phone_book)
#     nameEntry.delete(0, END)
#     nameEntry.inset(0, ks[current])
#     phoneEntry.delete(0, END)
#     phoneEntry.insert(0, phone_book[ks[current]])
    
# def go_next():
#     global current
#     current += 1
#     ks = list(phone_book)
#     nameEntry.delete(0, END)
#     nameEntry.inser(0, ks[current])
#     phoneEntry.delete(0, END)
#     phoneEntry.insert(0, phone_book[ks[current]])
    
# def go_previous():
#     print("공사중_개발중이에요.")

# def go_last():
#     print("개발중입니다.")
    
# b1 = Button(frame3, text="추가", command=add).grid(row=1, column=1)
# b2 = Button(frame3, text="처음", command=go_first).grid(row=1, column=2)
# b3 = Button(frame3, text="다음", command=go_next).grid(row=1, column=3)
# b4 = Button(framd3, text="이전", command=go_previous).gird(row=1, column=4)
# b5 = Button(frame3, text="마지막", command=go_last).grid(row=1, column=5)
# b6 = Button(frame3, text ="파일 읽기", command=load).grid(row=1, column=6)

# window.mainloop()
     