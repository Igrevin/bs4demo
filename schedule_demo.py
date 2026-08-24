import time
import schedule
from datetime import datetime

def task1():
    print(f"任務1 完成時間：{datetime.now()}")

def task2():
    print(f"任務2 完成時間：{datetime.now()}")

schedule.every(2).seconds.do(task1)
schedule.every(4).seconds.do(task2)
print("排程開始")

while True:
    schedule.run_pending()
    time.sleep(1)
print("程式結束")



