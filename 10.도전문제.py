# 1번
# from tkinter import *

# def process():
#     temperature = float(e1.get())
#     mytemp = (temperature-32)*5/9
#     e2.insert(0, str(mytemp))
    
# def process2():
#     temperature = float(e2.get())
#     mytemp = (temperature*(9/5))+32
#     e1.insert(0, str(mytemp))
    
# window = Tk()
# l1 = Label(window, text = "화씨")
# l2 = Label(window, text = "섭씨")
# l1.grid(row = 0, column = 0)
# l2.grid(row = 1, column = 0)

# e1 = Entry(window)
# e2 = Entry(window)
# e1.grid(row = 0, column = 1)
# e2.grid(row = 1, column = 1)

# b1 = Button(window, text = "화씨 -> 섭씨", command=process)
# b2 = Button(window, text = "섭씨 -> 화씨", command=process2)
# b1.grid(row = 2, column = 0)
# b2.grid(row = 2, column = 1)

# window.mainloop()

# 2번
# from tkinter import *

# window = Tk()

# w = Button(window, text = "버튼1", bg="red", fg="white")
# w.place(x=0, y=0)
# w = Button(window, text = "버튼2", bg="orange", fg="white")
# w.place(x=20, y=20)
# w = Button(window, text = "버튼3", bg="yellow", fg="white")
# w.place(x=40, y=40)
# w = Button(window, text = "버튼4", bg="green", fg ="white")
# w.place(x=60, y=60)
# w = Button(window, text = "버튼5", bg="blue", fg="white")
# w.place(x=80, y=80)
# window.mainloop()

# 3번
# from tkinter import *

# def paint(event):
#     global lastx, lasty
#     x,y = (event.x),(event.y)
#     canvas.create_line(lastx,lasty,x,y,fill = "black")
#     lastx,lasty = x,y
    
# def activate_paint(event):
#     global lastx, lasty
#     lastx, lasty = (event.x),(event.y)
    
# def release(event):
#     global lastx, lasty
    
#     if(lastx, lasty) == (event.x,event.y):
#         canvas.create_line(lastx,lasty,lastx+1,lasty+1)
        
# lastx,lasty = None, None

# window = Tk()
# canvas = Canvas(window)
# canvas.pack()
# canvas.bind('<B1-Motion>',paint)
# canvas.bind('<ButtonPress-1>', activate_paint)   #B1-Press
# canvas.bind('<ButtonRelease-1>', release)         #B1-Release
# window.mainloop()

# 4번
# from tkinter import *

# mycolor = "blue"

# def paint(event):
#     x1,y1 = (event.x-1), (event.y+1)
#     x2,y2 = (event.x-1), (event.y+1)
#     canvas.create_oval(x1, y1, x2, y2, fill = mycolor)
    
# def change_color_red():
#     global mycolor
#     mycolor = "red"
    
# def change_color_green():
#     global mycolor
#     mycolor = "green"

# def change_color_yellow():
#     global mycolor
#     mycolor = "yellow"
    
# window = Tk()
# canvas = Canvas(window)
# canvas.pack()
# canvas.bind("<B1-Motion>", paint)
# button = Button(window, text="빨간색", command=change_color_red)
# button.pack()
# button = Button(window, text="녹 색", command=change_color_green)
# button.pack()
# button = Button(window, text="노란색", command=change_color_yellow)
# button.pack()
# window.mainloop()
