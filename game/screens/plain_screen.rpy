## 아무 배경이나 누르면 닫히는 스크린
## Show("plain_screen", inner_frame="test_cmp")로 호출가능
## inner_frame에는 plain_screen위에 뛰울 팝업UI의 스크린 이름을 넣어주면 됌
#
#

screen plain_screen(inner_screen):
    button:
        action [Hide(inner_screen), Hide("plain_screen"), Return()]

        frame:
            xfill True
            yfill True

            # 색상 코드 위에 두자리 숫자 투명도
            background "#45c18580"

            use expression inner_screen