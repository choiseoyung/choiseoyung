# 1. 사용자로부터 5개의 숫자를 얽어서 리스트에 저장하고 숫자들의 평균을 계산하여 출력하는 프로그램을 작성하라.
#    리스트를 생성하고, 사용자에게서 받은 정수 append()로 리스트에 추가한다. 리스트의 크기는 len(alist)을 사용.
#    len()은 내장 함수로 사용

# alist = []
# sum = 0

# for i in range(5):
#     i = int(input("정수를 입력하시오: "))
#     alist.append(i)
    
# for i in alist:
#     sum += i
# avg = sum / len(alist)
# print("평균=", avg)

# 2. 주사위를 던져서 나오는 값들의 빈도를 계산하는 프로그램을 작성하라.
#    즉 1, 2, 3, 4, 5, 6의 값이 각각 몇 번이나 나오는지를 계산한다. 난수 발생 함수와 리스트를 사용해보자.
# 주사위 값이 나오는 빈도를 다음 같은 리스트에 저장해보자.
#  counters = [0, 0, 0, 0, 0, 0]
# 주사위를 던져서 값이 나오면 해당되는 리스트의 요소를 증가시킨다.
#  value = random.randint(0, 5)
#  counters[value] = counters[value] + 1

# import random
# counters = [0, 0, 0, 0, 0, 0]

# for i in range(1000):
#     value = random.randint(0, 5)
#     counters[value] = counters[value] + 1
    
# for i in range(6):
#     print("주사위가", i + 1, "인 경우는", counters[i], "번")

# 3. 딕셔너리를 사용하여서 친구들의 이름과 전화번호를 저장해보자. 사용자로부터 친구들의 이름과 전화번호를 입력하고 딕셔너리에 저장한다.
#    이름을 입력하지 않고 엔터키를 치면 검색모드가 되고, 검색 모드에서는 친구들의 이름으로 전화번호를 검색할 수 있도록 한다.
#    공백 딕셔너리를 생성하고 사용자가 입력하는 대로 딕셔너리에 추가되게 한다.

# contacts = {  }

# while True:
#     name = input("(입력모드)이름을 입력하시오: ")
#     if not name:
#         break;
#     tel = input("전화번호를 입력하시오: ")
#     contacts[name] = tel
    
# while True:
#     name = input("(검색모드)이름을 입력하시오: ")
#     if not name:
#         break;
#     if name in contacts :
#         print(name, "의 전화번호는", contacts[name], "입니다.")

# 4. 색상을 리스트에 저장한다. 리스트에 저장된 색상을 하나씩 꺼내어 거북이의 색상으로 설정하면서 속이 채워진 사각형을 그리는 프로그램을 작성하라.
# draw_square(x, y, c)를 작성하고 for c in ["yello", "red", "purple", "blue"]: t.draw_square(x, y, c)를 호출한다.

# import turtle
# import random

# t = turtle.Turtle()
# t.shape("turtle")

# def draw_square(x, y, c):
#     t.up()
#     t.goto(x, y)
#     t.down()
#     t.color("black", c)
#     t.begin_fill()
#     t.fd(100)
#     t.left(90)
#     t.forward(100)
#     t.left(90)
#     t.forward(100)
#     t.left(90)
#     t.forward(100)
#     t.left(90)
#     t.end_fill()
# for c in ["yellow", "red", "purple", "blue"]:
#     x = random.randint(-100, 100)
#     y = random.randint(-100, 100)
#     draw_square(x, y, c)
    
# t._screen.exitonclick()

# 5. 색상을 리스트에 저장한다.
# 리스트에 저장된 색상을 하나씩 꺼내어 거북이의 색상으로 설정하면서 속이 채워진 다각형을 그리는 프로그램을 작성하여 보자.
# 화면의 (x, y) 위치에 다각형을 그리는 함수 def_shape(t, c, length, sides, x, y)을 작성한다.
# 색상을 리스트에 저장하고 하나씩 꺼내서 거북의 색상으로 설정한다.
# 난수를 발생하여 랜덤한 위치에 랜덤한 크기의 다각형을 그려보자.

# import turtle
# import random

# t = turtle.Turtle()
# s = turtle.Screen()

