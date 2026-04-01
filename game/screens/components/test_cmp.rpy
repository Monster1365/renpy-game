## 테스트 팝업 컴포넌트
#
#


screen test_cmp:
    button: ##팝업 화면 내 버튼 클릭으로 plain_screen닫히는거 방지(클릭이 plain_screen으로 넘어가지 않게 방지)
        action NullAction()

        frame:
            xsize 200
            ysize 200

            text "inner_screen의 frame입니다."

            background "#706ddb"