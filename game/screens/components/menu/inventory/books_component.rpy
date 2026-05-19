screen books_component:
    frame:
        xsize 600 ysize 400
        
        # vpgrid는 행(rows)이나 열(cols) 하나만 지정하면 개수가 모자라도 에러가 안 납니다.
        vpgrid:
            cols 5
            spacing 10
            mousewheel True
            draggable True
            scrollbars "vertical"

            for i in belonging_items:
                if i.quantity > 0:
                    use itembox(i.serial)
