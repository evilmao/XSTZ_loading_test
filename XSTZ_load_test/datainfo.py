#coding:utf-8
'''
    1.参数信息处理
    -- payload 为基本参数(dict)；
    -- accountinfo 账号信息(list)
    -- payload_list 发送参数信息（list）
'''
payload  = {
                'Money':0.01,
                'PayType':14,
                'BankName':'中国建设银行',
                'BankType':'CCB',
                'Source':2,
                #'BankCard':'6217004229999718484'#6221505200007030713
            }

accountinfo = [
                {'Account':8000005,'Name':'测试魏小东'}
            ]*2000
        
payload_list = [] #空列表用来存储发送参数
url = 'http://192.168.0.249:8001/Center/Deposit'  #API接口url
url1 = 'http://192.168.0.249:8001/Center/WYDeposit' #绑定银行卡后，打款

#生成发送参数参数列表
for user in accountinfo:
    user.update(payload)
    payload_list.append(user)


if __name__ == '__main__':    
    print (payload_list)

    

    
    
  
    






