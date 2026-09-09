## 커스텀 action 정의
#
#

init python:
    import random


################################################################################
## 메뉴 관련 클래스와 함수
################################################################################
    ## 메뉴 선택 액션 객체 생성
    ## status, schedule... 등의 버튼을 눌렀을때 선택된 버튼이 Action에 담김
    ## Action을 opion으로 넘겨줌
    ## 앞서 정의해준 menu_btn_options에서 Actoin랑 키 값을 매칭해서 알맞은 value값을 넘겨줌
    ## value에는 이동할 label이 들어있고 renpy.jump()함수로 label로 넘어감
    ## 사용예시: textbutton status action MenuButton("status")
    ## 게임 실행시 파일이 한번에 모두 실행되서(컴파일말고 게임 실행시 스크린 그릴때) 객체는 그때 한번만 생성하는 듯..?
    #
    #
    class MenuButton(Action):
        # 객체가 생성될때 초기화되는 매직 메서드
        def __init__(self, option):
            self.option = option

        # 객체를 함수처럼 호출할수 있게 해주는 매직 메서드
        def __call__(self):
            if self.option in menu_btn_options:
                renpy.store.is_visible_menu = False # 메뉴 버튼 모두 사라지게 하기
                renpy.jump(menu_btn_options[self.option]) # game/label/action_label로 이동
            else:
                return
        
        def get_sensitive(self):
            return self.option in menu_btn_options
    
