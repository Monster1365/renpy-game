## 기본 변수 설정
## 딕셔너리로 관리, get/set으로 값 조회 및 수정
# 
# todo : item class 구현하기
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

    schedule_options = ["studyroom",
                        "playwithchild",
                        "learnlanguage",
                        "learnattitude",
                        "housework",
                        "lesson",
                        "hospitalwork",
                        "clotheswork",
                        "farmwork",
                        "mindset",
                        "outing",
                        "adventure"]

    ## 객체 정의
    # 플레이어 데이터 정의
    class Profile:
        def __init__(self):
            self.name = "character"
            self.birthday = None
            self.age = 10
            self.money = 600
    
    class Status:
        def __init__(self):
            self.hp = 30
            self.strength = 30
            self.attraction = 0
            self.morality = 0
            self.intellect = 0
            self.stress = 0
            self.sociality = 0
            self.attitude = 0

    class Times:
        def __init__(self):
            self.current_year = 2026
            self.current_month = 1
            self.current_day = 1

    class Player:
        """
        profile: Profile<obj> /
        status: Status<obj> /
        times: Times<obj>
        """
        def __init__(self):
            self.profile = Profile()
            self.status = Status()
            self.times = Times()

    # 아이템 데이터 정의
    class Item:
        """
        ===============
        Parameter: Tpye
        ===============

        serial: number,
        category: category -> default, shop, drop...
        title: string,
        description: string,
        price: positive number,
        variance: dict = {status: number},
        quantity: number | default = 0
        hasEvent: boolean | default = False
        isShopItem: boolean | default = False
        """
        def __init__(
                self,
                serial,
                category,
                title,
                description,
                price,
                variance,
                quantity=0,
                hasEvent=False,
                isShopItem=False
            ):
                    
            self.serial = serial
            self.title = title
            self.description = description
            self.price = price
            self.variance = variance
            self.quantity = quantity
            self.isEquipable = isEquipable
            self.isConsumable = isConsumable
            self.hasEvent = hasEvent
            self.isShopItem = isShopItem

    class BelongingItem(Item):
        """
        child_serial: number
        quantity: number | defaut = 0
        """
        def __init__(
                self,
                serial,
                child_serial,
                category,
                title,
                description,
                price,
                variance,
                hasEvent=False,
                isShopItem=False,
                quantity=0,
            ):
            super(). __init__(
                        serial,
                        category,
                        title,
                        description,
                        price,
                        variance,
                        hasEvent,
                        isShopItem
                    )
            self.child_serial = child_serial
            self.quantity = quantity
    
    class ClothesItem(Item):
        """
        child_serial: number
        """
        def __init__(
                self,
                serial,
                child_serial,
                category,
                title,
                description,
                price,
                variance,
                hasEvent=False,
                isShopItem=False,
            ):
            super(). __init__(
                        serial,
                        category,
                        title,
                        description,
                        price,
                        variance,
                        hasEvent,
                        isShopItem
                    )
            self.child_serial = child_serial
    
    class BookItem(Item):
        """
        child_serial: number
        quantity: number | defaut = 0
        """
        def __init__(
                self,
                serial,
                child_serial,
                category,
                title,
                description,
                price,
                variance,
                hasEvent=False,
                isShopItem=False,
                quantity=0,
            ):
            super(). __init__(
                        serial,
                        category,
                        title,
                        description,
                        price,
                        variance,
                        hasEvent,
                        isShopItem
                    )
            self.child_serial = child_serial
            self.quantity = quantity

init:

    ## 게임 환경 설정
    # 게임에서 사용할 시스템 대화창을 정의합니다.
    define system = Character('system', color="#c8ffc8")

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

    # 스케줄 선택 변수
    default nowSelect = ""

    # 선택된 스케줄 저장용 변수
    default scheduleList = []


    ## 게임 진행중 동적으로 변하는 변수 상태 관리 객체 생성
    # 플레이어 객체
    default player = Player()

    # 아이템 객체 생성
    # 예시) default book1 = Book()
    # 옷
    default default_clothes = ClothesItem(0, 0, "buy", "기본옷", "기본옷입니다.", 0, {})

    # 소모품
    default cake = BelongingItem(1, 0, "shop", "케이크", "설명", 100, {}, False, True, 0)

    # 책
    default attitude_skill = BookItem(2, 0, "shop", "예의의 기술", "설명", 100, {}, False, True, 0)

    # 아이템 객체 리스트
    # 아이템 시리얼 넘버 = index값
    define items = [
        default_clothes,
        cake,
        attitude_skill
    ]
    define clothes_items = [default_clothes]
    define belonging_items = [cake]
    define book_items = [attitude_skill]

    



    ## 이미지 불러오는 방식
    # image background = "assets/images/background.jpg"
