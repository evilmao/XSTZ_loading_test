---

---

## XSTZ_load_test

用来测试鑫圣投资平台注资行为的压力脚本.

##Requiretments

Running Environment(运行环境)

*  Python 3.5+ 
*  Linux/Windows/MAC OS
*  Third-party library (threading, threadingpool )

##Installation(安装)

*  git clone  <https://github.com/evilmao/XSTZ_loading_test.git>
*  cd XSTZ_load_test
*  `pip install -r requirements.txt`

##Usage 

*  安装完毕后，根据需求编辑datainfo.py文件，包含但不限于以下内容 payload(基本参数)，accountinfo(账户信息)，url(API接口)

*  `InjectionTrade_threadpool.py` 基于线程池原理，对并发数可控()，非阻塞（建议使用）。

*  `InjectionTrade_mutilprocess.py` 基于multiprocessing 模块，使用多进程模式测试，适用于windows多核模式下。

*  `InjectionTrade_thread.py` 基于threading.Thread() 多线程模型，lInux单核模式下测试。

*  执行

    ```shell
   python InjectionTrade_threadpool.py  #pool = threadpool.ThreadPool(500) //line41 可调节并发数
    ```

*  取值：成功失败数据被写入本地文件 Injection_success.txt 和Injection_error.txt中，打开文本获得压测基本数据。

## Support 

此脚本分三个版本，分别使用多线程，多进程，线程池方式进行测试，建议使用线程池方法，同时，在模拟多用户时，需尽量使用多个账号进程测试。否则出现 `{'IsSuccess': False, 'Message': "不能在具有唯一索引 'IX_MS_Deposit_BillNo' 的对象 'dbo.MS_Deposit' 中插入重复键的行。\r\n语句已终止。", 'Page': None}` 错误。