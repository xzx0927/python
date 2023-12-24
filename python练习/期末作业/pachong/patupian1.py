import requests

from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 '
                  'Safari/537.36 Edg/119.0.0.0',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://10wallpaper.com/'
}
wangzhan_zidian = {'Landscape': 39, 'People': 34, 'Plants': 21, 'Amimal': 17, 'Movie': 26, 'Game': 19, 'City': 10,
                   'Desige': 22, 'Photography': 25, 'Space': 3, 'Sports': 14, 'Advertising': 25, 'Auto': 32,
                   'Military': 5, 'Festivals': 9, 'Other': 44}
for key in wangzhan_zidian:
    type_url = 'https://10wallpaper.com/' + key
    pages = wangzhan_zidian[key]
    for page in range(1, pages):
        list_page_content = requests.get(type_url + '_wallpapers/page/' + str(page), headers=header).content.decode(
            'utf-8')  # 译码的网址
        soup = BeautifulSoup(list_page_content, 'html.parser')  # 创建对象
        yiceng_r = soup.find(class_='col-right')
        yiceng_r1 = yiceng_r.select('div p a')
        for a in yiceng_r1:
            s = a["href"]
            if s.startswith('/list/'):
                s1 = s
                print(s1)
                erceng_url = "https://10wallpaper.com" + s1
                erceng_res = requests.get(erceng_url, headers=header).content.decode('utf-8')
                soup1 = BeautifulSoup(erceng_res, 'html.parser')
                erceng_r = soup1.find(class_='pics')
                erceng_r1 = erceng_r.select('p a')
                for r in erceng_r1:
                    b = r['href']
                    if b.startswith('/view/'):
                        b1 = b
                        print(b1)
                        sanceng_url = "https://10wallpaper.com" + b1
                        sanceng_res = requests.get(sanceng_url, headers=header).content.decode('utf-8')
                        soup2 = BeautifulSoup(sanceng_res, 'html.parser')
                        sanceng_r = soup2.find(class_='inner')
                        sanceng_r1 = sanceng_r.select('p img')
                        for c in sanceng_r1:
                            print(c['src'])
                            siceng_url = "https://10wallpaper.com" + c['src']
                            siceng_res = requests.get(siceng_url, headers=header)
                            img_name = c['src'].split('/')[-1]
                            with open('img/' + img_name, 'wb') as f:
                                f.write(siceng_res.content)
                                f.close()
                                print('下载成功')

        # page_regexp = '<a href="(/list/\w+Photo.html)">'  # 正则表达式
        # page_pattern = re.compile(page_regexp)  # 转译
        # page_results = page_pattern.findall(list_page_content)  # 比对符合条件的网址
        #     nei_content = res.content.decode('utf-8')
        #     tu_regexp = '<a href="(/view/\w+.html)" target="_blanck">'
        #     tu_pattern = re.compile(tu_regexp)
        #     tu_results = tu_pattern.findall(nei_content)
        #     for ti_url in tu_results:
        #         x_url = 'https://10wallpaper.com' + ti_url
        #         x_res = requests.get(x_url, headers=header).content.decode('utf-8')
        #         x_regexp = 'wallpaper/1366x768/[\S]+.jpg'
        #         pattern=re.compile(x_regexp)  # 编码正则表达式
        #         results = pattern.findall(x_res)
        #         print(results)
        #         for url in results:
        #             req = requests.get('https://10wallpaper.com/'+url, headers=header) # 调整分辨率
        #             img_name = url.split('/')[-1]
        #             with open('img/' + img_name, 'wb') as f:
        #                 f.write(req.content)
        #                 f.close()
