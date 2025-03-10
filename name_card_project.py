## 명함관리 프로그램 작성
# 1. 명함입력, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료

import sys

display = '''
-------------------------------------------------------------
1. 명함입력, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료
-------------------------------------------------------------
메뉴를 선택하세요 >>> '''

menu = ''
while True:
    menu = input(display)
    if menu == '1':
        print('명함입력')
        
    elif menu == '2':
        print('/n 명함수정')
        name = input("수정할 명함의 이름을 입력하세요: ")

        index = -1
        a = 0
        while a < len(business_card):
            if business_card[a][0] == name:
                index = a
                break
            a += 1

        if index == -1:
            print("해당 명함이 없습니다.")
            continue
        
        print(f"현재 정보: {business_card[index]}")
        print("수정할 항목을 선택하세요: 1. 이름  2. 전화번호  3. 소속")
        choice = input("번호 입력: ")

        if choice == "1":
            business_card[index][0] = input("새로운 이름: ")
        elif choice == "2":
            business_card[index][2] = input("새로운 전화번호: ")
        elif choice == "3":
            business_card[index][1] = input("새로운 소속: ")
        else:
            print("잘못된 입력입니다.")
            continue
        
        print("명함이 수정되었습니다.")
        print(f"수정된 정보: {business_card[index]}")

    elif menu == '3':
        print('명함삭제')
    elif menu == '4':
        print('명함목록보기')
    elif menu == '5':
        print('프로그램 종료')
        sys.exit()
    else:
        print('메뉴선택을 잘못하셨습니다.')
