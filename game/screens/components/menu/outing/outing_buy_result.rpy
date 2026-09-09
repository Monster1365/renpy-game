screen outing_buy_result:
    button:
        align (0.5, 0.8)
        action NullAction()

        frame:
            style "outing_buy_result_frame"

            vbox:
                ysize 200
                spacing 3

                for i in outing_buy_result:
                    frame:
                        xsize 500
                        ysize 50
                        hbox:
                            spacing 10
                            text i[0]
                            text "="
                            text i[1]