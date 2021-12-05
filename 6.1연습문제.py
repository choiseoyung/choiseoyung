# 10. 문서로 제공한 연습문제 10번의 그림을 보고 프로그램을 작성합니다.
#     거북이를 왕복 달리게 하는 것입니다.

#     거북이가 현재 바라보고 있는 방향을 잘 설정해야 합니다. 잘못설정하면 뒤로 달리게 됩니다.

# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# for i in range(5):
#     t.fd(200);
#     t.rt(90)
#     t.fd(20);
#     t.rt(90)
#     t.fd(200)
#     t.lt(90)
#     t.fd(20);
#     t.left(90)
# t._screen.exitonlclcik()

# 11. 터틀 그래픽 프로그램을 분석해봅시다. 학습하지 않은 함수가 있다면 웹 서핑을 해서 정리해봅시다.

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.color('red', 'yellow')
# t.begin_fill()
# while True:
#     t.fd(200)
#     t.lt(170)
#     if abs(t.pos()) < 1:
#         break
# t.end_fill()
# t._screen.exitonclick()
# color(c1, c2)함수는 도형의 선색상과 채우기색상을 c1과 c2로 설정. begin_fill()를 호출하면 속이 채워진 도형이 그려진다.
# pos()함수는 거북이의 좌표를 반환한다. abs()는 절대값을 계산한다. break는 반복 루프를 빠져나오도록 하게 한다.

# 12. 터틀 그래픽과 반복을 사용하여 싸인(sine)그래프를 그려보자. 거북이를 싸인값에 따라서 움지게 한다.
#     싸인 값은 sin()함수로 계산한다. 프로그램의 첫 부분이 import math를 추가한다. 각도를 라디안으로 변환하여야 한다.
#     radian = 3.14 * degree /180.0 수식을 사용한다.

# import turtle
# import math

# t = turtle.Turtle()
# t.shape("turtle")
# t.color('red', 'yellow')

# for x in range(0, 360):
#     t.goto(x, 200 * math.sin(x*3.14/180))
# t._screen.exitonclick()