# def draw_shape(t, c, length, sides, x, y):
#     t.up()
#     t.goto(x, y)
#     t.down()
#     t.fillcolor(c)
#     angle = 360.0 / sides
#     t.begin_fill()
#     for dist in range(sides):
#         t.forward(length)
#         t.left(angle)
#     t.end_fill()
    
# for i in range(10):
#     color = random.choice(['while', 'yellow', 'blue', 'skyblue', 'orange', 'green'])
#     side_length = random.randint(10, 100)
#     sides = random.randint(3, 10)
#     x = random.randint(-200, 200)
#     y = random.randint(-200, 200)
#     draw_shape(t, color, side_length, sides, x, y)  

# 6. 색상을 리스트에 저장한다. 리스트에 저장된 색상을 하나씩 꺼내어 거북이의 색상으로 설정하면서
#    속이 채워진 별을 랜덤한 위치에 그리는 프로그램을 작성해보자.
# 화면의 (x, y) 위치에 별을 그리는 함수 draw_star(color, length, x, y)을 작성한다.
# 색상을 리스트에 저장하고 하나씩 꺼내서 거북이의 색상으로 설정한다. 난수를 발생하여 랜덤한 위치에 랜덤한 크기의 별을 그려보자.
# 화면의 배경색을 검정으로 하려면 s = turtle.screen(); s.bgcolor("black");을 실행한다.

# import turtle
# import random

# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")

# def draw_star(aturtle, color, side_length, x, y):
#     aturtle.color(color)
#     aturtle.begin_fill()
#     aturtle.penup()
#     aturtle.goto(x, y)
#     aturtle.pendown()
#     for i in range(5):
#         aturtle.forward(side_length)
#         aturtle.right(144)
#         aturtle.forward(side_length)
#     aturtle.end_fill()
    
# for i in range(20):
#     color = random.choice(['white', 'yellow', 'blue', 'skyblue', 'orange', 'green'])
#     side_length = random.randint(10, 100)
#     x = random.randint(-200, 200)
#     y = random.randint(-200, 200)
#     draw_star(t, color, side_length, x, y)

# 7. 인터넷 도메인의 약자와 해당되는 국가를 딕셔너리에 저장해보자. 예를 들어 "kr"은 대한민국으로 저장되어야 한다.
#    딕셔너리를 순화하면서 모든 키와 값을 출력하는 프로그램을 작성해보자.
# 딕셔너리에서 키와 값을 모두 꺼내서 출력하려면 다음과 같은 문장을 사용한다.
# domains = {"kr": "대한민국", ... }
# for k, v in domains.items():
#      print(k, ":", v)

# domains = {"kr": "대한민국", "us": "미국", "jp": "jp", "de": "독일", "sk": "스로바키아", "hu": "헝가리", "no": "노르웨이"}

# for k, v in domains.items():
#     print(k, ":", v)

# 8. 딕셔너리에 문제와 정답을 저장하고 하나씩 꺼내서 사용자에게 제시하는 프로그램을 작성해보자.
#    사용자는 문자열로 답해야 한다. 번호로 답할 수는 없다.
# problems = {'파이썬':'최근에 가장 떠오르는 프로그래밍 언어', '변수':'데이터를 저장하는 메모리 공간', '함수':'작업을 수행하는 문장들의 집합에 이름을 붙인것',
# '리스트':'서로 관련이 없는 항목들의 모임'}
# for word in problems.keys():
# ...

# problems = {'파이썬': '최근에 가장 떠오르는 프로그래밍 언어',
#             '변수': '데이터를 저장하는 메모리 공간',
#             '함수': '작업을 수행하는 문장들의 집합에 이름을 붙인 것',
#             '리스트': '서로 관련이 없는 항목들의 모임',
#             }

# def show_words(problems):
#     display_message = ""
#     i=1
#     for word in problems.keys():
#         display_message += "("+str(i)+")"
#         display_message += word + " "
#         i+=1
#     print(display_message)

# for meaning in problems.values():
#     print("다음은 어떤 단어에 대한 설명일까요? ")
#     print("\""+meaning+"\"")
#     correct = False
#     while not correct:
#         show_words(problems)
#         guessed_word = input("")
#         if problems[guessed_word] == meaning:
#             print("정답입니다. !")
#             correct = True
#         else:
#             print("정답이 아닙니다.")