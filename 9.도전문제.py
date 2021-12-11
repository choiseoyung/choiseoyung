# 1번
# import random

# question = ["56 / 8", "8 * 9", "50 -25", "1 + 6", "81 / 9",
#             "22 + 10", "8 / 4", "9 * 7", "17 - 4", "3 + 5"]
# dailyQuestion = random.choice(question)
# print("#########################")
# print("# 오늘의 산수 문제 #")
# print("#########################")
# print("")
# print(dailyQuestion)

# 2번
# items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}

# while True:
#     print("")
#     print("# 재고 목록 #")
#     for key in sorted(items.keys()):
#         print(key, items[key])
        
#     print("\n********************")
#     print("0. 종료")
#     print("1. 재고 추가")
#     print("2. 재고 삭제")
#     print("********************\n")
#     a = int(input("무엇을 하시겠습니까?: "))
    
#     if a == 1:
#         item = input("물건의 이름을 입력하시오: ")
#         num = input("몇개를 추가하시겠습니까? :")
#         items[item] = int(items[item]) + int(num)
    
#     elif a == 2:
#         item = input("물건의 이름을 입력하시오: ")
#         num = input("몇개를 삭제하시겠습니까? :")
#         items[item] = int(items[item]) - int(num)
    
#     else:
#         break

# 3번
# english_dict = dict()

# english_dict['하나'] = 'one'
# english_dict['둘'] = 'two'
# english_dict['셋'] = 'three'

# word = input("단어를 입력하시오: ")
# print(english_dict[word])

# 4번
# import smtplib
# from email.mime.text import MIMEText

# me = 'abc@server.kr'     # 보내는 사람 메일 주소
# you = ['der1@server.com', 'def2@server.com', 'def3@server.com']   # 받는 사람 메일 주소
# contents = '12월 20일에 동창회가 있으니 참석해주시기 바랍니다.'

# msg = MIMEText(contents, _charset='euc-kr')
# msg['Subject'] = '동창회 모임'
# msg['From'] = me
# msg['To'] = you
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.ehlo()
# server.starttls()
# server.ehlo()

# server.login("자신의 아이디", "패스워드")

# for i in range(len(you)):
#     server.sendmail(me, you[i], msg.as_string())
# server.quit()