## 측면의 메뉴버튼 컴포넌트
# 
# option인자에는 문자열 값이 들어옴 ex) "status"
#

screen menu_btn_component(option):
    frame:
        textbutton option action MenuButton(option)