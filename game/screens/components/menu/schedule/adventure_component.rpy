screen adventure_component:
    grid 2 2:
        spacing 10

        button:
            style "schedule_cmp_button"
            text "무사수행1"
            action SetScreenVariable("componentSelect", "adventure")
