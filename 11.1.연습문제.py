# 1. 사용자가 입력한 텍스트 파일을 열어서 파일 안의 글자가 몇 개있는지 계산하는 프로그램을 작성하라.
# 텍스트 파일이므로 open(filename, "r")과 같이 파일을 열고, 파일 안의 각 줄은 아래의 코딩을 보면서 한다.

# filename = input("파일 이름을 입력하시오: ").strip()     # 파일명 입력하는 부분
# infile = open(filename, "r")                            # 텍스트 파일을 여는 부분이며, 읽기까지 진행된다.
# count = 0                                               # count는 0 으로 초기화 한다.

# for line in infile:                                     # infile 즉, 파일에서 문자를 카운트 하는 부분
#     for ch in infile: 
#         count += 1
        
# print("파일 안에는 총", count, "개의 글자가 있습니다.") 
# infile.close()

# 2. 사용자로부터 파일 이름과 문자열을 입력받은후, 파일을 열어서 사용자가 원하는 문자열을 삭제한 후에 다시 파일에 쓴다.
#    문자열을 파일에 쓰려면 print() 함수를 사용하면 편하다.

# infilename = input("파일 이름을 입력하시오: ").strip()
# infile = open(infilename, "r")
# file_s = infile.read()
# removed_s = input("삭제할 문자열을 입력하시오 ").strip()
# modified_s = file_s.replace(removed_s, "")

# infile.close()
# outfile = open(infilename, "w")

# print(modified_s, file = outfile, end="")
# print("변경된 파일이 저장되었습니다. 확인해보세요.")
# outfile.close()

# 3. 사용자가 입력하는 파일에 있는 각 문자들이 나타내는 빈도를 계산하는 프로그램을 작성하라.
#    텍스트 파일이므로 open(filename, "r")을 사용한다. 파일 안의 각 줄은 아래의 코드와 같이 하면 된다.
#    또한 각 줄 안의 문자들은 다시 for 루프를 사용하면 됩니다.

# filename = input("파일 이름을 입력하시오: ").strip()
# infile = open(filename, "r")        # 퀴즈입니다. 이부분에 에러를 해결하면 보너수 점수.
# for line in infile:
#     ...
# def countLine(line, counter):
#     for ch in line:
#         if ch.isalpha():
#             counter[ch] = counter[ch] + 1
#         else:
#             counter[ch] = 1
            
# fname = input("입력 파일 이름:  ").strip()
# infile = open(fname, "r")

# my_dict = {}
# for line in infile:
#     countLine(line, my_dict)

# print(my_dict)
# infile.close()
