# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("","몇각형을 원하시나요?: ")
# n = int(s)
# s = turtle.textinput("","한변의 크기를 입력해주세요: ")
# len = int(s)
# for i in range(n):
#     t.forward(len)
#     t.left(360/n)

# import turtle
# import random
# t = turtle.Turtle()
# t.shape("turtle")

# for i in range(30):
#     length = random.randint(1,100)
#     t.forward(length)
#     angle = random.randint(1,4)
#     t.right(90 * angle)

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", i*j)
#         j = j+1 
#     print(" ")
#     i = i+1

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# i = 0
# while i < 5:
#     t.forward(50)
#     t.right(144)

# import turtle
# import random

#색상은 리스트에 저장했다가 하나씩 꺼내서 변경하자.
# colors = ["red", "purple", "blue", "green", "yellow", "orange"]
# t = turtle.Turtle()

#배경색은 다음과 같은 문장으로 변경이 가능하다.
# turtle.bgcolor("black")

#거북이의 속도는 0으로 설정하면 최대가 된다.
# t.speed(0)

#거북이가 그리는 선의 두께는 width()를 호출하면 된다.
# t.width(3)

# length = 10   # 초기 선의 길이는 10으로 한다.

#while 반복문이다. 선의 길이가 500보다 작으면 반복한다.
# while length < 500:
#     t.forward(length)                # length만큼 전진한다.
#     t.pencolor(colors[length%6])     # 선의 색상을 변경한다.
#     angle = random.randint(1,100)    
#     t.right(angle)                   # 랜덤한 각도로 회전한다.
#     length +=5                       # 선의 길이를 5만큼 증가한다.

# import random

# tries = 0
# guess = 0
# answer = random.randint(1,100)

# print("1부터 100 사이의 숫자를 맞추시오: ")

# while guess != answer:
#     if tries < 10:
#         guess = int(input("숫자를 입력하시오: "))
#         tries = tries + 1
#         if guess <  answer:
#             print("낮음!")
#         elif guess > answer:
#             print("높음!")
#     else:
#         print("시도횟수를 초과하였습니다.")
#         break
    
# if guess == answer:
#     print("축하합니다. 시도횟수=", tries)
# else:
#     print("정답은 ",  answer)

# import random

# while True:
#     q = random.randint(0,1)
#     x = random.randint(1,100)
#     y = random.randint(1,100)
#     if(q == 1)&(x > y):
#         print(x, "-", y, "=", end=" ")
#         answer = int(input())
#         if answer == x - y:
#             print("잘했어요!!")
#         else:
#             print("다음번에는 잘할 수 있죠?")
            
#     else:
#         print(x, "+", y, "=", end=" ")
#         answer = int(input())
#         if answer == x + y:
#             print("잘했어요!!")
#         else:
#             print("다음번에도 잘할 수 있죠?")   

# import random
# number = random.randint(1,8)

# list = ["한 점의 의심도 없이 맞습니다.", "할 수 있습니다.", "물론입니다.", "글쎄요. 열심히 해야 할 것입니다.",
#         "안 될 것 같습니다.", "조금 더 노력하세요.", "행운을 빕니다.", "다음 달에 할 수 있을 겁니다."]
# while True:
#     name = input("이름:(종료하려면 엔터키) ")
#     if name =='':
#         break;
#     question = input("무엇에 대하여 알고 싶은가요? ")
#     print(name, "님", "/" ", question, "/"에 대하여 질문 주셨군요.")
#     print("운명의 주사위를 굴려볼게요...")
#     print(list[number-1])