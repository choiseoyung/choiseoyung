# import turtle    # 터틀 그래픽 모듈을 불러온다.
# import random    # 난수 모듈을 불러온다.

# screen = turtle.Screen()
# image1 ="D:/rabbit.gif"
# image2 ="D:/turtle.gif"
# image3 ="D:/turtle2.gif"
# screen.addshape(image1)
# screen.addshape(image2)
# screen.addshape(image3)

# t1 = turtle.Turtle()     # 첫 번재 거북이를 생성한다.
# t1.shape(image1)
# t1.pensize(5)            # 펜의 두께를 5로 한다.
# t1.penup()               # 펜을 든다.
# t1.goto(-300, 0)         # (-300, 0) 위치로 간다.

# t2 = turtle.Turtle()     # 두 번째 거북이를 생성한다.
# t2.shape(image2)
# t2.pensiaze(5)           # 펜의 두께를 5로 한다.
# t2.penup()               # 펜을 든다.
# t2.goto(-300, -100)      # (-300, -100) 위치로 간다.

# t3 = turtle.Turtle()     # 세 번째 거북이를 생성한다.
# t3.shape(image2)
# t3.pensize(5)            # 펜의 두께를 5로 한다.
# t3.penup()               # 펜을 든다.
# t3.goto(-300, -200)      # (-300, -200) 위치로 간다.

# t1.pendown()             # 첫 번째 거북이의 펜을 내린다.
# t2.pendown()             # 두 번째 거북이의 펜을 내린다.
# t3.pendown()             # 세 번째 거북이의 펜을 내린다.
# t1.speed(1)
# t2.speed(1)
# t3.speed(1)

# for i in range(100):             # 100번 반복한다.
#     d1 = random.randint(1, 60)   # 1부터 60사이의 난수를 발생한다.
#     t1.forward(1)                # 난수만큼 이동한다.
#     d2 = random.randint(1, 60)
#     t2.forward(2)
#     d3 = random.randint(1, 60)
#     t3.forward(d3)