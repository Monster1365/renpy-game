## schedule 팝업 컴포넌트
#
#

screen schedule_component:
    default nowSelect = "test"
    default scheduleList = []

    button:
        xalign 0.3
        yalign 0.5
        
        action NullAction()

        frame:
            xsize 550
            ysize 700
            
            xpadding 20
            ypadding 20

            background "#706ddb"
            vbox:
                spacing 20
                # 이건 왼쪽 프레임
                frame:
                    xsize 350
                    ysize 400

                    background "#aeeae8"

                    vbox:
                        spacing 10
                        text "schedule is empty..."
                        if scheduleList:
                            for i in scheduleList:
                                pass
                frame:
                    xsize 350
                    ysize 200

                    background "#aeeae8"
    
    button:
        xalign 1.0
        yalign 0.5
        
        action NullAction()

        frame:
            xsize 550
            ysize 700
            xpadding 20
            ypadding 20
            background "#706ddb"

            # 스케줄 눌렀을때 오른쪽에 표시되는 요소들
            # 만약 else로 분기하면 가장 기본 화면을 띄움
            #
            # 학습
            if nowSelect == "study":
                vbox:
                    spacing 30
                    xalign 0.5
                    yalign 0.5
                    
                    grid 2 2:
                        spacing 10

                        button:
                            xsize 210
                            ysize 100
                            xpadding 10
                            ypadding 10
                            background "#cac9e5"

                            text "공부방"

                        button:
                            xsize 210
                            ysize 100
                            xpadding 10
                            ypadding 10
                            background "#cac9e5"

                            text "아이들과 뛰어놀기"
                        
                        button:
                            xsize 210
                            ysize 100
                            xpadding 10
                            ypadding 10
                            background "#cac9e5"

                            text "언어교육"
                        button:
                            xsize 210
                            ysize 100
                            xpadding 10
                            ypadding 10
                            background "#cac9e5"

                            text "예절교육"

                    frame:
                        xsize 430
                        ysize 250
                        ypadding 10
                        background "#696880"

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 10

                            button:
                                xsize 430
                                ysize 100
                                xpadding 10
                                ypadding 10
                                background "#cac9e5"

                                text "스케줄 넣기"
                            button:
                                xsize 430
                                ysize 100
                                xpadding 10
                                ypadding 10
                                background "#cac9e5"

                                text "돌아가기"

            elif nowSelect == "work":
                vbox:
                    spacing 30
                    xalign 0.5
                    yalign 0.5
                    
                    grid 2 2:
                        spacing 10

                        button:
                            xsize 210
                            ysize 100
                            xpadding 10
                            ypadding 10
                            background "#cac9e5"

                            text "공부방"

                        button:
                            xsize 210
                            ysize 100
                            xpadding 10
                            ypadding 10
                            background "#cac9e5"

                            text "아이들과 뛰어놀기"
                        
                        button:
                            xsize 210
                            ysize 100
                            xpadding 10
                            ypadding 10
                            background "#cac9e5"

                            text "언어교육"
                        button:
                            xsize 210
                            ysize 100
                            xpadding 10
                            ypadding 10
                            background "#cac9e5"

                            text "예절교육"

                    frame:
                        xsize 430
                        ysize 250
                        ypadding 10
                        background "#696880"

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 10

                            button:
                                xsize 430
                                ysize 100
                                xpadding 10
                                ypadding 10
                                background "#cac9e5"

                                text "스케줄 넣기"
                            button:
                                xsize 430
                                ysize 100
                                xpadding 10
                                ypadding 10
                                background "#cac9e5"

                                text "돌아가기"
            else:
                vbox:
                    frame:
                        xsize 500
                        ysize 200
                        background "#aaa9ca"

                        textbutton "[nowSelect]" action SetScreenVariable("nowSelect", "study")

label study_btn_label:
    call screen plain_screen(inner_screen="study_screen")

screen study_screen():
    button:
        xalign 1.0
        yalign 0.5
        
        action NullAction()

        frame:
            xsize 550
            ysize 700
            
            xpadding 20
            ypadding 20

            background "#74db6d"