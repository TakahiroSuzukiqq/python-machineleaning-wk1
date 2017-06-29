#parsing data1################################
# import pandas as pd
# import os
# import time 
# from datetime import datetime

# path = "/Users/TakahiroSuzuki/Desktop/machinelearning/intraQuarter"

# def Key_Stats(gather="Total Debt/Equity (mrq)"):
#     statspath = path+'/_KeyStats'
#     stock_list = [x[0] for x in os.walk(statspath)]
#     #print(stock_list)

#     for each_dir in stock_list[1:]:
#         each_file = os.listdir(each_dir)
#         # print(each_file)
#         # time.sleep(15)
#         if len(each_file) > 0 :
#            for file in each_file:

#                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
#                unix_time = time.mktime(date_stamp.timetuple())
#                print(date_stamp, unix_time)
#                time.sleep(15)
# Key_Stats()

#parsing data2 pass data################################
import pandas as pd
import os
import time 
from datetime import datetime

path = "/Users/TakahiroSuzuki/Desktop/machinelearning/intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    #print(stock_list)

    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("_KeyStats")[1]
        if len(each_file) > 0 :
           for file in each_file:
               date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
               unix_time = time.mktime(date_stamp.timetuple())
               #print(date_stamp, unix_time)
               full_file_path = each_dir+'/'+file
               print(full_file_path)
               source = open(full_file_path, 'r').read()
               #print(source)
               value = source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
               print(ticker+":",value)



           time.sleep(15)



Key_Stats()