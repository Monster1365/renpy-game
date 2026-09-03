screen study_component():
    grid 3 2:
        spacing 10

        for i in schedule_options.keys():
            if i in ["mindset", "reading", "outing"]:
                pass
            else:
                button:
                    style "schedule_cmp_button"
                    text [schedule_options[i]["title"]]
                    if len(scheduleList) < 3:
                        action ChooseSchedule(i)
