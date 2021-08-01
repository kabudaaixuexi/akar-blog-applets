# -*- coding:utf-8 -*-
import urllib
import urllib.request
import hmac
import hashlib
import base64
import time
import random
import os
import Config

def formatSignString(param):
    signstr = "POSTasr.cloud.tencent.com/asr/v1/"
    for t in param:
        if 'appid' in t:
            signstr += str(t[1])
            break
    signstr += "?"
    for x in param:
        tmp = x
        if 'appid' in x:
            continue
        for t in tmp:
            signstr += str(t)
            signstr += "="
        signstr = signstr[:-1]
        signstr += "&"
    signstr = signstr[:-1]
    # print 'signstr',signstr
    return signstr


def sign(signstr, secret_key):
    hmacstr = hmac.new(secret_key.encode('utf-8'), signstr.encode('utf-8'), hashlib.sha1).digest()
    s = base64.b64encode(hmacstr)
    # print 'sign: ',s
    return s.decode('utf-8')


def randstr(n):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(n):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    # print salt
    return salt

def createQueryArr(template_name=""):
    query_arr = dict()
    query_arr['appid'] = Config.config.APPID
    query_arr['projectid'] = 1013976
    if len(template_name) > 0:
        query_arr['template_name'] = template_name
    query_arr['sub_service_type'] = 1
    query_arr['engine_model_type'] = Config.config.ENGINE_MODEL_TYPE
    query_arr['res_type'] = Config.config.RES_TYPE
    query_arr['result_text_format'] = Config.config.RESULT_TEXT_FORMAT
    query_arr['timeout'] = 100
    query_arr['source'] = 0
    query_arr['needvad'] = 0
    query_arr['secretid'] = Config.config.SECRETID
    query_arr['timestamp'] = str(int(time.time()))
    query_arr['expired'] = int(time.time()) + 24 * 60 * 60
    query_arr['nonce'] = query_arr['timestamp'][0:4]
    query_arr['voice_format'] = Config.config.VOICE_FORMAT
    if Config.config.HOT_WORD_ID != "" :
        query_arr['hotword_id'] = Config.config.HOT_WORD_ID
    query_arr['filter_dirty'] = Config.config.FILTER_DIRTY
    query_arr['filter_modal'] = Config.config.FILTER_MODAL
    query_arr['filter_punc'] = Config.config.FILTER_PUNC
    query_arr['convert_num_mode'] = Config.config.CONVERT_NUM_MODE
    query_arr['word_info'] = Config.config.WORD_INFO
    return query_arr

# 对传入的文件，分片后不断发送请求接收回复，发完全部分片后返回最终收到的回复。
def sendVoice(filepath, printCutResponse):
    if len(str(filepath)) == 0:
        print('filepath can not be empty')
        return
    query_arr = createQueryArr()
    query_arr['voice_id'] = randstr(16)
    
    file_object = open(filepath, 'rb')
    file_object.seek(0, os.SEEK_END)
    datalen = file_object.tell()
    file_object.seek(0, os.SEEK_SET)
    seq = 0
    while (datalen > 0):
        end = 0
        if (datalen < Config.config.CUT_LENGTH):
            end = 1
        query_arr['end'] = end
        query_arr['seq'] = seq
        query = sorted(query_arr.items(), key=lambda d: d[0])
        signstr = formatSignString(query)
        autho = sign(signstr, Config.config.SECRET_KEY)

        if (datalen < Config.config.CUT_LENGTH):
            content = file_object.read(datalen)
        else:
            content = file_object.read(Config.config.CUT_LENGTH)
        seq = seq + 1
        datalen = datalen - Config.config.CUT_LENGTH
        headers = dict()
        headers['Authorization'] = autho
        headers['Content-Length'] = len(content)
        requrl = "http://"
        requrl += signstr[4::]
        req = urllib.request.Request(requrl, data=content, headers=headers)
        res_data = urllib.request.urlopen(req)
        res = res_data.read()
        if (printCutResponse):
            print(res)
    file_object.close()
    return res

# 发送单个分片的请求，返回单次请求的回复信息。
def sendRequest(content, voiceId, seq, endFlag):
    if(len(str(content))) == 0:
        print('content length can not be empty')
        return ''
    query_arr = createQueryArr()
    query_arr['voice_id'] = voiceId
    query_arr['end'] = endFlag
    query_arr['seq'] = seq
    query = sorted(query_arr.items(), key=lambda d: d[0])
    signstr = formatSignString(query)
    autho = sign(signstr, Config.config.SECRET_KEY)
    headers = dict()
    headers['Authorization'] = autho
    headers['Content-Length'] = len(content)
    requrl = "http://"
    requrl += signstr[4::]
    req = urllib.request.Request(requrl, data=content, headers=headers)
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    return res
