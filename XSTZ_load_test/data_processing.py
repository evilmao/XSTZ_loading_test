#coding:utf-8

__doc__ == '''
-- this function is used to show the result of load test!
'''

from InjectionTrade_Influxdb import db, InjectionTrade,main
from datainfo import payload_list

def showDatas(client):
    
    result1 = client.query('select count(Status) from InjectionFunds group by Status') #collect the  total number of requests
    if (result1.items()):
        count1 = ((result1.items()[0][1]))
        for i in count1:
            data1 = i["count"]
                
    result2 = client.query('select count(Status) from InjectionFunds where Status=true') # collect the number of request successfully!        
    if (result2.items()):
        count2  = ((result2.items()[0][1]))
        for i in count2:
            data2 = i["count"]
    
    success_rate = '%.3f%%' % ((data2/data1)*100)  #Calculate the success_rate
    
    result3 = client.query('select MEAN(ResponseTime) from InjectionFunds where Status=true')
    time = ((result3.items()[0][1]))
    for t in time:
        ResponseTime = '%.3f'% (t["mean"])
    print ("Test Result:")
    print(" "*12, "-"*23)   
    print (" "*12,"| 并发请求数：{}    |".format(len(payload_list)))     
    print (" "*12,"| 成功率:{}!     |".format(success_rate))
    print (" "*12,"| 平均响应时间:{}S |".format(ResponseTime))
    print(" "*12, "-"*23)   


#程序调用入口        
if __name__ == "__main__":   
    main()
    client = db() 
    showDatas(client)