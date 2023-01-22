from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from datetime import datetime
def my_job():
  print(f"custom job called at {datetime.now()}")
scheduler = BlockingScheduler()
scheduler.add_job(my_job, 'cron', minute='1', hour='14-15')
# scheduler.add_job(func=my_job, trigger='interval',seconds=2,start_date='13:45:00',end_date = "13:46:00",timezone='Asia/Kolkata')
# # scheduler.add_job(func=my_job, trigger='interval', seconds=2, id='my custom task')
# scheduler.start()
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger

trigger = OrTrigger([CronTrigger(hour='21', minute='15-59/1'),
                     CronTrigger(hour='22', minute='0-15/1')])
scheduler.add_job(my_job, trigger,timezone='Asia/Kolkata')
scheduler.start()
