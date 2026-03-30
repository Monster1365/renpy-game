## 게임 실행시 가장 먼저 동작되야할 파일
# game_loop 실행, 스크린 띄우기, 기본 변수 초기화


# 게임에서 사용할 캐릭터를 정의합니다.
define system = Character('system', color="#c8ffc8")


# 여기에서부터 게임이 시작합니다.
label start:

    system "대충 스토리가 나옴"

    system "game/core/game_loop.rpy - main_loop 이동"

    transform full_bg:
        size (1920, 1080)

    scene background at full_bg

    jump main_loop
