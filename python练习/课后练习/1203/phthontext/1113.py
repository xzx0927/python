import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://10wallpaper.com/',
}
b = webdriver.Edge()
for page in range(1, 3):
    b.get('https://10wallpaper.com/List_wallpapers/page/' + str(page))
    # list_page_content = requests.get('https://10wallpaper.com/', headers=header).content.decode('utf-8')
    t = b.find_elements(By.CSS_SELECTOR, 'div p a img')
    print(t)
    for i in t:
        req = requests.get(i.get_attribute('src').replace('1280x720', '3840x2160'), headers=header)
        i_name = i.get_attribute('src').split('?')[-1]
        print(i_name)
        x=0
        with open('img/' + str(x), 'wb') as f:
            x=x+1
            f.write(req.content)
            f.close()
        # x = 0
        # with open('img/'+ x, 'wb') as f:
        #     x++
        #     f.write(req.content)
        #     f.close()

    # for i in t:
    #     print(i['src'])
input()

