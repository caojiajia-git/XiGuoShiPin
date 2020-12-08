import json
import base64
import time
import requests

def one():
    url = "https://www.ixigua.com/api/videov2/author/video?_signature=_02B4Z6wo00f01NgHi3QAAIBBlUlZL0FrR0DYBo.AAGme49&author_id=104813200378&type=hotsoon&max_time=0"
    # url = "https://www.ixigua.com/home/104813200378/hotsoon/?preActiveKey=video"
    headers = {
        'Host':'www.ixigua.com',
        'referer':'https://www.ixigua.com/home/104813200378/hotsoon/?preActiveKey=video',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'cookie': 'ttwid=6886003189775386125; ttwid.sig=iiVjdzkcb-NPlnE5QuxwQMsWqgc; xiguavideopcwebid=6886003189775386125; xiguavideopcwebid.sig=TIRP0hiHoJ4d7AiEAVhaq4RHSOA; MONITOR_WEB_ID=addbd662-af47-4af4-9342-072535e2e741; _ga=GA1.2.626853169.1603272559; ixigua-a-s=1; Hm_lvt_db8ae92f7b33b6596893cdf8c004a1a2=1603416904,1603503838,1603510074,1603675056; _gid=GA1.2.1834030952.1603675056; ttcid=9b3914a83ef54d388fd439c5d5ddf63a30; __ac_nonce=05f966c5d0031fd2124d6; __ac_signature=_02B4Z6wo00f01DP5wwwAAIBBfrcRVEt-H0Az-ceAAFNt3c; _gat_gtag_UA_89504546_18=1; Hm_lpvt_db8ae92f7b33b6596893cdf8c004a1a2=1603694463'

    }
    req = requests.get(url=url,headers=headers)
    req.encoding='utf-8'
    content=json.loads(req.text)
    a_list = content['data']['data']
    # print(a_list)
    list_ = []
    for i in a_list:
        title = i['title']
        # a_url = i['share']['share_url']
        a_url = 'https://www.ixigua.com/' + i['group_id']
        # print(title)
        # print(a_url)
        req2 = requests.get(url=a_url,headers=headers)
        req2.encoding='utf-8'
        aa = req2.text
        # print(aa)
        bb = ''.join(aa)
        try:
            cc = bb.split('"video_1":')[1].split('"main_url":"')[1].split('","backup_url_1"')[0]
        except:
            cc = bb.split('"video_2":')[1].split('"main_url":"')[1].split('","backup_url_1"')[0]
        # print(cc)
        debs64 = base64.b64decode(cc)
        # print(debs64)
        aa = str(debs64).rfind('/')
        debs642 = str(debs64)[:aa+1]
        xin_url = debs642[2:]
        list_.append(xin_url)
    down_video(list_)

def down_video(list_):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    for i in list_:
        print(i)
        time.sleep(1)
        r = requests.get(i, headers=header,stream=True)
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        time.sleep(1)
        with open(r'./' + picture_time + '.mp4', "wb") as mp4:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    mp4.write(chunk)

if __name__ == '__main__':
    one()





