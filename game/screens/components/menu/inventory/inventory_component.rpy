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
                    use belongings_component
                                    
                elif inventory_options == "clothes":
                    use clothes_component
                    
                elif inventory_options == "books":
                    use books_component

            # vpgrid:
            #     cols 4 # 열의 개수 고정, 행은 아이템 수에 따라 자동 생성
            #     spacing 10
            #     draggable True
            #     mousewheel True
            #     scrollbars "vertical"

            #     for i in range(100): # 100개의 아이템
            #         textbutton "아이템 [i]" action NullAction()