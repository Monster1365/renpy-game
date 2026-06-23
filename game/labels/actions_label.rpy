## 팝업 컴포넌트를 띄움. 이때 call을 사용해서 popup이 닫힐때 return을 받아야만 다음 줄인 show scren...을 실행할 수 있음
## 그렇기 때문에 call한게 반환될 때 까지 게임의 제어권이 action_label에게 넘어가 있는 상태임
## 그리고 return을 받아서 call이 종료되면 다음 줄들을 실행하고 마지막에 jump로 다시 제어권을 main_loop로 넘김
#
#

label status_button_label:
    call screen plain_screen(inner_screen="status_component")
    $ is_visible_menu=True
    jump main_loop


## 아래는 구현해야할 것들
label schedule_button_label:
    call screen plain_screen(inner_screen="schedule_component")
    $ is_visible_menu=True
    if _return == "go_schedule":
        jump schedule_test
    jump main_loop

label inventory_button_label:
    call screen plain_screen(inner_screen="inventory_component")
    $ is_visible_menu=True
    jump main_loop

label outing_button_label:
    call screen plain_screen(inner_screen="outing_component")
    $ is_visible_menu=True
    jump main_loop

label setting_label:
    $ is_visible_setting_btn=False
    call screen plain_screen(inner_screen="preferences")
    $ is_visible_setting_btn=True
    jump main_loop

label schedule_test:
    call screen plain_screen(inner_screen="preferences")
    jump main_loop