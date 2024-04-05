#!/usr/bin/env python3 
#-*- coding: utf-8 -*- 

import subprocess
import schedule
import time

def job():
  subprocess.call(
    ['python', 'aggregate.py']
  )
schedule.every().day.at("15:00").do(job)

while True:
  schedule.run_pending()
  time.sleep(1)
