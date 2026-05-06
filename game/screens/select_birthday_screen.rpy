## 생일 정하는 스크린 - init_setting_label에서 call됌
#
#

screen selet_birthday_screen:
    frame:
        text "1초 뒤에 이 창은 사라집니다."
    
    # 3.0초가 지나면 Return() 액션을 실행해라!
    timer 1.0 action Return()