################################################################################
## 스케줄 핵심 로직 관련 클래스와 함수
################################################################################

    # 스케줄화면 나가거나 스케줄 돌릴때 발생, 스케줄 리스트 싹 비움
    def clearSchedule():
        renpy.store.scheduleList = []

    # 스케줄 넣기를 누르면 발생, option에서 확인하고 아니면 리턴
    class ChooseSchedule(Action):
        # 객체가 생성될때 초기화되는 매직 메서드
        def __init__(self, option):
            self.option = option

        # 객체를 함수처럼 호출할수 있게 해주는 매직 메서드
        def __call__(self):
            # 올바른 옵션인지, 선택이 3보다 작은지 확인
            if (self.option in schedule_options) and (len(scheduleList) < 3):
                renpy.store.scheduleList.append(self.option)
                renpy.restart_interaction()
            else:
                return
        
        def get_sensitive(self):
            return self.option in schedule_options
    
    # 스케줄 제일 마지막에 선택한거 하나만 삭제하기
    class DeleteSchedule(Action):
        def __call__(self):
            if scheduleList:
                scheduleList.pop()
                renpy.restart_interaction()
            else:
                return

    # todo
    # 1. 날짜 계산
    # 2. 성공 실패 계산
    # 3. 스탯 변화량 계산 및 스탯 업데이트
    # 4. 이벤트계산
    #
    # 스케줄 큐 사용해서 1~4번 돌리기
    # 4번에서 검사후 이벤트 있으면 이벤트 큐에 push
    # 이벤트큐에 있는 요소는 스케줄이 한번 pop된 후에 이벤트큐 pop
    # 이벤트 큐 다 pop되면 그 다음에 스케줄 다음거 pop하기
    # 이렇게 만들어진 결과를 result에 저장
    # 이후 유저가 보는 화면에선 이미 만들어진 result를 하나하나 보여줌
    def goSchedule(schedules):
        manager = ScheduleManager(schedules)
        n1 = next(manager)
        n2 = next(manager)
        n3 = next(manager)
        renpy.store.record_schedule_result.append((n1, n2, n3))
        renpy.store.now_schedule_result = (n1, n2, n3)
        # renpy.restart_interaction()
        renpy.show_screen("plain_screen", "print_schedule_screen")
        return

    class ScheduleManager:
        def __init__(self, schedules):
            self.schedules = schedules
            self.__now_schedule = ""
            self.__p = []
            self.result = {
                "time": "",
                "pass_time": "",
                "p_rate": [],
                "status": []
            }

        def __iter__(self):
            return self

        def __next__(self):
            if self.schedules:

                # 초기화
                self.result = {
                    "time": "",
                    "pass_time": "",
                    "p_rate": [],
                    "status": []
                }
                self.p = ""

                self.__now_schedule = self.popleft()
                self.run_phase("before") # 선수이벤트 검사, 확률 검사, 
                self.run_phase("after") # 스케줄 실행, 능력치, 친밀도 검사
                self.run_phase("end") # 이벤트 체크, 시간변화 체크
                return (self.__now_schedule, self.result) # 실행한 스케줄과 그 결과 반환
            else:
                raise StopIteration
        
        def run_phase(self, point):
            if point == "before":
                pass
                #checkEvent()
            elif point == "after":
                self.updateStatus(self.__now_schedule)
            elif point == "end":
                self.passTime()
                #checkEvent()

        def popleft(self):
            if self.schedules:
                return self.schedules.pop(0)
            else:
                return False
        
        # 체력, 근력, 스트레스 지수를 계산해서 성공확률 구하는 함수
        def calc_rate(self, schedule):
            # 스케줄이 rest이면 따로 예외적으로 처리
            is_rest = True if schedule in ["mindset", "reading", "outing"] else False
            
            if is_rest:
                result = "best"

            else:
                hp, morality, stress = renpy.store.player.getRatingProp()
                stand_key = schedule_options[schedule]["stand"]["key"]
                stand_val = schedule_options[schedule]["stand"]["value"]
                player_status = renpy.store.player.status # player.status객체 가져옴
                now_stand_val = getattr(player_status, stand_key)

                # 1. hp*2 < stress 이면 무조건 fail
                # 2. 특정스탯 값이 기준을 못넘으면 normal 또는 good
                # 3. 내 스탯이 특정 기준을 만족할 때 분기
                # 3-1. hp > stress 이면 best
                # 3-2. 아니면 결과는 normal, good, best를 모두 가질수 있음

                #1
                if hp*2 < stress:
                    result = "fail"

                #2
                elif now_stand_val < stand_val: # 스탯 낮을때
                    #확률 normal, good
                    result = random.choice(["normal", "good"])

                #3
                elif stand_val <= now_stand_val:
                    #3-1
                    if hp > stress:
                        result = "best"

                    #3-2
                    elif hp <= stress:
                        # hp 높을수록 rate낮아짐
                        rate = (stress - hp) / hp
                        result = "good" if random.random() < rate else "best"
            
            return result

        def repeat_rateing(self, best, good, normal, mini, maxi, condition):
            if condition:
                now = renpy.random.randint(mini, maxi)
                b = abs(best - now)
                g = abs(good - now)
                n = abs(normal - now)
            else:
                now = renpy.random.randint(maxi, mini) # 랜던 함수 리스트 범위 넘어가는거 수정함
                b = abs(normal - now)
                g = abs(good - now)
                n = abs(best - now)
            return (b, g, n, now)

        def get_rated_var(self, want, minimum, maximum):
            mini = minimum
            maxi = maximum
            best = maxi
            good = ((maxi + mini)/2)
            normal = mini
            condition = True if minimum < maximum else False

            b, g, n, now = self.repeat_rateing(best, good, normal, mini, maxi, condition)

            count = 0
            max_count = 100

            if want == "normal":
                while True:
                    count += 1
                    if max_count <= count:
                        return 0

                    if min(b, g, n) == n:
                        return now
                    else:
                        b, g, n, now = self.repeat_rateing(best, good, normal, mini, maxi, condition)

            elif want == "good":
                while True:
                    count += 1
                    if max_count <= count:
                        return 0

                    if min(b, g, n) == g:
                        return now
                    else:
                        b, g, n, now = self.repeat_rateing(best, good, normal, mini, maxi, condition)
            elif want == "best":
                while True:
                    count += 1
                    if max_count <= count:
                        return 0

                    if min(b, g, n) == b:
                        return now
                    else:
                        b, g, n, now = self.repeat_rateing(best, good, normal, mini, maxi, condition)
            else:
                return 0


        # 증감시킬 스탯의 수치를 정하는 함수
        def p_rate(self, schedule, minimum, maximum): # -> list(int)

            # 만약 최대 최소 같으면 그냥 반환
            if minimum == maximum:
                return [minimum]*7
            else:
                result = [0]*7
                
                for i in range(7):
                    rate = self.calc_rate(schedule) # normal, good, best
                    self.result["p_rate"].append((schedule, rate))
                    self.__p.append(rate)
                    var = self.get_rated_var(rate, minimum, maximum)
                    result[i] = var
                return result
        
        # 수정할 것 한달 21일, 스케줄단위 일주일
        def passTime(self):
            player = renpy.store.player
            year = player.times.current_year
            month = player.times.current_month
            day = player.times.current_day
            self.result["time"] = str(year)+"."+str(month)+"."+str(day)
            if day == 15:
                day = 1
                month += 1
                if month == 12:
                    month = 1
                    year +=1
            else:
                day += 7
            self.result["pass_time"] = str(year)+"."+str(month)+"."+str(day)
            player.times.current_year = year
            player.times.current_month = month
            player.times.current_day = day

        ## 스케줄의 스탯의 확률을 구하고 변경을 돌리는 함수
        # status_dict : dict
        # minimum : int
        # maximum : int
        # var : list 2D
        def updateStatus(self, schedule): # schedule은 schdule옵션
            if schedule == "reading":
                rand_status = random.choice(["intellect", "attraction", "music"])
                self.changeStatus("stress", schedule, [-1]*7)
                self.changeStatus(rand_status, schedule, [1]*7)
            else:
                status_dict = schedule_options[schedule]["status"] # 증감시킬 스테이터스 가져오기
                bound_pass_count = 0
                if status_dict: # 스테이터스 하나하나 돌면서 증감 실행
                    for key, value in status_dict.items():
                        if key == "bond":
                            var = self.p_rate(schedule, minimum, maximum)
                            self.changeStatus(key, schedule, random.choice(var)) # 유대 스탯 7개중 랜덤으로 하나 선택
                        elif key == "recall":
                            self.changeStatus(key, schedule, 1)
                        else:
                            if key == "stress":
                                minimum = value[1]
                                maximum = value[0]
                            else:
                                minimum = value[0] # 증감 최값
                                maximum = value[1] # 증감 최댓값
                            var = self.p_rate(schedule, minimum, maximum) # 확률함수 돌려서 증감된 스탯값 리스트로 받음 (7번 실행)
                            self.changeStatus(key, schedule, var) # 스탯변경 함수 돌리기
            # 카운트하기
            self.scheduleCount(schedule)

        ## 실제로 스탯 증감값이 변경이 적용되는 함수
        # 특정 스탯의 7일치 증감값 반영후 결과를  result에 반영
        # todo
        def changeStatus(self, status, schedule, var):
            player_status = renpy.store.player.status # player.status객체 가져옴
            if isinstance(var, int):
                player_status.addStatus(status, var)
            else:
                for i in var:
                    player_status.addStatus(status, i)

            self.result["status"].append((status, player_status.getStatus(status))) # 결과 기록용
        
        # 스케줄 실행횟수 카운트하고 자동으로 레벨업 시키는 함수
        def scheduleCount(self, schedule):
            key = schedule_options[schedule]["key"]

            # 딕셔너리 키 값이 없을때 예외처리
            if key in player.skill.skill_level.keys():
                now_level = player.skill.skill_level[key]
                now_count = player.skill.skill_count[schedule] + 1
                max_level = player.skill.max_level[key]
                player.skill.skill_count[schedule] = now_count
                if now_count == 10 and now_level < max_level:
                    player.skill.skill_level[key] += 1

    # 스테이터스 변화 액션
    class ChangeStatus(Action):
        def __init__(self, context, status, variate):
            self.context = context
            self.status = status
            self.variate = variate

        def __call__(self):
            p = renpy.store.player.status
            s = self.status
            p.s += self.variate

