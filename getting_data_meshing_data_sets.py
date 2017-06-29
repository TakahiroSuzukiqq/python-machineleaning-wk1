import pandas as pd
import os
import time 
from datetime import datetime

path = "/Users/TakahiroSuzuki/Desktop/machinelearning/intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    #print(stock_list)  #df=dataframe
    df = pd.DataFrame(columns = ['Date', 'Unix', 'Ticker', 'DE Ratio', 'Price', 'SP500'])

    #read the data file 
    sp500_df = pd.DataFrame.from_csv("YAHOO-INDEX_GSPC.csv")

    for each_dir in stock_list[1:25]:
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
  
                  try: 
                      sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                      row = sp500_df[(sp500_df.index == sp500_date)]
                      sp500_value = float(row["Adj Close"])
                  except:  #259200 = 259200 seconds for 3days 
                      sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                      row = sp500_df[(sp500_df.index == sp500_date)]
                      sp500_value = float(row["Adj Close"])
 
                                                       #ここから 1=左　　　　　　　　ここまで 0=右
                  stock_price = float(source.split('</small><big><b>')[1].split('</b></big>')[0])
                  #print("stock_price:",stock_price,"ticker:",ticker)

               #print(ticker+":",value)   
                  df = df.append({'Date':date_stamp, 
                             'Unix':unix_time, 
                             'Ticker':ticker, 
                             'DE Ratio':value,
                             'Price':stock_price,
                             'SP500':sp500_value}, ignore_index = True)
               except Exception as e:
                  pass

           #time.sleep(15)
    save = gather.replace(' ', '').replace(')', '').replace('(','').replace('/', '') + ('.csv')
    print(save)
    df.to_csv(save)


Key_Stats()

#now i can compare the percentage change btwn the price and sp500 index.
