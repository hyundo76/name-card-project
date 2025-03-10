## 명함관리 프로그램 작성
# 1. 명함입력, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료

import sys

display = '''
-------------------------------------------------------------
1. 명함입력, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료
-------------------------------------------------------------
메뉴를 선택하세요 >>> '''

business_card = []

menu = ''
while True:
    menu = input(display)
    if menu == '1':
        print('명함입력')
        name = (input("이름을 입력하세요 :"))

        phone = (input("전화번호를 입력하세요 :"))

        belong = (input("소속을 입력하세요 :"))

        print("입력이 완료 되었습니다")

        card = [(name),(phone),(belong),]

        business_card.append(card)

    elif menu == '2':
        print('명함수정')
    elif menu == '3':
        print('명함삭제')
    elif menu == '4':
        print('명함목록보기')

        if len(buisness_card) == 0:
            print("저장된 명함이 없습니다.")
        else:
            for i in range(len(business_card)):
                card = business_card[i]
                print(f"{i+1} | 이름 : {card[0]} | 소속 : {card[1]} | 전화번호 : {card[2]}")

    elif menu == '5':
        print('프로그램 종료')
        sys.exit()
    else:
        print('메뉴선택을 잘못하셨습니다.')
