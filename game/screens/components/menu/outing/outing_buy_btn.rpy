screen outing_buy_btn(item):
    button:
        align (0.9, 0.8)
        action NullAction()

        frame:
            style "outing_buy_frame"

            vbox:
                align (0.5, 0.5)
                spacing 10
                text [outing_buy_btn_text]
                button:
                    xsize 100
                    ysize 80
                    align (0.5, 0.5)

                    if canBuy:
                        text "구매"
                        background "#4de342"

                        action [Function(buyItem, item), Show("outing_buy_result")]

                    else:
                        text "구매불가"
                        background "#e34742"

                        action [Function(buyItem, item)]
