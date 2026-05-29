screen outing_choice_component(select):
    button:
        align (0.05, 0.9)
        action NullAction()

        frame:
            style "outing_choice_cmp_frame"

            vpgrid:
                cols 2
                spacing 10
                xalign 0.5

                for key, value in outing_options[select]["choice"].items():
                    button:
                        style "outing_choice_cmp_button"
                        text [value]
                        action [SetVariable("outingSelect", ""), Return(key)]