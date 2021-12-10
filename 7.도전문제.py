# 1번
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# def shape(length):   #length는 한 변의 길이
#     s = turtle.textinput("", "몇각형을 원하시나요?: ")
#     n = int(s)
#     for i in range(n):
#         t.forward(length)
#         t.left(360/n)
    
# t.up()            # 펜을 든다.
# t.goto(-200, 0)   # (-200, 0)으로 이동한다.
# t.down()          # 펜을 내린다.
# shape(100);       # square() 함수를 호출한다.

# t.up()
# t.goto(0, 0)
# t.down()
# shape(100);

# t.up()
# t.goto(200, 0)
# t.down()
# shape(100);

# 2번
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# def square(length,index):      # length는 한 변의 길이
#     t.color(colorList[index])
#     t.begin_fill()
#     for i in range(4):
#         t.forward(length)
#         t.left(90)
#     t.end_fill()
# colorList = ["red", "blue", "green"]
# x = -200

# for i in range(len(colorList)):
#     t.up()                     # 펜을 든다.
#     t.goto(x,0)                # (-200, 0)으로 이동한다.
#     t.down()                   # 펜을 내린다.
#     square(100, i);            # square() 함수를 호출한다.
#     x += 200

# 3번
# import turtle
# t = turtle.Turtle()

# n-각형을 그리는 함수를 정의한다.
# def n_polygon(n, length):
#     for i in range(n):
#         t.forward(length)
#         t.left(360/n)
        
# def get_color(index):
#     list = ["red", "orange", "yellow", "green", "blue", "navy", "purple", "gray", "skyblue", "pink"]
#     t.color(list[index])
#     t.begin_fill()
#     n_polygon(6, 100)
#     t.end_fill()
    
# for i in range(10):
#     t.left(20)
#     get_color(i)

# 4번
# import turtle                # 터틀 그래픽 모듈을 포함한다.
# t = turtle.Turtle()

# def circle(length):
#     t.circle(length)
#     t.left(60)
# def drawit(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.begin_fill()
#     t.color("green")
#     circle(50)
#     t.end_fill()
    
# s = turtle.Screen()          # 그림이 그려지는 화면을 얻는다.
# s.onscreenclick(drawit)     #  마우스 클릭 이벤트 처리 함수를 등록한다.

# 5번
# import turtle      # 터틀 그래픽 모듈을 포함한다.
# import random

# def tree(length):
#     angle = (random.randint(-20, 20))
#     if length > 5:                    # length가 5보다 크면 순환호출을 한다.
#         t.forward(length)             # 거북이가 length 만큼 선을 그린다.
#         t.right(20 + angle)           # 오른쪽으로 랜덤한 각도만큼 회전한다.
#         tree(length-15 * (random.random()+0.4))   # 랜덤한 값을 인수로 tree()를 호출한다.
#         t.left(40 + (angle * 2))                  # 왼쪽으로 랜덤한 각도 만큼 회전한다. 
#         tree(length-15 * (random.random()+0.4))   # 랜덤한 값을 인수로 tree()를 호출한다.
#         t.right(20 + angle)                       # 오른쪽으로 랜덤한 각도만큼 회전한다.
#         t.backward(length)                        # length만큼 뒤로 간다. 제자리로 돌아온다.

# t = turtle.Turtle()
# t.left(90)

# t.color("green")
# t.speed(1)
# tree(90)
    


