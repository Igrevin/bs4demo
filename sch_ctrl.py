import schedule
import time

def task1():
    print("hello")

job1 = schedule.every(10).seconds.do(task1)
job2 = schedule.every(20).seconds.do(task1)

while True:
    schedule.run_pending()
    print(f"job pool 任務數量為：{len(schedule.get_jobs())}")
    if len(schedule.get_jobs()) == 0:
        print("可以下班啦！")
        break

    schedule.clear()
    time.sleep(1)
    
print("歐挖打")
