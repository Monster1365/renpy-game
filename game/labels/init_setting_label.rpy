## 게임 시작시 띄우는 화면 제어 레이블
#
# 1. 오프닝 띄우기
# 2. 이름 정하기
# 3. 생일 정하기
#
label opening_label:
    system "opening"
    call screen opening_screen

    return

label select_name_label:
    system "select name"
    call screen select_name_screen

    $ player.profile.name = _return

    return

label selet_birthday_label:
    system "select birthday"
    call screen selet_birthday_screen
    return

label init_setting_label:

    # 인게임 오프닝
    call opening_label

    # 이름 정하기
    $ player_name = renpy.input("당신의 이름은 무엇인가요?", default="name")
    $ player_name = player_name.strip()
    call screen select_name_screen(player_name)

    # 생일 정하기
    call screen selet_birthday_screen


    # main.rpy에 있는 start로 돌아가서 나머지 일 수행
    return