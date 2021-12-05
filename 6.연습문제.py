# 1. 2부터 100사이의 모든 짝수를 출력하는 반복 루프를 작성해보자.
# x%2한 결과가 0이면x는 짝수이다.
# for i in range (2, 101):
#     if i%2 == 0:
#         print(i, end = " ")

# 2. 복리이자율 7%로 1000만원을 저축했을 경우 2000만원이 되는데 몇 년이 걸리는지 계산하기 위해 아래의 코드를 작성하였다.
#    잘못된 점은 없는지 체크하라.

# year = 0
# balance = 1000

# while balance <= 2000:         #여기의 연산자가 틀렸다. <= 으로 고쳐야 함.
#     year = year + 1
#     interest = balance * 0.07
#     balance = balance + interest
# print(year, "년이 걸립니다.")

# 3. 다음 코드의 출력을 예상해보자. 각 단계에서 변수와 값을 예상해 보자.
# %는 나머지를 계산하는 연산자이다. //는 나눗셈에서 몫을 계산하는 것이다.

# n = 1234
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum = sum + digit
#     n = n // 10
# print(sum)

# 4. 사용자에게 곱셈 퀴즈를 내고 답을 사용자로부터 받는 프로그램에서 사용자가 올바른 답을 입력할 때까지 반복하게 수정하라.
# 어떤 조건이 만족될 때까지 반복하는 것은 while 루프를 사용하는 것이다.

# ans = 0
# while ans != 3*9:
#     ans = int(input("3 x 9는?"))
# print("맞았습니다.")

# 5. 사용자가 입력한 정수의 합을 계산하는 프로그램을 작성하라. 사용자가 0을 입력 하기 전까지 정수를 계속하여 읽도록 하자.
# 무한루프를 작성하고 사용자가 입력한 값이 0이면 break 문장을 실행하여 반복 루프를 종료한다. 무한루프는 while True: 이다.

# sum = 0
# while True:
#     x = int(input("정수를 입력하시오: "))
#     if x == 0:
#         break;
#     sum = sum + x
# print("합은", sum, "입니다.")

# 6. 난수 생성 함수를 사용하여 2개의 주사위를 던졌을 때 나오는 수를 제공하는 화면과 같이 출력하여 본다.
# 1부터 6사이의 난수를 발생하려면 r = random.randint(1, 6) 문장을 사용, 프로그램의 첫 부분이 import random 문장
# 잊지 마세요.

# from random import randint

# for i in range(3):
#     d1 = randint(1, 6)
#     d2 = randint(1, 6)
#     print("첫번째 주사위=", d1, "두번째 주사위=", d2)

# 7. 여러분들에게 제공된 연습문제를 확인하시기 바랍니다.
# 터틀 그래픽과 반복을 사용하여 눈 모양을 그려본다. 연습문제의 이미지를 확인하세요.

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.lt(90)

# for i in range(1,7) :
#     t.fd(100)
#     t.fd(-30)
#     t.lt(60)
#     t.fd(30)
#     t.fd(-30)

#     t.rt(120)
#     t.fd(30)
#     t.fd(-30)

#     t.lt(60)
#     t.fd(-70)
#     t.lt(60)
#     t._streen.exitonclick()
# 하나의 패턴을 그리는 코드는 아래와 같다.
# t.fd(100); t.fd(-30); t.fd(30), t.lt(60); t.fd(30); t.fd(-30) 참고하시면 됩니다.
# 파이썬에서 문장의 끝에 ; 표시를 하면 한 줄에 여러개의 문장을 입력할 수 있다.

# 8. 터틀그래픽을 별을 그려보았을 것이다. 아래의 코드를 응용하여 10개의 별을 그리는 프로그램을 코딩하라.
#    별들을 시작 각도가 약간씩 다르다.
# 별을 그리는 코드를 반복하나. 하나의 별을 그리는 반복이 끝나면 lefr*10을 실행한다.



# import turtle

# myPen = turtle.Turtle()
# myPen.speed(0)
# myPen.color("#ff0000")

# for j in range(1, 10):
#     for i in range(1,6):
#         myPen.left(144)
#         myPen.forward(200)
#     myPen.left(10)

# myPen._screen.exitonclick()

# 9. 반복과 난수를 함께 사용하면 화면에 랜덤한 원을 그릴 수 있다. 화면에 10개의 랜덤한 원을 그리는 프로그램을 작성하라.
#    원의 중심과 반지름이 모두 난수이어야 한다.
# 참고: 1부터 100사이의 난수를 발생하려면 r = random.randint(1,100)을 사용하면 되지요! 첫부분에 randdom도 import해야 하고요.
#       원의 중심, 원의 반지름을 모두 난수로 설정합니다.

import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for j in range(1, 10):
    t.up()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    r = random.randint(10, 200)
    t.goto(x, y)
    t.down()
    t.circle(r)
t._screen.exitonclick()
