# Chatbot_S2S

基于苏神的gpt-2代码和模型封装的闲聊项目

# 使用方式
 1、clone代码
 
 2、按装依赖
    
    pip install -r requirements.txt
 
 3、下载训练好的模型。同时你也可以自己训练
    
    模型地址：链接:https://pan.baidu.com/s/1NPR8GcG3tFMeFlOevmIDnQ  密码:3s97
  
 4、修改config.py文件，路径为model/config.py
 
 5、运行服务
    
    python server/run_server.py
 
 6、测试。可以用postman
 
    {
        "sender": "202009160002",
        "message": "我想点外卖"
    }
    
    返回结果：
    
    {
        "result": "我想吃烧烤",
        "time": "2020-10-03 03:30:15"
    }

# 后续

    1、目前由于参数量较大，响应时间较慢，后续会使用模型加速进行优化

# 参考
1、https://github.com/bojone/nezha_gpt_dialog

2、https://github.com/thu-coai/CDial-GPT
