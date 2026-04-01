## 기본 변수 설정
## 딕셔너리로 관리, get/set으로 값 조회 및 수정
#
#

## 객체로 상태 관리
init python:

    ## 선택 상태 - 딕셔너리로 저장
    ## staus, schedule 등의 선택을 넣는 딕셔너리 구조
    #
    #
    menu_btn_options = {
        "status": "status_button_label",
        "schedule": "schedule_button_label",
        "inventory": "inventory_button_label",
        "outing": "outing_button_label",
    }
    


    class Profile:
        def __init__(self):
            self.name = "character"
            self.age = 10
            self.money = 600
    
    class Status:
        def __init__(self):
            self.hp = 100
            self.strength = 100
            self.attraction = 100
            self.morality = 100
            self.intellect = 100
            self.stress = 100

    class Times:
        def __init__(self):
            self.current_year = 2026
            self.current_month = 1
            self.current_day = 1

    class Player:
        def __init__(self):
            self.profile = Profile()
            self.status = Status()
            self.times = Times()

init:

    # 화면 최대 크기
    define X_FULL = 1920
    define Y_FULL = 1080

    # 화면 비율 설정
    define TOP_LAYOUT_HEIGHT = 100
    define MIDDLE_LAYOUT_HEIGHT = 880
    define BOTTOM_LAYOUT_HEIGHT = 100

    # 환경변수 설정
    define TIME_DISPLAY = "days" # or weeks

    # 기본 설정 값김
    define MAX_YEAR = 8
    define MAX_MONTH = 12
    define MAX_DAY = 30

    # 메뉴 화면이 보이는 상태인지 아닌지 상태를 저장하는 변수
    default is_visible_menu = True

    ## 게임 진행중 동적으로 변하는 변수 상태 관리 객체 생성
    default player = Player()


    ## 이미지 불러오는 방식
    # image background = "assets/images/background.jpg"
