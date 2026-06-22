## 레이아웃 하단
#
#

screen bottom_layout():
    frame:
        background "#c9ffca"
        yfill True
        xfill True
        ysize BOTTOM_LAYOUT_HEIGHT

        if is_visible_setting_btn:
            use setting_btn_component