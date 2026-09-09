## 아무 배경이나 누르면 닫히는 스크린
## Show("plain_screen", inner_frame="test_cmp")로 호출가능
## inner_frame에는 plain_screen위에 뛰울 팝업UI의 스크린 이름을 넣어주면 됌
#
#

screen plain_screen(inner_screen):

    button:
        if inner_screen == "schedule_component" and scheduleSelect:
            action SetScreenVariable("scheduleSelect", "")

        elif inner_screen == "schedule_component":
            action [
                Function(clearSchedule),
                Hide(inner_screen),
                Hide("plain_screen"),
                Return()
            ]

        elif inner_screen == "outing_component" and outingSelect and not outingItemSelect:
            action SetVariable("outingSelect", "")
        
        elif inner_screen == "outing_component" and outingItemSelect and outing_buy_result_frame:
            action [SetVariable("outing_buy_result_frame", False), Hide("outing_buy_result")]
        
        elif inner_screen == "outing_component" and outingItemSelect and not canBuy:
            action [SetVariable("canBuy", True), Hide("outing_buy_btn")]
        
        elif inner_screen == "outing_component" and outingItemSelect:
            action [SetVariable("outingItemSelect", ""), Hide("outing_buy_btn")]

        else:
            action [
                Hide(inner_screen),
                Hide("plain_screen"),
                Return()
            ]

        frame:
            xfill True
            yfill True
            background "#45c18580"

            use expression inner_screen
