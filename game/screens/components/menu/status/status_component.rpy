## status 팝업 컴포넌트
#
#

screen status_component:
    button:
        xalign 1.0
        yalign 0.5
        
        action NullAction()
        
        frame:

            xsize 600
            ysize 450
            background "#706ddb"

            # 'c'는 Center(내용), 'r'은 Right(스크롤바)
            side "c r":
                spacing 5 # 내용과 스크롤바 사이 간격

                # 1. 뷰포트 정의 (반드시 id를 부여해야 함)
                viewport id "my_vp":
                    mousewheel True
                    
                    vbox:
                        spacing 10
                        for i in range(1, 31):
                            text "리스트 항목 [i]" color "#fff"

                # 2. 커스텀 스크롤바 정의
                # value에 YScrollValue("뷰포트ID")를 넣으면 연동됨
                vbar value YScrollValue("my_vp")
