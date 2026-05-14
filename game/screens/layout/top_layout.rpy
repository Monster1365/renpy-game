## 레이아웃 상단
#
#

screen top_layout():
    frame:
        background "#d9dcff"
        yfill True
        xfill True
        ysize TOP_LAYOUT_HEIGHT

        hbox:
            spacing 20
            use time_stamp_component
            use show_money_component
            use show_profile_component