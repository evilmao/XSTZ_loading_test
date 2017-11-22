#coding:utf-8

__doc__ == '''The Program is used to test the server load press of website--
http://www.xsmcfx.com .
-- Use the multiprocessing module to achieve concurrent operation.
-- According account number create client-connections
-- According return message content,judged whether operation is successful.
'''
import requests
import threading
from datainfo import payload_list,url #导入用户信息
import json 
import time
import tqdm


def InjectionTrade(data):
    try:      
        t1 = time.time()
        r =  requests.post(url, data=data)
        t2= time.time()        
        resp = r.text 
        result = json.loads(resp)

        if result["IsSuccess"] == False: #请求错误
            with open("Injection_error.txt",'a+') as f:
                f.write("The AccountId{0} injected funds failed! usetime--{1}!\n".format(data["Account"],(t2-t1)))
            
        elif result["IsSuccess"] == True: #请求成功
            with open("Injection_success.txt",'a+') as f:
                f.write("The AccountID--{0} injected funds successfully! usetime--{1}!\n".format(data["Account"],(t2-t1)))
            
    except Exception as e:
        with open("Error_log.txt","a+") as f:
            f.write(str(e)+'\n')

    
if __name__ == "__main__":
    threads = [] 
    for data in payload_list:
        my_thread = threading.Thread(target=InjectionTrade,args=(data,))    #使用多线程进行并发操作
        threads.append(my_thread)

    for n in threads:
        n.start()
        
    for n in threads:
        n.join()
        
    print ("finished!")