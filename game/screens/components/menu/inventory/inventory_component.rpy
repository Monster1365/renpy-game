## inventory 팝업 컴포넌트
#
#

screen inventory_component:
    default inventory_options = "belongings"

    button:
        xalign 1.0
        yalign 0.5
        
        action NullAction()
        
        frame:

            xsize 600
            ysize 450
            background "#706ddb"

            vbox:
                # 카테고리 탭 (hbox)
                hbox:
                    spacing 10
                    xalign 0.5
                    textbutton "Belongings" action SetScreenVariable("inventory_options", "belongings")
                    textbutton "Clothes" action SetScreenVariable("inventory_options", "clothes")
                    textbutton "Books" action SetScreenVariable("inventory_options", "books")

                # 2. 조건에 따른 내용 표시
                if inventory_options == "belongings":
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
                                    
                elif inventory_options == "clothes":
                    text "옷장 카테고리입니다." xalign 0.5
                    
                elif inventory_options == "books":
                    text "책장 카테고리입니다." xalign 0.5

            # vpgrid:
            #     cols 4 # 열의 개수 고정, 행은 아이템 수에 따라 자동 생성
            #     spacing 10
            #     draggable True
            #     mousewheel True
            #     scrollbars "vertical"

            #     for i in range(100): # 100개의 아이템
            #         textbutton "아이템 [i]" action NullAction()