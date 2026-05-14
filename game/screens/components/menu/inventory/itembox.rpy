screen itembox(serial):
    default item = items[serial]
    default img = ""

    button:
        action NullAction()
        style "itembox"
        
        vbox:
            if img:
                pass
            else:
                text item.title

            hbox:
                pass