## 커스텀 action 정의
#
#

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

## 메뉴 선택 액션 객체 생성
## status, schedule... 등의 버튼을 눌렀을때 선택된 버튼이 Action에 담김
## Action을 opion으로 넘겨줌
## 앞서 정의해준 menu_btn_options에서 Actoin랑 키 값을 매칭해서 알맞은 value값을 넘겨줌
## value에는 이동할 label이 들어있고 renpy.jump()함수로 label로 넘어감
## 사용예시: textbutton status action MenuButton("status")
## 게임 실행시 파일이 한번에 모두 실행되서(컴파일말고 게임 실행시 스크린 그릴때) 객체는 그때 한번만 생성하는 듯..?
#
#
    class MenuButton(Action):
        # 객체가 생성될때 초기화되는 매직 메서드
        def __init__(self, option):
            self.option = option

        # 객체를 함수처럼 호출할수 있게 해주는 매직 메서드
        def __call__(self):
            renpy.jump(menu_btn_options[self.option]) # game/label/action_label로 이동



## 나중에 구현 할 것
## 액션 예시
#     class MyAction(Action):
#         def __init__(self, label_name):
#             self.label_name = label_name

#         def __call__(self):
#             renpy.jump(self.label_name)



## 아이템 선택
#     class SelectItem(Action):
#         def __init__(self, item):
#             self.item = item

#         def __call__(self):
#             store.selected_item = self.item

#         def get_selected(self):
#             return store.selected_item == self.item



## 스탯 변경
#     class AddStat(Action):
#         def __init__(self, stat, amount):
#             self.stat = stat
#             self.amount = amount

#         def __call__(self):
#             setattr(store, self.stat, getattr(store, self.stat) + self.amount)

