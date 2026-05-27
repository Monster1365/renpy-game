screen itembox(key):
    default item = ITEMS_DB[key]
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