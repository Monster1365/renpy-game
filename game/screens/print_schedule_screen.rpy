screen print_schedule_screen():
    button:
        align (0.5, 0.5)
        
        # 이중클릭을 막아줌
        action NullAction()

        frame:
            xsize 800
            ysize 700
            padding (20, 20, 20, 20)
            align (0.5, 0.5)
            background "#706ddb"

            vbox:
                for result in now_schedule_result:
                    hbox:
                        text [result[0]]
                        frame:
                            hbox:
                                vbox:
                                    text [result[1]["time"]]
                                    text [result[1]["pass_time"]]
                                    text [result[1]["p_rate"]]
                                vbox:
                                    if result[1]["status"]:
                                        hbox:
                                            for i in result[1]["status"]:
                                                text i[0]
                                                text ":"
                                                text str(i[1])
                                
                                
