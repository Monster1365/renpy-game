screen study_component():
    grid 2 2:
        spacing 10

        button:
            style "schedule_cmp_button"
            text "공부방"
            action SetScreenVariable("componentSelect", "studyroom")

        button:
            style "schedule_cmp_button"
            text "아이들과 뛰어놀기"
            action SetScreenVariable("componentSelect", "playwithchild")
        
        button:
            style "schedule_cmp_button"
            text "언어교육"
            action SetScreenVariable("componentSelect", "learnlanguage")

        button:
            style "schedule_cmp_button"
            text "예절교육"
            action SetScreenVariable("componentSelect", "learnattitude")

