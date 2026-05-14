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

            # 테스트를 위해 아이템 10개를 반복 생성
            for i in range(10):
                textbutton "아이템 [i]":
                    xsize 100 ysize 100
                    action NullAction()
