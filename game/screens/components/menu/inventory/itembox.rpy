screen itembox(serial):
    default item = items[serial]

    button:
        action NullAction()
        style_prefix "item"
        xsize 100
        ysize 100
        
        vbox:
            frame:
                text item.title

            hbox:
                pass