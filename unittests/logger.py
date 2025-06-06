#!/usr/bin/env python
"""
module with functions to enable logging
"""

import time,os,re,csv,sys,uuid,joblib
from datetime import date

if not os.path.exists(os.path.join(".","logs")):
    os.mkdir("logs")

def update_train_log(tag,period,rmse,runtime,MODEL_VERSION,MODEL_VERSION_NOTE,test=False):
    """
    update train log file
    """

    ## name the logfile using something that cycles with date (day, month, year)    
    today = date.today()
    if test:
        logfile = os.path.join("logs","train-test.log")
    else:
        logfile = os.path.join("logs","train-{}-{}.log".format(today.year, today.month))
        
    ## write the data to a csv file    
    header = ['unique_id','timestamp','tag','period','rmse','model_version',
              'model_version_note','runtime']
    write_header = False
    if not os.path.exists(logfile):
        write_header = True
    with open(logfile,'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if write_header:
            writer.writerow(header)

        to_write = map(str,[uuid.uuid4(),time.time(),tag,period,rmse,
                            MODEL_VERSION,MODEL_VERSION_NOTE,runtime])
        writer.writerow(to_write)

def update_predict_log(country, y_pred,y_proba,target_date,runtime,MODEL_VERSION,test=False):
    """
    update predict log file
    """

    ## name the logfile using something that cycles with date (day, month, year)    
    today = date.today()
    if test:
        logfile = os.path.join("logs","predict-test.log")
    else:
        logfile = os.path.join("logs","predict-{}-{}.log".format(today.year, today.month))
        
    ## write the data to a csv file    
    header = ['unique_id','timestamp','country', 'y_pred','y_proba','target_date','model_version','runtime']
    write_header = False
    if not os.path.exists(logfile):
        write_header = True
    with open(logfile,'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if write_header:
            writer.writerow(header)

        to_write = map(str,[uuid.uuid4(),time.time(),country,y_pred,y_proba,target_date,
                            MODEL_VERSION,runtime])
        writer.writerow(to_write)

if __name__ == "__main__":

    from model import MODEL_VERSION, MODEL_VERSION_NOTE
   
 
    update_train_log('united_kingdom', ('2017-12-01', '2018-12-01'), {'rmse':0.5}, "00:00:01",
                         0.1, "test model", test=True)


    update_predict_log('united_kingdom', [0], [0.6,0.4], '2018-12-01',"00:00:02", 0.1, test=True)
    
        
