screen menu_component:
    vbox:
        xalign 0.0
        yalign 0.5

        frame:
            xsize 200
            ysize 400
            padding (10, 10, 10, 10)
            background "#706ddb"

            has vbox

            use menu_btn_component("status")
            use menu_btn_component("schedule")
            use menu_btn_component("inventory")
            use menu_btn_component("outing")