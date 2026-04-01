screen time_stamp():
    frame:
        hbox:
            textbutton "[player.times.current_year] /" style "test" action Show("plain_screen", inner_screen="test_cmp")
            text "[player.times.current_month]  /"
            text "[player.times.current_day]  /"

style test:
    # 텍스트 스타일
    # font "NanumGothic.ttf"
    # size 30
    # color "#ffffff"
    # bold True
    # italic True
    # outlines [(2, "#000", 0, 0)]

    # 레이아웃/박스
    # spacing 1스
    # xalign 0.5
    # yalign 0.5

    color "#d87f7f"
    size 30