# -*- coding:utf-8 -*-
# 引用 SDK
import RASRsdk
import os
import Config

# ----------------------------- 调用方法1 -----------------------------
# 音频文件路径
filepath = "../../test_wavs/8k.wav"
# 调用语音识别函数获得识别结果, 参数2标识是否打印中间结果到控制台
result = RASRsdk.sendVoice(filepath, True)
print("Final result: " + str(result))

# ---------------------------------------------------------------------
# 若需中途调整参数值，可直接修改，然后继续发请求即可。比如：
Config.config.ENGINE_MODEL_TYPE = '8k_0'

# ----------------------------- 调用方法2 -----------------------------
def requestExample():
    # 将音频文件分解成小的切片数据（即：切分成长度较小的多个字符串）发出。模拟不断发送数据接收回复，最终收完整句话的识别结果。
    filepath = "../../test_wavs/8k.wav"
    file_object = open(filepath, 'rb')
    file_object.seek(0, os.SEEK_END)
    datalen = file_object.tell()
    file_object.seek(0, os.SEEK_SET)
    
    # 发送请求时需要用户自行维护3个变量：voiceId：创建后保持不变； seq：递增； endFlag：前面为0，发送尾部分片的请求时设置为1
    voiceId = RASRsdk.randstr(16)
    seq = 0
    endFlag = 0
    while (datalen > 0):
        if (datalen < Config.config.CUT_LENGTH):
            endFlag = 1
            content = file_object.read(datalen)
        else:
            content = file_object.read(Config.config.CUT_LENGTH)
        res = RASRsdk.sendRequest(content, voiceId, seq, endFlag)
        print(res)  # 打印收到的结果到控制台。示例用途。
        seq = seq + 1
        datalen = datalen - Config.config.CUT_LENGTH
    file_object.close()

# 使用方法2
requestExample()

