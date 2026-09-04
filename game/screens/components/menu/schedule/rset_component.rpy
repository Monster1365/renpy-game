screen rest_component():
    grid 2 2:
        spacing 10

        for i in ["mindset", "reading", "outing"]:
            button:
                style "schedule_cmp_button"
                text [schedule_options[i]["title"]]
                if len(scheduleList) < 3:
                    action ChooseSchedule(i)
