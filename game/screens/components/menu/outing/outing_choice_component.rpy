screen outing_choice_component(select):
    button:
        align (0.05, 0.9)
        action NullAction()

        frame:
            style "outing_choice_cmp_frame"

            if outing_options[select]["category"] == "general_store":
                vpgrid:
                    cols 3
                    spacing 10
                    xalign 0.5

                    for key, value in item_data.items():
                        if value["category"] == outing_options[select]["category"]:
                            button:
                                style "outing_choice_cmp_button"
                                text [value["title"]]
                                # action [SetVariable("outingSelect", ""), Return()]
                                action [SetVariable("outingItemSelect", key), Hide("outing_component"), Show("outing_buy_btn", item=key)]
            elif outing_options[select]["category"] == "restaurant":
                vpgrid:
                    cols 2
                    spacing 10
                    xalign 0.5

                    for key, value in item_data.items():
                        if value["category"] == outing_options[select]["category"]:
                            button:
                                style "outing_choice_cmp_button"
                                text [value["title"]]
                                # action [SetVariable("outingSelect", ""), Return()]
                                action [SetVariable("outingItemSelect", key), Hide("outing_component"), Show("outing_buy_btn", item=key)]
            else:
                button:
                    align (0.5, 0.5)
                    xsize 200
                    ysize 100
                    background "#ceb1fc"
                    
                    text "test"
                    action [
                        SetVariable("outingSelect", ""),
                        Hide("outing_component"),
                        Hide("plain_screen"),
                        Hide("main_screen"),
                        SetVariable("is_visible_menu", True),
                        Jump("adventure_label")
                    ]