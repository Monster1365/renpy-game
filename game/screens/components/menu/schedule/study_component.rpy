screen study_component():
    grid 2 2:
        spacing 10

        button:
            xsize 210
            ysize 100
            padding (10, 10, 10, 10)
            background "#cac9e5"

            text "공부방"
            action SetScreenVariable("componentSelect", "studyroom")

        button:
            xsize 210
            ysize 100
            padding (10, 10, 10, 10)
            background "#cac9e5"

            text "아이들과 뛰어놀기"
        
        button:
            xsize 210
            ysize 100
            padding (10, 10, 10, 10)
            background "#cac9e5"

            text "언어교육"
        button:
            xsize 210
            ysize 100
            padding (10, 10, 10, 10)
            background "#cac9e5"

            text "예절교육"
