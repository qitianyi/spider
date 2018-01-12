import requests
import json
import time
def signIN_sso(sno,password):
    url_log = 'http://sso.jwc.whut.edu.cn/Certification/login.do'
    post_data = {
        'imageField.x': '39', 'imageField.y': '30', 'userName': sno, 'password': password, 'type': 'xs'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Referer': 'http://sso.jwc.whut.edu.cn/Certification/toLogin.do',
    }
    s=requests.Session()
    test=s.post(url_log,data=post_data,headers=headers)
    jse_url='http://202.114.90.180/Course/'
    s.get(url=jse_url,headers=headers)
    s.close()
    return s.cookies

def get_data(cookies):
    """
    post_data的信息从谷歌浏览器拿到  
    
    :param cookies: 
    :return: 
    """
    post_data={
    'xnxq':'2017-2018-2',
    'kcdm':'6010021000',
    'jxjhh':'2016',
    'addid':'5D0EEA323EDE056CE053FD02A8C04864',
    'gsdm':'',
    'keyinfo':'C4564AFD4F6C72F773A41AAC2A97698B',
    '_':""
    }
    url='http://202.114.90.180/Course/gxkxkAdd.do'
    s=requests.session()
    s.cookies=cookies
    error=300
    while error==300:
        try:
            tim = int(time.time())
            post_data['_']=str(tim)
            page=s.get(url=url,params=post_data)
            data=json.loads(page.text)
            error=int(data['statusCode'])
            print(data['message'])
            time.sleep(1)
            #3s一次
        except:
            get_data(cookies)
    s.close()
if __name__=='__main__':
    cookies=signIN_sso(sno='0121610880122',password='qty340474')
    get_data(cookies)