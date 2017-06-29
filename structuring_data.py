#parsing data3 store data################################
import pandas as pd
import os
import time 
from datetime import datetime

path = "/Users/TakahiroSuzuki/Desktop/machinelearning/intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    #print(stock_list)  #df=dataframe
    df = pd.DataFrame(columns = ['Date', 'Unix', 'Ticker', 'De Ratio'])

    for each_dir in stock_list[1:5]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("_KeyStats")[1]
        if len(each_file) > 0 :
           for file in each_file:
               date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
               unix_time = time.mktime(date_stamp.timetuple())
               #print(date_stamp, unix_time)
               full_file_path = each_dir+'/'+file
               #print(full_file_path)
               source = open(full_file_path, 'r').read()
               #print(source)
               try:
                  value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
               #print(ticker+":",value)
                  df = df.append({'Date':date_stamp, 'Unix':unix_time, 'Ticker':ticker, 'De Ratio':value,}, ignore_index = True)
               except Exception as e:
                  pass

           #time.sleep(15)
    save = gather.replace(' ', '').replace(')', '').replace('(','').replace('/', '')+ ('.csv')
    print(save)
    df.to_csv(save)


Key_Stats()


#note 
#1
#The df variable is used to store the creation of a new "DataFrame" object from Pandas, where we specify the columns to be date, unix, ticker, and DE ratio

#2
#The Try here identifies the value as usual, then we're re-defining our DataFrame object as the previous DataFrame object with the new data appended to it

#3
#specifying a custom name for the csv file, then using pandas to_csv capability to output the Data Frame to an actual CSV file
#Running this then saves the dataframe as a CSV spreadsheet for us. We want to save the data since we really just need to access and store the data once