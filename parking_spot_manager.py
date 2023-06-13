class parking_spot:
    # 생성자. 주차장 정보를 매개변수로 받아 self.__item 선언. 위도/경도 제외 모두 문자열.
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {'name': name,  # 자원명
                       'city': city,  # 도시 이름
                       'district': district,  # 시/군/구
                       'ptype': ptype,  # 주차장 유형
                       'longitude': float(longitude),  # 경도
                       'latitude': float(latitude)}  # 위도

    # self.__item getter.
    def get(self, keyword='name'):
        return self.__item[keyword]

    # you have to implement 'constructor(생성자)' and 'get' method

    # self.__item(주차장 정보) 형식 맞춰 출력하는 함수
    def __str__(self):
        item = self.__item
        s = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s


# 주차장 정보 문자열 리스트를 입력받아 순번 제외한 정보들을 토대로 객체 생성 후 리스트에 저장, 반환하는 함수.
def str_list_to_class_list(str_list):
    return [parking_spot(*i.split(',')[1:7]) for i in str_list]


# parking_spot 객체 리스트 요소 개수 출력 후 각 객체 __str__() 메서드로 주차장 정보들 차례로 출력
def print_spots(spots):
    print(f'"---print elements({len(spots)})---"')

    for data in spots:
        print(data.__str__())


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)

    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)
