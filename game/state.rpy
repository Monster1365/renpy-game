## 기본 변수 설정
## 메모 1. 몬스터 딕셔너리: 변하지 않는 몬스터에 대한 정적 데이터를 담는 용도
## 메모 2. 몬스터 객체: 몬스터의 상태, 행동을 관리하기 위한 용도
#
init python:
################################################################################
## 딕셔너리 옵션
################################################################################
    menu_btn_options = {
        "status": "status_button_label",
        "schedule": "schedule_button_label",
        "inventory": "inventory_button_label",
        "outing": "outing_button_label",
    }

    schedule_options = {
        "study1": {
            "key": "study",
            "title": "글 배우기",
            "level": 1,
            "status": {
                "intellect": [1, 2],
                "sociality": [0, 1],
                "bond": [1, 2],
                "stress": [1, 1],
            },
            "stand": {
                "key": "intellect",
                "value": 10,
            },
        },
        "study2": {
            "key": "study",
            "title": "서적 탐독",
            "level": 2,
            "status": {
                "intellect": [1, 3],
                "sociality": [0, 1],
                "bond": [1, 1],
                "stress": [1, 2],
            },
            "stand": {
                "key": "intellect",
                "value": 30,
            },
        },
        "study3": {
            "key": "study",
            "title": "학문 연마",
            "level": 3,
            "status": {
                "intellect": [2, 4],
                "sociality": [1, 1],
                "bond": [1, 1],
                "stress": [2, 3],
            },
            "stand": {
                "key": "intellect",
                "value": 80,
            },
        },
        "study4": {
            "key": "study",
            "title": "수사학",
            "level": 3,
            "status": {
                "intellect": [1, 2],
                "sociality": [1, 4],
                "bond": [1, 1],
                "stress": [2, 3],
            },
            "stand": {
                "key": "intellect",
                "value": 80,
            },
        },
        "dress1": {
            "key": "dress",
            "title": "몸단장",
            "level": 1,
            "status": {
                "attraction": [1, 2],
                "attitude": [0, 1],
                "stress": [1, 1],
            },
            "stand": {
                "key": "attraction",
                "value": 10,
            },
        },
        "dress2": {
            "key": "dress",
            "title": "옷차림 익히기",
            "level": 2,
            "status": {
                "attraction": [2, 2],
                "attitude": [0, 2],
                "stress": [1, 1],
            },
            "stand": {
                "key": "attraction",
                "value": 30,
            },
        },
        "fight1": {
            "key": "fight",
            "title": "호신술",
            "level": 1,
            "status": {
                "hp": [1, 3],
                "strength": [0, 2],
                "intellect": [0, 1],
                "stress": [1, 2],
            },
            "stand": {
                "key": "strength",
                "value": 10,
            },
        },
        "fight2": {
            "key": "fight",
            "title": "격투술",
            "level": 2,
            "status": {
                "hp": [2, 5],
                "strength": [1, 4],
                "intellect": [0, 1],
                "stress": [2, 4],
            },
            "stand": {
                "key": "strength",
                "value": 30,
            },
        },
        "manner1": {
            "key": "manner",
            "title": "기초 예법",
            "level": 1,
            "status": {
                "attraction": [0, 1],
                "attitude": [1, 2],
                "stress": [1, 1],
            },
            "stand": {
                "key": "attitude",
                "value": 10,
            },
        },
        "manner2": {
            "key": "manner",
            "title": "고급 예법",
            "level": 2,
            "status": {
                "attraction": [0, 1],
                "attitude": [2, 4],
                "stress": [1, 2],
            },
            "stand": {
                "key": "attitude",
                "value": 30,
            },
        },
        "music1": {
            "key": "music",
            "title": "음악 입문",
            "level": 1,
            "status": {
                "attraction": [0, 1],
                "music": [1, 2],
                "stress": [1, 1],
            },
            "stand": {
                "key": "music",
                "value": 10,
            },
        },
        "music2": {
            "key": "music",
            "title": "피아노 교습",
            "level": 2,
            "status": {
                "attraction": [0, 2],
                "music": [1, 3],
                "stress": [1, 2],
            },
            "stand": {
                "key": "music",
                "value": 10,
            },
        },
        "music3": {
            "key": "music",
            "title": "독주회 준비",
            "level": 3,
            "status": {
                "attraction": [0, 2],
                "music": [2, 5],
                "stress": [1, 3],
            },
            "stand": {
                "key": "music",
                "value": 10,
            },
        },
        "mindset": {
            "key": "mindset",
            "title": "마음수양",
            "level": 1,
            "status": {
                "morality": [1, 2],
                "stress": [-1, -1],
                "recall": [1, 1],
            },
        },
        "reading": {
            "key": "reading",
            "title": "독서",
            "level": 1,
            "status": {
                "intellect": [1, 1],
                "attraction": [1, 1],
                "music": [1, 1],
                "stress": [-1, -1],
            },
        },
        "outing": {
            "key": "outing",
            "title": "외출",
            "level": 1,
            "status": {
                "hp": [1, 1],
                "morality": [-1, -1],
                "sociality": [0, 1],
                "stress": [-3, -3],
            },
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

    # 모든 캐릭터 정적 문서 데이터
    character_data = {
        "schedule": {
            "teacher": {
                "attraction": {},
                "fight": {},
                "attitude": {},
                "music": {},
                "mindset": {},
            },
        },
        "monster": {
            "nothuman": {
                "dogs": {
                    "hp": 80,
                    "attack": 18,
                    "defense": 8,
                    "money": [15, 30],
                    "drop": ["dog_meet", "dog_skin"],
                    "rate": 20
                    "habitat": ["street", "swamp", "mountain"],
                },
                "fox": {
                    "hp": 60,
                    "attack": 15,
                    "defense": 5,
                    "money": [10, 20],
                    "drop": ["fox_fur"],
                    "rate": 20
                    "habitat": ["swamp", "mountain"],
                },
                "wolf": {
                    "hp": 140,
                    "attack": 32,
                    "defense": 16,
                    "money": [40, 70],
                    "drop": ["fang"],
                    "rate": 20
                    "habitat": ["swamp", "mountain"],
                },
                "boar": {
                    "hp": 220,
                    "attack": 38,
                    "defense": 30,
                    "money": [50, 100],
                    "drop": ["boar_tooth"],
                    "rate": 20
                    "habitat": ["swamp", "mountain"],
                },
                "bear": {
                    "hp": 420,
                    "attack": 55,
                    "defense": 45,
                    "money": [180, 260],
                    "drop": ["bear_skin"],
                    "rate": 20
                    "habitat": ["swamp", "mountain"],
                },
            },
            "human": {
                "bandit": {
                    "hp": 180,
                    "attack": 35,
                    "defense": 20,
                    "money": [120, 180],
                    "drop": ["knife"],
                    "rate": 20
                    "habitat": ["mountain"],
                },
                "pickpocket": {
                    "hp": 90,
                    "attack": 20,
                    "defense": 8,
                    "money": [40, 100],
                    "drop": [],
                    "rate": 20
                    "habitat": ["street"],
                },
                "scammer": {
                    "hp": 120,
                    "attack": 10,
                    "defense": 12,
                    "money": [20, 80],
                    "drop": [],
                    "rate": 20
                    "habitat": ["street"],
                },
                "swampwoman": {
                    "hp": 260,
                    "attack": 42,
                    "defense": 28,
                    "money": [20, 150],
                    "drop": [], # 기억조각
                    "rate": 20
                    "habitat": ["swamp", "around_swamp"],
                },
                "peddler": {
                    "hp": 170,
                    "attack": 20,
                    "defense": 35,
                    "money": [15, 30],
                    "drop": [], # 고급아이템
                    "rate": 20
                    "habitat": ["swamp", "mountain"],
                },
                "traitor": {
                    "hp": 300,
                    "attack": 70,
                    "defense": 50,
                    "money": [0, 0],
                    "drop": [],
                    "rate": 20
                    "habitat": ["mountain"],
                },
            },
        },
    }

    item_data = {
        "rye_bread": {
            "id": 1,
            "type": "belongings",
            "category": "eatery_store",
            "title": "호밀빵",
            "description": "호밀빵이다. 체력을 15증가시키고 근력을 5증가시킨다.",
            "price": 180,
            "sell": 90,
            "isEquipable": False,
            "isConsumable": True,
            "status": {
                "hp": 15,
                "strength": 5,
            },
            "heal": 0,
            "attack": 0,
            "defense": 0,
        },
        "roast": {
            "id": 2,
            "type": "belongings",
            "category": "eatery_store",
            "title": "고기구이",
            "description": "고기구이다.",
            "price": 420,
            "sell": 210,
            "isEquipable": False,
            "isConsumable": True,
            "status": {
                "hp": 40,
                "strength": 10,
            },
            "heal": 0,
            "attack": 0,
            "defense": 0,
        },
        "stew": {
            "id": 3,
            "type": "belongings",
            "category": "eatery_store",
            "title": "스튜",
            "description": "스튜이다.",
            "price": 200,
            "sell": 100,
            "isEquipable": False,
            "isConsumable": True,
            "status": {
                "hp": 25,
            },
            "heal": 0,
            "attack": 0,
            "defense": 0,
        },
        "small_potion": {
            "id": 4,
            "type": "belongings",
            "category": "general_store",
            "title": "작은 회복약",
            "description": "작은 회복약이다.",
            "price": 80,
            "sell": 40,
            "isEquipable": False,
            "isConsumable": True,
            "status": {},
            "heal": 30,
            "attack": 0,
            "defense": 0,
        },
        "potion": {
            "id": 5,
            "type": "belongings",
            "category": "general_store",
            "title": "회복약",
            "description": "회복약이다.",
            "price": 500,
            "sell": 250,
            "isEquipable": False,
            "isConsumable": True,
            "status": {},
            "heal": 300,
            "attack": 0,
            "defense": 0,
        },
        "dumbbell": {
            "id": 6,
            "type": "belongings",
            "category": "general_store",
            "title": "아령",
            "description": "아령이다.",
            "price": 500,
            "sell": 250,
            "isEquipable": False,
            "isConsumable": True,
            "status": {
                "hp": 20,
                "strength": 15,
            },
            "heal": 0,
            "attack": 0,
            "defense": 0,
        },
        "cosmetics": {
            "id": 7,
            "type": "belongings",
            "category": "general_store",
            "title": "화장품",
            "description": "화장품이다.",
            "price": 700,
            "sell": 350,
            "isEquipable": False,
            "isConsumable": True,
            "status": {
                "attraction": 20,
            },
            "heal": 0,
            "attack": 0,
            "defense": 0,
        },
        "knife": {
            "id": 8,
            "type": "clothes",
            "category": "general_store",
            "title": "단검",
            "description": "단검이다.",
            "price": 400,
            "sell": 0,
            "isEquipable": True,
            "isConsumable": False,
            "status": {},
            "heal": 0,
            "attack": 15,
            "defense": 0,
        },
        "silver_sword": {
            "id": 9,
            "type": "clothes",
            "category": "general_store",
            "title": "은검",
            "description": "은검이다.",
            "price": 1000,
            "sell": 0,
            "isEquipable": True,
            "isConsumable": False,
            "status": {},
            "heal": 0,
            "attack": 40,
            "defense": 0,
        },
        "knight_sword": {
            "id": 10,
            "type": "clothes",
            "category": "general_store",
            "title": "기사의 검",
            "description": "기사의 검이다.",
            "price": 2500,
            "sell": 0,
            "isEquipable": True,
            "isConsumable": False,
            "status": {},
            "heal": 0,
            "attack": 90,
            "defense": 0,
        },
        "leather_armor": {
            "id": 11,
            "type": "clothes",
            "category": "general_store",
            "title": "가죽 갑옷",
            "description": "가죽 갑옷이다.",
            "price": 800,
            "sell": 0,
            "isEquipable": True,
            "isConsumable": False,
            "status": {},
            "heal": 0,
            "attack": 0,
            "defense": 20,
        },
        "iron_armor": {
            "id": 12,
            "type": "clothes",
            "category": "general_store",
            "title": "철 갑옷",
            "description": "철 갑옷이다.",
            "price": 1500,
            "sell": 0,
            "isEquipable": True,
            "isConsumable": False,
            "status": {},
            "heal": 0,
            "attack": 0,
            "defense": 40,
        },
        "knight_armor": {
            "id": 13,
            "type": "clothes",
            "category": "general_store",
            "title": "기사의 갑옷",
            "description": "기사의 갑옷이다.",
            "price": 3400,
            "sell": 0,
            "isEquipable": True,
            "isConsumable": False,
            "status": {},
            "heal": 0,
            "attack": 0,
            "defense": 65,
        },
        "dress": {
            "id": 14,
            "type": "clothes",
            "category": "general_store",
            "title": "드레스",
            "description": "드레스이다.",
            "price": 5000,
            "sell": 0,
            "isEquipable": True,
            "isConsumable": False,
            "status": {
                "attraction": 120,
            },
            "heal": 0,
            "attack": 0,
            "defense": 0,
        },
        "dog_skin": {
            "id": 15,
            "type": "belongings",
            "category": "monster_drop",
            "title": "들개 가죽",
            "description": "들개 가죽이다.",
            "price": 0,
            "sell": 100,
            "isEquipable": False,
            "isConsumable": False,
            "status": {},
            "heal": 0,
            "attack": 0,
            "defense": 0,
        },
        "fox_fur": {
            "id": 16,
            "type": "belongings",
            "category": "monster_drop",
            "title": "여우털",
            "description": "여우털이다.",
            "price": 0,
            "sell": 180,
            "isEquipable": False,
            "isConsumable": False,
            "status": {},
            "heal": 0,
            "attack": 0,
            "defense": 0,
        },
        "fang": {
            "id": 17,
            "type": "belongings",
            "category": "monster_drop",
            "title": "송곳니",
            "description": "송곳니이다.",
            "price": 0,
            "sell": 300,
            "isEquipable": False,
            "isConsumable": False,
            "status": {},
            "heal": 0,
            "attack": 0,
            "defense": 0,
        },
        "boar_tooth": {
            "id": 18,
            "type": "belongings",
            "category": "monster_drop",
            "title": "멧돼지 엄니",
            "description": "멧돼지 엄니이다.",
            "price": 0,
            "sell": 500,
            "isEquipable": False,
            "isConsumable": False,
            "status": {},
            "heal": 0,
            "attack": 0,
            "defense": 0,
        },
        "bear_skin": {
            "id": 19,
            "type": "belongings",
            "category": "monster_drop",
            "title": "곰가죽",
            "description": "곰가죽이다.",
            "price": 0,
            "sell": 1000,
            "isEquipable": False,
            "isConsumable": False,
            "status": {},
            "heal": 0,
            "attack": 0,
            "defense": 0,
        },
        "dog_meet": {
            "id": 20,
            "type": "belongings",
            "category": "monster_drop",
            "title": "들개 고기",
            "description": "익힌 고기이다.",
            "price": 0,
            "sell": 80,
            "isEquipable": False,
            "isConsumable": True,
            "status": {
                "hp": 10,
                "strength": 2,
            },
            "heal": 0,
            "attack": 0,
            "defense": 0,
        },
    }

################################################################################
## 객체 정의
################################################################################
    # 플레이어 정적 데이터
    class Profile:
        def __init__(self):
            self.name = "character"
            self.birthday = None
            self.age = 10
            self.money = 600
    
    # 플레이어 스테이터스
    class Status:
        def __init__(self):
            self.hp = 30 # 체력
            self.strength = 30 # 근력
            self.attraction = 0 # 매력
            self.morality = 0 # 도덕
            self.intellect = 0 # 지력
            self.stress = 0# 스트레스
            self.sociality = 0 # 화술
            self.attitude = 0 # 예의
            self.recall = 0 # 회상
            self.bond = 0 # 유대
            self.music = 0 #음악

    # 게임 날짜
    class Times:
        def __init__(self):
            self.current_year = 2026
            self.current_month = 1
            self.current_day = 1

    # 스케줄 레벨
    class Skill: # skill level
        def __init__(self, options): # player.skill.sill_level["key"] -> int
            self.skill_level = {
                "study": 1,
                "dress": 1,
                "fight": 1,
                "manner": 1,
                "music": 1,
            }
            self.max_level = {
                "study": 3,
                "dress": 2,
                "fight": 5,
                "manner": 4,
                "music": 3,
            }
            self.skill_count = {
                "study1": 0,
                "study2": 0,
                "study3": 0,
                "study4": 0,
                "dress1": 0,
                "dress2": 0,
                "fight1": 0,
                "fight2": 0,
                "manner1": 0,
                "manner2": 0,
                "music1": 0,
                "music2": 0,
                "music3": 0,
            }

    # 플레이어
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
            self.skill = Skill(schedule_options)

        def getRatingProp(self):
            return (self.status.hp, self.status.morality, self.status.stress)

    # class Character:
    #     pass
    # 아이템 정적 데이터
    class Item:
        """
        quantity: number | default = 0,
        equipped: boolean | default = False,
        """
        def __init__(self, name, quantity=0, equipped=False):
            self.name = name
            self.quantity = quantity
            self.equipped = equipped
    
    class Monster:
        def __init__(self, name, hp, attack, defense, money, drop, rate):
            self.name = name
            self.hp = hp
            self.attack = attack
            self.defense = defense
            self.money = money
            self.drop = drop
            self.rate = rate
        
        def takeDamage(self, var):
            self.hp = (self.hp + self.defense) - var
        def attack(self):
            pass
        def dropMoney(self):
            pass # 랜덤함수
        def dropItem(self):
            pass # 랜덤함수

init: # 렌파이에 저장되는 동적 변수
################################################################################
## 게임 환경 설정
################################################################################
    ## 개발환경체크
    define ENV = "development"

    ## 게임 환경 설정
    
    # 게임에서 사용할 시스템 대화창을 정의합니다.
    define system = Character('system', color="#c8ffc8")

    # 화면 최대 크기
    define X_FULL = 1920
    define Y_FULL = 1080

    # 화면 비율 설정
    define TOP_LAYOUT_HEIGHT = 100
    define MIDDLE_LAYOUT_HEIGHT = 850
    define BOTTOM_LAYOUT_HEIGHT = 130

    # 환경변수 설정
    define TIME_DISPLAY = "days" # or weeks

    # 기본 설정 값김
    define MAX_YEAR = 2
    define MAX_MONTH = 12
    define MAX_DAY = 21

################################################################################
## 메뉴 관련 변수
################################################################################
    ## 메뉴

    # 메뉴 화면이 보이는 상태인지 아닌지 상태를 저장하는 변수
    default is_visible_menu = True

################################################################################
## 스케줄 관련 변수
################################################################################
    ## 스케줄

    # 스케줄 선택 변수
    default scheduleSelect = ""

    # 선택된 스케줄 저장용 변수
    # action의 clearSchedule 참조
    default scheduleList = []

    # 스케줄 결과 전체 저장용
    default record_schedule_result = []

    default now_schedule_result = ()

    # study에서 level에 따라 학습 가능한 스케줄이 다르므로 유동적으로 변하는 ui구현을 위한 변수
    # 현재 실행 가능한 스케줄 항목을 리스트에 저장
    # action의 show_study_schedule_button 참조
    default available_study_schedule_list = []

    # todo count schedule

################################################################################
## 외출 관련 변수
################################################################################
    ## 외출

    default outingSelect = ""

################################################################################
## 객체 생성
################################################################################
    ## 게임 진행중 동적으로 변하는 변수 상태 관리 객체 생성
    
    # 플레이어 객체
    default player = Player()

    #CHARACTER_DB
    
    # 게임 아이템 초기화
    default ITEMS_DB = {
        "rye_bread": Item("rye_bread"),
        "roast": Item("roast_roast"),
        "stew": Item("stew"),
        "small_potion": Item("small_potion"),
        "potion": Item("potion"),
        "dumbbell": Item("dumbbell"),
        "cosmetics": Item("cosmetics"),
        "knife": Item("knife"),
        "silver_sword": Item("silver_sword"),
        "knight_sword": Item("knight_sword"),
        "leather_armor": Item("leather_armor"),
        "iron_armor": Item("iron_armor"),
        "knight_armor": Item("knight_armor"),
        "dress": Item("dress"),
        "dog_skin": Item("dog_skin"),
        "fox_fur": Item("fox_fur"),
        "fang": Item("fang"),
        "boar_tooth": Item("boar_tooth"),
        "bear_skin": Item("bear_skin"),
    }

    ## 설정
    default is_visible_setting_btn = True

    ## 이미지 불러오는 방식
    # image background = "assets/images/background.jpg"
