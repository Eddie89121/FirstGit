import random
# from openpyxl.workbook.workbook import Workbook 
# import requests 
# import json 
# from datetime import datetime 

# # 헤더값은 각자의 f12의 내용 참고해서 작성해야됨. 아래 코드의 값과 다를 수 있음. 
# header = { 
#     'accept': '*/*', 
#     'accept-encoding': 'gzip, deflate, br', 
#     'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7', 
#     'cookie': 'mid=Yl4A5gALAAGkM1xRDCnHj_QMA0LC; ig_did=24E6B9F6-818E-450A-AD22-ACBE78D4F374; ig_nrcb=1; csrftoken=CUQ91TR4rkLcWI5GX7yItQDEMfCZLyX5; ds_user_id=52627331756; sessionid=52627331756%3A26RfWACrO824k6%3A18; rur="EAG\05452627331756\0541681864196:01f7e0a60374ee15f81170706387198314d0166585cc588474aa3ae552d60d7ce26df77b"', #교체
#     'referer': "https://www.instagram.com/", 
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 
#     'sec-ch-ua-mobile': '?0', 
#     'sec-ch-ua-platform':'windows', 
#     'sec-fetch-dest': 'empty', 
#     'sec-fetch-mode': 'cors', 
#     'sec-fetch-site': 'same-origin', 
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36', #교체
#     'x-asbd-id': '198387', 
#     'x-ig-app-id': '936619743392459', 
#     'x-ig-www-claim': 'hmac.AR0xvMfbTxmrH54oW4AQdaa_T5SSYuD9uxm4nQtPyh-icvhY', #교체
#     'x-requested-with': 'XMLHttpRequest' 
#     } 


# dataList = [] 
# search = '여행'
# URL = 'https://www.instagram.com/explore/tags/'+search+'/?__a=1' 

# # 개수확인용도 
# pidCount = 0 

# while(True): 

#     res = requests.get(URL, headers =header) 
#     res = res.json() 

#     if 'next_page' not in res['data']['recent'].keys() or int(res['data']['recent']['next_page']) == 0: break 
#     max_id = res['data']['recent']['next_max_id'] 


#     for n in res['data']['recent']['sections']: 
#         for m in ((n['layout_content']['medias'])): 
#             # m : 인스타 게시글 1개 
#             m = m['media'] 
#             data = {} 
#             data['pagePk'] = m['code'] 
#             data['URL'] = 'https://www.instagram.com/p/'+ data['pagePk']+"/" 
#             data['user_name'] = (m['user']['username']) 

#             # 이미지/동영상 체크 
#             keys = m.keys() 
#             if 'carousel_media' in keys: 
#                 data['image'] = (m['carousel_media']) 
#             else: 
#                 data['image'] = [{'image_versions2':{"candidates":[{'url'}]}}] 
#                 # data['image'] = [{'image_versions2':{"candidates":[{'url':'동영상업로드'}]}}] 
            
#             dataList.append(data) 
#             pidCount = pidCount+1 

#             comments = m['comments']
            
#             # print(m.keys())

#             # print(data['URL'])
#             for i in range(len(comments)):
#                 if 'comments' not in m.keys():
#                     continue
#                 print(str(pidCount) + '번 ' + str(i+1) + '  ' +'@' + data['user_name'] + ', 댓글 : ' + comments[i].get('text') + ', URL : ' + data['URL'])
               


#     URL = 'https://www.instagram.com/explore/tags/'+search+'/?__a=1&max_id='+max_id 
    

def time():
    a=True
    while(a):
        r = (random.random()*10)+1
        if r >= 6 and r <= 10:
            t = r
            a=False
        else:
            continue
        return t

print(time())