# age = 20
# if age < 20:
#     print('20살 미만')
# else:
#     print('20살 이상')
# 20살 미만

# age = 30
# if age >= 30 and age <= 50:
#     print('30살 이상이고 50살 이하')

# temp = int(input("현재 온도를 입력하시오: "))
# if temp >= 25:
#     print("반바지를 입으세요")
# else:
#     print("긴바지를 입으세요")

# score = int(input("성적을 입력하시오: "))
# if score >= 90:
#     print("A학점입니다.")
# elif score >= 80:
#     print("B학점입니다.")
# elif score >= 70:
#     print("C학점입니다.")
# elif score >= 60:
#     print("D학점입니다.")
# else :
#     print("F학점입니다.")

# import random
# x = random.randint(1, 100)
# y = random.randint(1, 100)
# ans = int(input(str(x) + "-" + str(y) + "="))
# if ans == x-y :
#     print("맞았습니다.")
# else :
#     print("틀렸습니다.")

# n = int(input("정수를 입력하시오: "))
# if n%2==0 and n%3==0:
#     print("2와 3으로 나누어 떨어집니다.")
# else :
#     print("2와 3으로 나누어 떨어지지 않습니다.")

# import random
# solution = random.randint(0, 90)
# user = int(input("복권번호를 입력하시오(0에서 99사이): "))
# digit1 = solution // 10
# digit2 = solution % 10
# u_digit1 = user // 10
# u_digit2 = user % 10
# print("당첨번호는", solution, "입니다.")
# if (digit1 == u_digit1 and digit2 == u_digit2):
#     print("상금은 100만원입니다.")
# elif (digit1 == u_digit1
#         or digit1 == u_digit2
#         or digit2 == u_digit1
#         or digit2 == u_digit2):
#     print("상금은 50만원입니다.")
# else :
#     print("상금은 없습니다.")

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# x1 = int(input("큰 원의 중심좌표 x1: "))
# y1 = int(input("큰 원의 중심좌표 y1: "))
# r1 = int(input("큰 원의 반지름: "))
# x2 = int(input("작은 원의 중심좌표 x2: "))
# y2 = int(input("작은 원의 중심좌표 y2: "))
# r2 = int(input("작은 원의 반지름:"))

# t.penup()
# t.goto(x1, y1)
# t.pendown()
# t.circle(r1)

# t.penup()
# t.goto(x2, y2)
# t.pendown()
# t.circle(r2)

# dist = ((x1 - x2) * (x1 - x2) + (y1 - y2)) ** 0.5
# if dist <= r1 - r2 :
#     turtle.write("두번째 원이 첫번째 원의 내부에 있습니다.")
# elif dist <= r1 + r2 :
#     turtle.write("두번째 원이 첫번째 원과 겹칩니다.")
# else :
#     turtle.write("두번째 원이 첫번째 원과 겹치지 않습니다.")
# t._scrren.exitonclick()    #화면을 마우스로 클릭해야 종료되게 하는 부분

