#비밀번호 생성
def checkpassword(password):
    if len(password)<8 or (password.isalnum())!=True:
        return False
    else:
        return True
password=""
# password=(input("새로운 비밀번호를 입력하세요:"))
# if checkpassword(password)==True:
#     print("Good!비밀번호가 올바르게 생성되었습니다.")
# else:
#     print("오류! 비밀번호가 규칙에 맞지 않습니다.")

while True:
    password = (input("새로운 비밀번호를 입력하세요:"))
    if checkpassword(password) == True:
        print("Good!비밀번호가 올바르게 생성되었습니다.")
        break
    else:
        print("오류! 비밀번호가 규칙에 맞지 않습니다.")
        continue
