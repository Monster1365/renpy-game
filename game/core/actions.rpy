## 커스텀 action 정의
#
#

init python:
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
## 스케줄 관련 클래스와 함수
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
        renpy.restart_interaction()
        return

    # todo
    class ScheduleManager:
        def __init__(self, schedules):
            self.schedules = schedules
            self.__now_schedule = ""
            self.__p = ""
            self.result = {
                "time": "",
                "pass_time": "",
                "is_sucess": "",
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
                    "is_sucess": "",
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
                self.p_rate(self.__now_schedule)
                #checkEvent()
            elif point == "after":
                self.updateStatus(self.__now_schedule, self.__p)
            elif point == "end":
                self.passTime()
                #checkEvent()

        def popleft(self):
            if self.schedules:
                return self.schedules.pop(0)
            else:
                return False
        
        def p_rate(self, schedule):
            if renpy.store.ENV == "development":
                self.result["is_success"] = "success"
                self.__p = "success"
            else:
                self.result["is_success"] = "success"
                self.__p = "success"
                pass
        
        def passTime(self):
            player = renpy.store.player
            year = player.times.current_year
            month = player.times.current_month
            day = player.times.current_day
            self.result["time"] = str(year)+"."+str(month)+"."+str(day)
            if day == 31:
                day = 11
                month += 1
                if month == 12:
                    month = 1
                    year +=1
            else:
                day += 10
            self.result["pass_time"] = str(year)+"."+str(month)+"."+str(day)
            player.times.current_year = year
            player.times.current_month = month
            player.times.current_day = day

        def updateStatus(self, schedule, p):
            player_status = renpy.store.player.status
            if p == "success":
                status_list = schedule_options[schedule]["status"]["success"]
                for status, var in status_list:
                    getstatus = getattr(player_status, status) + var
                    self.result["status"].append((status, getstatus))
                    setattr(player_status, status, getstatus)
            elif p == "fail":
                status_list = schedule_options[schedule]["status"]["fail"]
                for status, var in status_list:
                    self.result["status"].append([status, var])
                    getstatus = getattr(player_status, status) + var
                    self.result["status"].append((status, getstatus))
                    setattr(player_status, status, getstatus)










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

## 나중에 구현 할 것
## 액션 예시
#     class MyAction(Action):
#         def __init__(self, label_name):
#             self.label_name = label_name

#         def __call__(self):
#             renpy.jump(self.label_name)



## 아이템 선택
#     class SelectItem(Action):
#         def __init__(self, item):
#             self.item = item

#         def __call__(self):
#             store.selected_item = self.item

#         def get_selected(self):
#             return store.selected_item == self.item



## 스탯 변경
#     class AddStat(Action):
#         def __init__(self, stat, amount):
#             self.stat = stat
#             self.amount = amount

#         def __call__(self):
#             setattr(store, self.stat, getattr(store, self.stat) + self.amount)

