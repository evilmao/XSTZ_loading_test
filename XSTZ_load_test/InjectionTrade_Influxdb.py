#coding:utf-8

__doc__ == '''The Program is used to test the server load press of website--
http://www.xsmcfx.com .
-- Use the threading module to achieve concurrent operation.
-- According account number create client-connections
-- According return message content,judged whether operation is successful.
'''
import requests
import threading
import json 
import time
import tqdm
from influxdb import InfluxDBClient #导入influx数据库客户端
from datainfo import payload_list,url
from influxdb import exceptions


dbinfo = ('192.168.0.187','8086', '', '', 'XSTZ_Injection' )#连接数据库

#connected Influxdb               
def db():    
    #异常判断
    try:
        client = InfluxDBClient(*dbinfo) #创建client操作数据库对象        
        return client                    #返回数据库连接对象                
    except Exception as e:
        raise e

def InjectionTrade(data):
    client = db()   
    try:    
        t1 = time.time()
        r =  requests.post(url, data=data)
        #xlock.acquire() 
        t2= time.time()
        resp = r.text 
        result = json.loads(resp) #json处理返回的数据

        #连接influxdb数据库发送参数。 
        json_body = [
                        {
                        "measurement": "InjectionFunds",
                        "fields": {
                                    "Status":result["IsSuccess"],
                                    "ResponseTime":float('%.3f'%(float(t2-t1))),
                                    "Account_ID":data["Account"]
                                  }
                        }
                     ]      

        try:
            client.write_points(json_body)
            print ("One piece database was inserted to influxdb!") 
            #Xlock.release()        
        except exceptions.InfluxDBClientError as e:
            print (str(e))            
                      
    except Exception as e:
        with open("Error_log.txt","a+") as f:
            f.write(str(e)+'\n')
                        

def main(): 
    '''
    Before testing,initial the table of database.
    '''     
    client = db()
    client.query('drop  measurement InjectionFunds')
    
    threads = [] 
    xlock = threading.Lock()

    for i in payload_list:
        my_thread = threading.Thread(target=InjectionTrade,args=(i,) )
        threads.append(my_thread)
        
    for n in threads:
        n.start()
            
    for n in threads:
        n.join()
            
    print ("finished!")



if __name__ == "__main__": 
    main()


    