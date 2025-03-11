import sys

display = '''
-------------------------------------------------------------
1. 명함입력, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료
-------------------------------------------------------------
메뉴를 선택하세요 >>> '''

business_card = [
    ['홍길동', '010-1234-5678', '삼성전자'],
    ['김영희', '010-2345-6789', 'LG화학'],
    ['이철수', '010-3456-7890', '카카오']
]

menu = ''
while True:
    menu = input(display)
    if menu == '1':
        print('명함입력')

        while True:
            name = (input("이름을 입력하세요 :").strip())
            check = False
            for i, card in enumerate(business_card):
                if card[0] == name:
                    check = True
                    print("중복된 이름입니다.")
                    break
                
            if not check:
                print("중복되지 않은 이름입니다.")
                break
                    
        phone = (input("전화번호를 입력하세요 :").strip())
        belong = (input("소속을 입력하세요 :").strip())


        card = [name, phone, belong]
        business_card.append(card)
        print("입력이 완료되었습니다.")

    elif menu == '2':
        print('명함수정')
        name = input("수정할 명함의 이름을 입력하세요: ").strip()
        
        check = 0
        for card in business_card:
            if name == card[0]:
                while True:   
                    choice = int(input('수정할 값을 선택하세요>>> 1. 이름 2. 전화번호 3. 소속'))
                    if choice in (1,2,3):
                        card[choice - 1] = input('수정할 값: ').strip()
                        print("수정이 완료되었습니다.")
                        check = 1
                        break
                    else: 
                        print("경고: 1, 2, 3 중 하나를 선택하세요")
        if check == 0:
            print('해당 이름의 명함이 없습니다.')       
                        
    elif menu == '3':
        print('명함삭제')
        if not business_card :
            print("삭제할 명함이 없습니다.")
        else :
             remove_name = input('삭제할 명함 이름을 입력하시오').strip()
             
             check = 0
             for i in range(len(business_card)) :
                if business_card[i][0] == remove_name :
                    index = i
                    print(f"'{remove_name}'님의 명함을 삭제하시겠습니까? ")
                    answer = input("예 / 아니요 ").strip()
                    check = 1
                    if answer == '예' :
                        del business_card[index]
                        print(f"'{remove_name}'님의 명함이 삭제되었습니다.")
                    else :
                        print("삭제를 취소합니다.")
                    break
             if check == 0:
                print("해당 이름의 명함을 찾을 수 없습니다.")
    elif menu == '4':
        print('명함목록보기')
        if not business_card:
            print("저장된 명함이 없습니다.")
        else:
            for i, card in enumerate(business_card, start=1):
                print(f"{i} | 이름 : {card[0]} | 전화번호 : {card[1]} | 소속 : {card[2]}")

    elif menu == '5':
        print('프로그램 종료')
        sys.exit()
    else:
        print('메뉴선택을 잘못하셨습니다. 1 ~ 5 중 선택하세요.')
