screen itembox(key):
    default item = item_data[key]
    default img = ""

    button:
        action NullAction()
        style "itembox"
        
        vbox:
            if img:
                pass
            else:
                text item["title"]

            hbox:
                pass