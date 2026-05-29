## outing 팝업 컴포넌트
#
#

screen outing_component:
    button:
        align(0.05, 0.1)
        action NullAction()

        frame:
            xsize 600
            ysize 500
            background "#db6dd4"

    if outingSelect == "outing1":
        use outing_choice_component("outing1")

    elif outingSelect == "outing2":
        use outing_choice_component("outing2")

    elif outingSelect == "outing3":
        use outing_choice_component("outing3")

    elif outingSelect == "outing4":
        use outing_choice_component("outing4")

    else:
        button:
            align (1.0, 0.7)
            action NullAction()

            frame:
                xsize 550
                ysize 300
                padding (20, 20)
                background "#706ddb"
            
                grid 2 2:
                    spacing 10
                    align (0.5, 0.5)

                    for key, value in outing_options.items():
                        button:
                            style "outing_cmp_button"
                            text [value["title"]]
                            action SetVariable("outingSelect", key)
    
            
            