################################################################################
## 스케쥴 study_component 관련 함수
################################################################################
    # study에서 level에 따라 학습 가능한 스케줄이 다르므로 유동적으로 변하는 ui구현을 위한 함수
    def show_study_schedule_button():
        player_skill_level = player.skill.skill_level
        available_schedule =[]

        for schedule, value in schedule_options.items():
            if schedule in ["mindset", "reading", "outing"]:
                pass
            elif value["level"] == player_skill_level[value["key"]]:
                available_schedule.append(schedule)
        renpy.store.available_study_schedule_list = available_schedule

################################################################################
## outing 관련 함수
################################################################################
    def buyItem(item_name): # item -> str
        player_money = player.profile.money
        item = item_data[item_name]
        item_price = item["price"]

        if player_money >= item_price:

            # 즉시소모 아이템이면 if문 실행
            if item["isConsumable"] and item["category"] == "restaurant": # 음식
                consumRestaurantItem(item)
            else:
                buyItemDetail(item)
        else:
            renpy.store.canBuy = False
            renpy.store.outing_buy_btn_text = "돈이 부족합니다."
            #renpy.restart_interaction()
    
    def consumRestaurantItem(item):
        player = renpy.store.player
        status = item["status"]
        result = []

        for key, value in status.items():
            player.status.addStatus(key, value)
            result.append([key, str(value)])
        
        renpy.store.outing_buy_result_frame = True
        renpy.store.outing_buy_result = result

    def buyItemDetail(item):
        pass