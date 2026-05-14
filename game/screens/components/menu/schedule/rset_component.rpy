screen rest_component():
    grid 2 2:
        spacing 10

        button:
            style "schedule_cmp_button"
            text "마음수양"
            action SetScreenVariable("componentSelect", "mindset")

        button:
            style "schedule_cmp_button"
            text "외출"
            action SetScreenVariable("componentSelect", "outing")
