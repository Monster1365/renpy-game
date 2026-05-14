screen work_component():
    grid 2 3:
        spacing 10

        button:
            style "schedule_cmp_button"
            text "집안일"
            action SetScreenVariable("componentSelect", "housework")

        button:
            style "schedule_cmp_button"
            text "과외"
            action SetScreenVariable("componentSelect", "lesson")
        
        button:
            style "schedule_cmp_button"
            text "병원봉사"
            action SetScreenVariable("componentSelect", "hospitalwork")

        button:
            style "schedule_cmp_button"
            text "옷가게"
            action SetScreenVariable("componentSelect", "clotheswork")

        button:
            style "schedule_cmp_button"
            text "농장일"
            action SetScreenVariable("componentSelect", "farmwork")


        