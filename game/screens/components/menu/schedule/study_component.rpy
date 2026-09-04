screen study_component():
    vpgrid:
        cols 2
        spacing 10

        for i in available_study_schedule_list:
            button:
                style "schedule_cmp_button"
                text [schedule_options[i]["title"]]
                if len(scheduleList) < 3:
                    action ChooseSchedule(i)
