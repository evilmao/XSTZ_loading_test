#coding:utf-8

__doc__ == '''The Program is used to test the server load press of website--
http://www.xsmcfx.com .
-- Use the multiprocessing module to achieve concurrent operation.
-- According account number create client-connections
-- According return message content,judged whether operation is successful.
'''
import requests
import threading
import threadpool
from datainfo import payload_list,url #导入用户信息
import json 
import time
#import tqdm


def InjectionTrade(data):
    try:
        t1 = time.time()
        r =  requests.post(url,data=data)
        t2= time.time()
        resp = r.text 
        result = json.loads(resp)

        if result["IsSuccess"] == False:
            with open("Injection_error.txt",'a+') as f:
                f.write("The AccountId{0} injected funds failed! usetime--{1}!\n".format(data["Account"],(t2-t1)))
                            
        elif result["IsSuccess"] == True:
            print (result)
            with open("Injection_success.txt",'a+') as f:
                f.write("The AccountID--{0} injected funds successfully! usetime--{1}!\n".format(data["Account"],(t2-t1)))
            
    except Exception as e:
        with open("Error_log.txt","a+") as f:
            f.write(str(e)+'\n')

    
if __name__ == "__main__":        
    pool = threadpool.ThreadPool(500) #线程池,最大允许并行数
    s = threadpool.makeRequests(InjectionTrade,payload_list)
    [pool.putRequest(req) for req in s] 
    pool.wait() 
       
    print ("finished!")