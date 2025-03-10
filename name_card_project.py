display = ('''
-----------------------------------------------------------
1. 명함입력, 2. 명함수정, 3. 명함삭제 4. 명함목록보기, 5.종료
-----------------------------------------------------------
메뉴를 선택하세요 >>> ''')

business_card = []
menu = ''

while True :
    menu = input(display)
    if menu == '1':
        print('(명함입력)')
        print("명함 정보를 입력하세요:")
        name = input("이름: ")
        email = input("이메일: ")
        phone = input("전화번호: ")
        belong = input("소속 : ")

        name_card = [name]
        business_card.append(name_card)
        email_card = [email]
        business_card.append(email_card)
        phone_card = [phone]
        business_card.append(phone_card)
        belong_card = [belong]
        business_card.append(belong)
        print(f"{name}님의 명함이 입력되었습니다.")
        print(name, email, phone, belong)
      
    elif menu == '2':
        print('명함수정')
        Q1 = input('수정할 명함이 있습니까? (Y / N)')
        if Q1 == 'Y' :
            name1 = input("수정할 사람의 이름을 입력하시오.")
            if name1 in name_card in business_card : 
                found = name_card.index(name1)
                email_card[found] = input('새 이메일 :')
                phone_card[found] = input('새 전화번호 :')
                belong_card[found] = input('새 소속 :')
                print(f"'{name}'님의 명함이 수정되었습니다.")
                print(name_card[found], email_card[found], phone_card[found], belong_card[found])
            else : 
                print("해당 이름의 명함을 찾을 수 없습니다.")


    elif menu == '3':
        print('명함삭제')
        if not business_card :
            print("삭제할 명함이 없습니다.")
            continue
        
        remove_name = input('삭제할 명함 이름을 입력하시오')

            for i, business_card :
                if card[0] == remove_name :
              index = business_card.index(remove_name)
             print(f"'{name}'님의 명함을 삭제하시겠습니까? ")
             answer = input("예 / 아니요 ")
              for answer == '예' :
                   del business_card[]
            
              else : print("해당 이름의 명함을 찾을 수 없습니다.")
    elif menu == '4':
        print('명함목록보기')

    elif menu == '5':
        print('프로그램 종료')
        break
    else :
        print('메뉴선택을 잘못함.')

