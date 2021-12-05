# 1. 눈사람을 그리는 함수를 작성하고 이 함수를 여러번 호출하여 랜덤한 위치에 눈사람을 그리는 프로그램을 작성하라.
#    draw_snowman(x, y) 함수를 작성하고 테스트. 터틀 그래픽에서 배경을 하늘색으로 변경하려면 s = turtle.Screen();
#    s.bgcolor('skyblue'); 로 처리한다.


# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("black", "white")
# s = turtle.Screen(); s.bgcolor('skyblue');

# def draw_snowman(x, y):
#     t.up()
#     t.goto(x,y)
#     t.down()
#     t.begin_fill()
#     t.circle(20)
#     t.end_fill()
#     t.goto(x, y-25)
#     t.setheading(135)
#     t.forward(50)
#     t.backward(50)
    
#     t.setheading(30)
#     t.forward(50)
#     t.backward(50)
#     t.setheading(0)
    
#     t.begin_fill()
#     t.circle(15)
#     t.end_fill()
#     t.goto(x, y-70)
#     t.begin_fill()
#     t.circle(30)
#     t.end_fill()
    
# draw_snowman(0,0)
# draw_snowman(100,0)
# draw_snowman(200,0)
# t._screen.exitonclick()

# 2. 6각형을 그리는 draw_hexa()함수를 작성하고 이 함수를 호출하여 제공한 연습문제 문서의 그림, 벌집 모양을
#    화면에 그려보는 프로그램을 작성하라.

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)

# def hexagon():
#     for i in range(6):
#         turtle.forward(100)
#         turtle.left(360/6)
        
# for i in range (6):
#     hexagon()
#     turtle.forward(100)
#     turtle.right(60)
# t._screen.exitonclick()    

# 3. 함수 f(x)=x²+1을 계산하는 함수를 작성하고 이 함수를 이요하여 화면에 f(x)를 그려보자.

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(9)

# def f(x):
#     return x**2 + 1

# t.goto(200,0)
# t.goto(0,0)
# t.goto(0,200)
# t.goto(0,0)

# for x in range(150):
#     t.goto(x, int(0.01*f(x)))

# t._screen.exitonclick()

# 함수를 f(x) 정의하고 x를 0에서 150까지 변경하면서 f(x)값을 계산하여 거북이를 움직이면 됩니다. x축과 y축도 함께 그린다.
# 함수의 값이 무척 커질 수 있으므로 함수의 값에 0.01을 곱해서 거북이를 움직여보도록 합니다.

# 4. 거북이를 움직이지 않고 선을 긋는 함수 draw_line()정의하고 이것을 이용 거미줄과 같은 모양을 그려봅니다.
# 거북이는 항상 중에 위치 시킵니다.
# 거북이를 약간씩 회전시키면서 draw_line()호출합니다.

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)

# def draw_line():
#     t.fd(100)
#     t.backward(100)
    
# for x in range(12):
#     t.right(30)
#     draw_line()
    
# t._screen.exitonclick()

# 5. 생일 축하 노래를 출력하는 함수 happyBirthday()를 작성하고 출력해봅니다.
# 매개변수를 통하여 이름을 받으면 됩니다.

# def happyBirthday(person):
#     print("Happy birthday to you!")
#     print("Happy birthday to you!")
#     print("Happy birthday, dear " + person)
#     print("Hapyy birthday to you!")
    
# happyBirthday("최서영")

# 6. 사용자로부터 2개의 정수를 받아서 수학 문제를 만들어서 화면에 출력하는 함수를 작성하고 출력하라.
# 매개변수를 통하여 정수를 받으면 됩니다.

# def sumProblem(x,y):
#     sum = x + y
#     sentence = "정수" +str(x) + "+" +str(y) + "의 합은?"
#     print(sentence)
    
# def main():
#     a = int(input("첫 번째 정수: "))
#     b = int(input("두 번째 정수: "))
#     sumProblem(a, b)

# main()

# 7. 파이를 나타내는 PI=3.14를 전역 변수로 하여 원의 면적을 계산하는 함수 circleArea(radius)과 원의 둘레를 계산하는 
#    함수를 circleCircumference(radius)를 작성하고 확인하라.

# PI = 3.14159265358979

# def circleArea(radius):
#     return PI * radius * radius

# def circleCircumference(radius):
#     return 2 * PI * radius

# def main():
#     print("반지름이 5인 원의 면적:", circleArea(5))
#     print("반지름이 5인 원의 둘레: ", circleCircumference(5))

# main()

# 8. 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하는 함수를 각각 작성하고 출력하라.
# add(a,b)와 같은 함수를 만들어봅니다.

# def add(a,b):
#     print("(%d + %d)" % (a, b), end=" ")
#     return a + b
# def subtract(a, b):
#     print("(%d -%d)" % (a, b), end=" ")
#     return a - b

# def multiply(a, b):
#     print("(%d *%d)" % (a, b), end=" ")
#     return a * b

# def divide(a, b):
#     print("(%d / %d)" % (a, b), end=" ")
#     return a / b

# what = add(20, 10)
# print("= ", what)

# what = subtract(20, 10)
# print("= ", what)

# what = multiply(20, 10)
# print("= ", what)

# what = divide(20, 10)
# print("= ", what)
