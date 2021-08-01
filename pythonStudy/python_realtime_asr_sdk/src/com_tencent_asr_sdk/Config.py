# -*- coding:utf-8 -*-
'''
Created on 2019-4-24
@author: iantang
'''

class Config:
    '全局变量配置信息，请按需求改成自己的配置'
    
    # ------------- Required ---------------
    # AppId, secretId, secretKey获取方法可参考截图： 
    # https://cloud.tencent.com/document/product/441/6203
    # 具体路径：点控制台右上角您的账号-->选：访问管理-->点左边菜单的：访问秘钥-->API秘钥管理
    SECRET_KEY = 'Your SecretKey'
    SECRETID = 'Your SecretId'
    APPID = 'Your AppId'
    
    
    # ------------- optional，根据自身需求配置值 ---------------
    # 识别引擎 8k_0 or 16k_0
    ENGINE_MODEL_TYPE = '16k_0'
    # 结果返回方式 0：同步返回 or 1：尾包返回
    RES_TYPE = 0
    # 识别结果文本编码方式 0:UTF-8, 1:GB2312, 2:GBK, 3:BIG5
    RESULT_TEXT_FORMAT = 0
    #  语音编码方式 1:wav  4:sp  6:skill
    VOICE_FORMAT = 1
    #热词id
    HOT_WORD_ID = ""
    # 后处理参数
    FILTER_DIRTY = 0
    FILTER_MODAL = 0
    FILTER_PUNC  = 0
    CONVERT_NUM_MODE = 0
    WORD_INFO = 0
    # 语音切片长度 cutlength<200000
    CUT_LENGTH = 8192
    
    # ------------- 下面是初始化和验证方法，可跳过 ---------------
    def __init__(self):
        print ("")  

    def verifyProperties(self):
        if len(str(self.SECRET_KEY)) == 0:
            print('SECRET_KEY can not empty')
            return
        if len(str(self.SECRETID)) == 0:
            print('SECRETID can not empty')
            return
        if len(str(self.APPID)) == 0:
            print('APPID can not empty')
            return
        
        if len(str(self.ENGINE_MODEL_TYPE)) == 0 or (
            str(self.ENGINE_MODEL_TYPE) != '8k_0' and str(self.ENGINE_MODEL_TYPE) != '16k_0' and str(self.ENGINE_MODEL_TYPE) != '16k_en'):
            print('ENGINE_MODEL_TYPE is not right')
            return
        if len(str(self.RES_TYPE)) == 0 or (str(self.RES_TYPE) != '0' and str(self.RES_TYPE) != '1'):
            print('RES_TYPE is not right')
            return
        if len(str(self.RESULT_TEXT_FORMAT)) == 0 or (str(self.RESULT_TEXT_FORMAT) != '0' and str(self.RESULT_TEXT_FORMAT) != '1' and str(
                self.RESULT_TEXT_FORMAT) != '2' and str(self.RESULT_TEXT_FORMAT) != '3'):
            print('RESULT_TEXT_FORMAT is not right')
            return
        if len(str(self.VOICE_FORMAT)) == 0 or (
            str(self.VOICE_FORMAT) != '1' and str(self.VOICE_FORMAT) != '4' and str(self.VOICE_FORMAT) != '6'):
            print('VOICE_FORMAT is not right')
            return
        if len(str(self.CUT_LENGTH)) == 0 or str(self.CUT_LENGTH).isdigit() == False or self.CUT_LENGTH > 200000:
            print('self.CUT_LENGTH can not empty or length must < 200000')
            return
    
config = Config()
config.verifyProperties()
