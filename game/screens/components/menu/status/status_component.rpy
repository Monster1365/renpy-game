## status 팝업 컴포넌트
#
#

screen status_component():
    button:
        xalign 1.0
        yalign 0.5
        
        action NullAction()
        
        frame:

            xsize 350
            ysize 500
            
            xpadding 20
            ypadding 20

            background "#706ddb"

            vbox:
                spacing 15
                text "status info"

                vbox:
                    spacing 10

                    $ titleColor = '#fff'

                    grid 2 1:
                        xfill True
                        text "체력:" color titleColor xalign 0.0
                        text "[player.status.hp]" color titleColor xalign 1.0

                    grid 2 1:
                        xfill True
                        text "근력:" color titleColor xalign 0.0
                        text "[player.status.strength]" color titleColor xalign 1.0

                    grid 2 1:
                        xfill True
                        text "매력:  " color titleColor xalign 0.0
                        text "[player.status.attraction]" color titleColor xalign 1.0

                    grid 2 1:
                        xfill True
                        text "도덕성: " color titleColor xalign 0.0
                        text "[player.status.morality]" color titleColor xalign 1.0

                    grid 2 1:
                        xfill True
                        text "지력:  " color titleColor xalign 0.0
                        text "[player.status.intellect]" color titleColor xalign 1.0

                    grid 2 1:
                        xfill True
                        text "스트레스:" color titleColor xalign 0.0
                        text "[player.status.stress]" color titleColor xalign 1.0

                    grid 2 1:
                        xfill True
                        text "사회성: " color titleColor xalign 0.0
                        text "[player.status.sociality]" color titleColor xalign 1.0

                    grid 2 1:
                        xfill True
                        text "예의:  " color titleColor xalign 0.0
                        text "[player.status.attitude]" color titleColor xalign 1.0

