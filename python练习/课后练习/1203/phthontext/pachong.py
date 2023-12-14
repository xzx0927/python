import re

import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 '
                  'Safari/537.36 Edg/118.0.2088.76',
    'Referer': 'https://desk.zol.com.cn/bizhi/10054_120337_2.html',
    'Sec-Fetch-Site': 'cross-site'
}
res = requests.get('https://desk.zol.com.cn/bizhi/10054_120337_2.html', headers=header)
page_content = res.content.decode('gbk')
regexp ='https://desk-fd.zol-img.com.cn/t_s144x90c5/g7/M00/04/07/[-\w]+.jpg'  # 正则表达式
pattern = re.compile(regexp)

results = pattern.findall(page_content)
print(results)
for url in results:
    req = requests.get(url, headers=header)
    img_name = url.split('/')[-1]
    with open('img/' + img_name, 'wb') as f:
        f.write(req.content)
        f.close()
