default camera_x = ui.adjustment()
default camera_y = ui.adjustment()

transform map_zoom:
    zoom 5.0

screen viewport_example():
    button:
        action [Show("main_screen"), Return()]

        viewport id "vp":
            xysize (X_FULL, Y_FULL)
            draggable False
            arrowkeys True

            xadjustment camera_x
            yadjustment camera_y

            add "assets/images/washington.jpg" at map_zoom
