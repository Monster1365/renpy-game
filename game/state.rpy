## 기본 변수 설정
# 
#
init python:
    menu_btn_options = {
        "status": "status_button_label",
        "schedule": "schedule_button_label",
        "inventory": "inventory_button_label",
        "outing": "outing_button_label",
    }

    schedule_options = {
        "study1": {
            "title": "공부방",
            "status": {
                "increase": ["intellect", "stress"],
                "decrease": ["hp"]
            },
        },
        "study2": {
            "title": "애들과 뛰어놀기",
            "status": {
                "increase": ["hp", "strength", "stress"],
                "decrease": ["stress"]
            },
        },
        "study3": {
            "title": "언어교육",
            "status": {
                "increase": ["sociality", "attitude", "stress"],
                "decrease": []
            }
        },
        "study4": {
            "title": "예절수업",
            "status": {
                "increase": ["attitude", "morality", "stress"],
                "decrease": []
            }
        },
        "rest1": {
            "title": "마음수양",
            "status": {
                "increase": [],
                "decrease": ["stress"]
            }
        },
        "rest2": {
            "title": "외출",
            "status": {
                "increase": ["hp", "sociality"],
                "decrease": ["morality", "stress"]
            }
        },
        "adventure1": {
            "title": "adventure1",
            "status": {
                "increase": ["hp", "strength"],
                "decrease": ["stress"]
            }
        },
        "adventure2": {
            "title": "adventure2",
            "status": {
                "increase": ["hp", "strength"],
                "decrease": ["stress"]
            }
        },
        "adventure3": {
            "title": "adventure3",
            "status": {
                "increase": ["hp", "strength"],
                "decrease": ["stress"]
            }
        },
        "adventure4": {
            "title": "adventure4",
            "status": {
                "increase": ["hp", "strength"],
                "decrease": ["stress"]
            }
        },
    }

    outing_options = {
        "outing1": {
            "title": "restaurant",
            "choice": {
                "choice1": "dish1",
                "choice2": "dish2",
            },
        },
        "outing2": {
            "title": "variety store",
            "choice": {
                "choice1": "dish1",
                "choice2": "dish2",
            },
        },
        "outing3": {
            "title": "cathedral",
            "choice": {
                "choice1": "dish1",
                "choice2": "dish2",
            },
        },
        "outing4": {
            "title": "hospital",
            "choice": {
                "choice1": "dish1",
                "choice2": "dish2",
            },
        },
    }

    ## 객체 정의
    # 플레이어 정적 데이터
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
    class SL: # skill level
        def __init__(self, options):
            self.sl_dict = dict(zip(list(options.keys()), [1]*len(list(options.keys()))))

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
            self.SL = SL(schedule_options)

    # 아이템 정적 데이터
    class Item:
        """
        type: string -> clothes | belonging | book,
        serial: number,
        type_serial: number,
        category: category -> default, shop, drop...
        title: string,
        description: string,
        price: positive number,
        variance: string,
        quantity: number | default = 0,
        isEquipable: boolean | default = False,
        isConsumable: boolean | default = False,
        hasEvent: boolean | default = False,
        isShopItem: boolean | default = False,
        """
        def __init__(
                self,
                type,
                serial,
                type_serial,
                category,
                title,
                description,
                price,
                variance=None,
                isEquipable=False,
                isConsumable=False,
                hasEvent=False,
                isShopItem=False
            ):
            
            self.type = type
            self.serial = serial
            self.type_serial = type_serial
            self.title = title
            self.description = description
            self.price = price
            self.variance = variance
            self.isEquipable = isEquipable
            self.isConsumable = isConsumable
            self.hasEvent = hasEvent
            self.isShopItem = isShopItem
    
    # 게임 아이템 초기화
    ITEMS_DB = {
        "default_clothes": Item("clothes", 0, 0, "buy", "기본옷", "기본옷입니다.", "", 0, True),
        "cake": Item("belonging", 1, 0, "shop", "케이크", "설명", 100, "", False, True, False, True),
        "attitude_skill": Item("book", 2, 0, "shop", "예의의 기술", "설명", 100, "", False, True, False, True),
    }

init:
    ## 개발환경체크
    define ENV = "development"

    ## 게임 환경 설정
    # ========================================
    
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

    # ========================================



    ## 메뉴
    # ========================================

    # 메뉴 화면이 보이는 상태인지 아닌지 상태를 저장하는 변수
    default is_visible_menu = True

    # ========================================



    ## 스케줄
    # ========================================

    # 스케줄 선택 변수
    default scheduleSelect = ""

    # 선택된 스케줄 저장용 변수
    default scheduleList = []

    default record_schedule_result = []

    default now_schedule_result = ()

    # ========================================



    ## 외출
    # ========================================

    default outingSelect = ""

    # ========================================



    ## 게임 진행중 동적으로 변하는 변수 상태 관리 객체 생성
    # ========================================
    
    # 플레이어 객체
    default player = Player()

    # 아이템 객체 리스트
    # 아이템 시리얼 넘버 = index값
    define items_quantity = {
        "belongings": {
            "cake": 0,
        },
        "clothes": {
            "default_clothes": 1,
        },
        "books": {
            "attitude_skill": 0,
        },
    }

    # ========================================

    



    ## 이미지 불러오는 방식
    # image background = "assets/images/background.jpg"
