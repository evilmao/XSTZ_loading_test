#coding:utf-8

__doc__ == '''The Program is used to test the server load press of website--
http://www.xsmcfx.com .
-- Use the threading module to achieve concurrent operation.
t-- According account number create client-connections
-- According return message content,judged whether operation is successful.
'''
import requests
import multiprocessing
from datainfo import payload_list,url #导入用户信息
import json 
import time
import tqdm


def InjectionTrade(data):
    try:    
        t1 = time.time()
        r =  requests.post(url, data=data ,timeout=1) #客户端发送参数，设置超时时间1s
        t2= time.time()
        resp = r.text   #接收服务器返回数据
        result = json.loads(resp)
        
        if result["IsSuccess"] == False: 
            with open("Injection_error.txt",'a+') as f:
                f.write("The AccountId{0} injected funds failed! usetime--{1}!\n".format(data["Account"],(t2-t1)))
            
        elif result["IsSuccess"] == True:
            with open("Injection_success.txt",'a+') as f:
                f.write("The AccountID--{0} injected funds successfully! usetime--{1}!\n".format(data["Account"],(t2-t1)))
                 
            
    except Exception as e:
        with open("Error_log.txt","a+") as f:
            f.write(str(e)+'\n')

    
if __name__ == "__main__": 
    pool = multiprocessing.Pool(processes=4)#多进程，设置进程池，同时4个进程运行
    datalist = payload_list
 
    for data in datalist:
        pool.apply_async(InjectionTrade, (data,)) #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去   
    print ('Waiting for all subprocesses done...')

    pool.close()#关闭执行完毕的进程
    pool.join() #加入新的进程
    
    print ("finished!")