## 레이아웃 중간
#
#

screen middle_layout():
    frame:
        background "#ffd5d5"
        yfill True
        xfill True
        ysize MIDDLE_LAYOUT_HEIGHT

        if is_visible_menu:
            use menu_component