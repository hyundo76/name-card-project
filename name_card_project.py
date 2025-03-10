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
        name = (input("이름을 입력하세요 :").strip())

        phone = (input("전화번호를 입력하세요 :").strip())

        belong = (input("소속을 입력하세요 :").strip())

        print("입력이 완료 되었습니다")

        card = [(name),(phone),(belong),]

        business_card.append(card)

    elif menu == '2':
        print('/n 명함수정')
        name = input("수정할 명함의 이름을 입력하세요: ").strip()

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
        choice = input("번호 입력: ").strip()

        if choice == "1":
            business_card[index][0] = input("새로운 이름: ").strip()
        elif choice == "2":
            business_card[index][2] = input("새로운 전화번호: ").strip()
        elif choice == "3":
            business_card[index][1] = input("새로운 소속: ").strip()
        else:
            print("잘못된 입력입니다.")
            continue
        
        print("명함이 수정되었습니다.")
        print(f"수정된 정보: {business_card[index]}")

    elif menu == '3':
        print('명함삭제')
        if not business_card :
            print("삭제할 명함이 없습니다.")
        else :
             remove_name = input('삭제할 명함 이름을 입력하시오').strip()
             
             for i in range(len(business_card)) :
                if business_card[i][0] == remove_name :
                    index = i
                    print(f"'{remove_name}'님의 명함을 삭제하시겠습니까? ")
                    answer = input("예 / 아니요 ").strip()
                    if answer == '예' :
                        del business_card[index]
                        print(f"'{remove_name}'님의 명함이 삭제되었습니다.")
                    else :
                        print("삭제를 취소합니다.")
                break
             print("해당 이름의 명함을 찾을 수 없습니다.")
    elif menu == '4':
        print('명함목록보기')

        if len(business_card) == 0:
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
