'''
# 人脸检测与属性分析
'''
import base64
import urllib
import urllib.request,sys,base64
import urllib.parse
import json
import joint
import cv2

#request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"

f = open('/home/zhengr/Documents/data/1.jpg', 'rb')
image = base64.b64encode(f.read())
image64 = str(image,'utf-8')
image_type = "BASE64"



# params = "{\"image\":\"%s\",\"image_type\":\"BASE64\",\"face_field\":\"faceshape,facetype\"}"%image64
#params = {'image': image64,'image_type':"BASE64",'face_field': 'person_info'}
params = {'image': image64,'image_type':"BASE64"}
# 此处的faceshape和facetype需要自己加上去 更具自己需要的返回值

params = urllib.parse.urlencode(params).encode("utf-8")


access_token = '[24.fdd8df19e52da8ff449e1484aa582f42.2592000.1556250057.282335-15823849]'
request_url = request_url + "?access_token=" + access_token

request = urllib.request.urlopen(url=request_url, data=params)   # 发送请求

content = request.read()  # 将返回结果读取出来
print(content)  # 显示返回结果
result = str(content,'utf-8')
res = json.loads(result)
print(res['person_info'][0]['body_parts'])
ress = res['person_info'][0]['body_parts']
jo = joint.Joint(ress)
jo.xunhun('/home/zhengr/Documents/data/1.jpg')


import urllib.request,sys,base64
import urllib.parse

