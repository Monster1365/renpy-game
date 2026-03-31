## 아무 배경이나 누르면 닫히는 스크린
#
#

screen plain_screen():
    button:
        action Hide("plain_screen")

        frame:
            xfill True
            yfill False

            background "#45c185"