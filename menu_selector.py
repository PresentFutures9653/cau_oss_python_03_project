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
            print("---filter by---")  # 필터링 기준 정보 선택
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:  # 자원명 기준 필터링
                keyword = input('type name:')
                spots = psm.filter_by_name(spots, keyword)
                # fill this block
            elif select == 2:  # 도시명 기준 필터링
                keyword = input('type city:')
                spots = psm.filter_by_city(spots, keyword)
                # fill this block
            elif select == 3:  # 시/군/구 기준 필터링
                keyword = input('type district:')
                spots = psm.filter_by_district(spots, keyword)
                # fill this block
            elif select == 4:  # 주차장유형 기준 필터링
                keyword = input('type ptype:')
                spots = psm.filter_by_ptype(spots, keyword)
                # fill this block
            elif select == 5:  # 좌표(위도/경도) 기준 필터링
                min_lat = float(input('type min lat:'))  # 최저 위도 입력
                max_lat = float(input('type max lat:'))  # 최고 위도 입력
                min_lon = float(input('type min long:'))  # 최저 경도 입력
                max_lon = float(input('type max long:'))  # 최고 경도 입력
                spots = psm.filter_by_location(spots, (min_lat, max_lat, min_lon, max_lon))
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
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']  # 정렬 시 기준 정보명 리스트
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')  # 정렬 기준 입력
            if keyword in keywords:  # 만약 keyword가 keywords 리스트 안에 있는, 유효한 값이면 실행
                spots = psm.sort_by_keyword(spots, keyword)  # 정렬 함수
            else:
                print("invalid input")
        elif select == 4:  # 4번 (exit) 고를 시 'Exit' 출력 후 반복문 종료.
            print("Exit")
            break
            # fill this block
        else:
            print("invalid input")
