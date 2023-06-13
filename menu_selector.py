import file_manager as fm
import parking_spot_manager as psm


def start_process(path):
    str_list = fm.read_file(path)  # file_manager의 read_file 함수로 .csv파일 읽기

    # parking_spot_manager의 str_list_to_class_list 함수로 parking_spot 객체 리스트로 변수 초기화
    spots = psm.str_list_to_class_list(str_list)

    while True:
        print("---menu---")  # task 선택
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            psm.print_spots(spots)  # spots 리스트에서 각 parking_spot 객체 속 주차장 정보(self.__item) 출력
            # fill this block
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                print("not implemented yet")
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                print("not implemented yet")
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                print("not implemented yet")
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                print("not implemented yet")
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                print("not implemented yet")
                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else:
                print("invalid input")
        elif select == 4:  # 4번 (exit) 고를 시 'Exit' 출력 후 반복문 종료.
            print("Exit")
            break
            # fill this block
        else:
            print("invalid input")
