## 아무 배경이나 누르면 닫히는 스크린
## Show("plain_screen", inner_frame="test_cmp")로 호출가능
## inner_frame에는 plain_screen위에 뛰울 팝업UI의 스크린 이름을 넣어주면 됌
#

screen plain_screen(inner_screen):
    button:
        action Hide("plain_screen")

        frame:
            xfill True
            yfill True

            background "#45c185"

            use expression inner_screen