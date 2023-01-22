import yfinance as yf
import pandas as pd
import time
import os
import sys
import json
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from logger import logging
from exception import SensorException
from utils.client import client,DATABASE_NAME,COLLECTION_NAME,STOCK_NAME
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler

class Scheduling:
    def __init__(self):...
    def get_stock_data(self):
        try:
            self.icic_stock = yf.Ticker(STOCK_NAME)
            logging.info("Fetching ICICI bank ctock data from yahoo finace api... ")
            self.stock_df = self.icic_stock.history(start='2023-01-19',interval='1m')
            time.sleep(1)
            self.stock_df.index = self.stock_df.index.astype(str)
            logging.info("Preprocessing the dataframe")
            self.stock_df['DateTime'] = self.stock_df.index
            self.list_dict_data = list(self.stock_df.T.to_dict().values())
            logging.info("Insert the records to monogodb")
            client[DATABASE_NAME][COLLECTION_NAME].insert_many(self.list_dict_data)
        except Exception as e:
            raise SensorException(e,sys)
    def scheduling(self):
        try:
            self.scheduler = BlockingScheduler()
            logging.info("Creating BlockingScheduler object scheduler")
            trigger = OrTrigger([CronTrigger(hour='11', minute='15-59/15'),
                                 CronTrigger(hour='12-13', minute='0-59/15'),
                                 CronTrigger(hour='14', minute='0-15/15')])
            self.scheduler.add_job(self.get_stock_data, trigger, timezone='Asia/Kolkata')
            logging.info("Start Scheduling")
            self.scheduler.start()
        except Exception as e:
            raise SensorException(e,sys)
Obj1 = Scheduling()
Obj1.scheduling()