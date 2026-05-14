## schedule 팝업 컴포넌트
#
#

screen schedule_component:
    default nowSelect = ""
    default componentSelect = ""

    # button으로 감싸주는 이유는 plain_screen의 클릭과 중복돼서 현재 창이 닫히는걸 방지하려고
    # 왼쪽 요소
    button:
        align (0.3, 0.5)
        
        # 이중클릭을 막아줌
        action NullAction()

        frame:
            xsize 550
            ysize 700
            padding (20, 20, 20, 20)
            align (0.5, 0.5)
            background "#706ddb"

            vbox:
                spacing 20
                align (0.5, 0.5)

                frame:
                    xsize 500
                    ysize 400
                    background "#aeeae8"

                    vbox:
                        spacing 10

                        if scheduleList:
                            for i in scheduleList:
                                text i
                        else:
                            text "schedule is empty..."

                frame:
                    xsize 500
                    ysize 200
                    background "#aeeae8"
    
    # 오른쪽 요소
    button:
        align (1.0, 0.5)
        
        action NullAction()

        frame:
            xsize 550
            ysize 700
            padding (20, 20)
            background "#706ddb"
            
            # nowSelect가 False값을 가지지 않으면 학습, 알바, 휴식, 무사수행 등을 띄움
            if nowSelect:
                vbox:
                    spacing 30
                    align (0.5, 0.5)

                    # 분기 나눠서 컴포넌트를 화면에 띄움
                    if nowSelect == "study":
                        use study_component
                    elif nowSelect == "work":
                        use work_component
                    elif nowSelect == "rest":
                        use rest_component
                    elif nowSelect == "adventure":
                        use adventure_component

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
                                action [ChooseSchedule("schedule_component: ChooseSchedule()", componentSelect), SetScreenVariable("componentSelect", "")]
                            button:
                                xsize 430
                                ysize 100
                                xpadding 10
                                ypadding 10
                                background "#cac9e5"

                                text "돌아가기"

                                action SetScreenVariable("nowSelect", "")
            
            # nowSelect가 False값이면 선택창 띄움
            else:
                vbox:
                    spacing 10
                    xalign 0.5
                    yalign 0.5

                    button:
                        xsize 500
                        ysize 150
                        background "#aaa9ca"
                        text "학습"
                        action SetScreenVariable("nowSelect", "study")

                    button:
                        xsize 500
                        ysize 150
                        background "#aaa9ca"
                        text "알바"
                        action SetScreenVariable("nowSelect", "work")

                    button:
                        xsize 500
                        ysize 150
                        background "#aaa9ca"
                        text "휴식"
                        action SetScreenVariable("nowSelect", "rest")

                    button:
                        xsize 500
                        ysize 150
                        background "#aaa9ca"
                        text "무사수행"
                        action SetScreenVariable("nowSelect", "adventure")
