import requests
import re
import os
from multiprocessing import Pool


def shuaTMD():
    url = 'http://tpv.daxiangdaili.com/ip/'
    payload = {'tid': '557415012412212',
               'num': '5'}
    r = requests.get(url, params=payload)
    p = re.compile('[\r\n]')
    list = p.split(r.text)
    list = [x for x in list if x != '']

    for i in range(5):
        try:
            dic = {'http': list[i], 'https': list[i]}
            s = requests.session()
            headers1 = {'Host': 'jwc.uibe.edu.cn', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'zh-CN,zh;q=0.8'}
            r = s.get('http://jwc.uibe.edu.cn/WeiKe/ZhanShi.aspx?from=groupmessage&isappinstalled=0',
                      proxies=dic, headers=headers1, timeout=1)
            cookies = {'_LiuLanQiID_': r.headers['Set-Cookie'][13:-18]}
            headers2 = {'Host': 'jwc.uibe.edu.cn', 'Connection': 'keep-alive', 'Accept': '*/*', 'X-Requested-With': 'XMLHttpRequest',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36', 'Referer': 'http://jwc.uibe.edu.cn/WeiKe/ZhanShi.aspx?from=groupmessage&isappinstalled=0', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'zh-CN,zh;q=0.8'}
            r = s.get('http://jwc.uibe.edu.cn/WeiKe/VideoDianZan.ashx?zpid=7f967bce14fe4dd298f950ba17d15adb',
                      proxies=dic, cookies=cookies, headers=headers2, timeout=1)
            if len(r.text) > 100:
                print('Task %s : No' % (os.getpid()))
            else:
                print('Task %s : %s...' % (os.getpid(), r.text))
        except:
            # print('失败')
            continue


def main():
    count = 0
    while 1:
        count += 1
        pool = Pool(processes=10)
        for i in range(10):
            pool.apply_async(shuaTMD)
        print('进程' + str(count) + '开始')
        pool.close()
        pool.join()
        print('执行' + str(count) + '完毕\n')
    # while 1:
    #     shuaTMD()

if __name__ == '__main__':
    main()
