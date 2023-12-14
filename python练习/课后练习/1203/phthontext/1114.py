import time

import xlwt
from selenium import webdriver
from selenium.webdriver.common.by import By

brower = webdriver.Edge()
brower.get('https://movie.douban.com/top250?start=25o')
wb = xlwt.Workbook('utf-8')
sh = wb.add_sheet('douban')

global a
a = 0
c = ['排名','名称','大概信息','评论']
for x in (0, 10):
    t = brower.find_elements(By.CSS_SELECTOR, '.item .pic a')
    for i in t:
        for b in range(a, a+1):
            for j in range(0,4):
                print(c[j])
                sh.write(b, j, label=c[j])
        c.clear()
        s = i.get_attribute('href')
        js = 'window.open("' + s + '");'
        brower.execute_script(js)
        all_handles = brower.window_handles  # 获取全部窗口语炳集合
        now_handles = brower.current_window_handle  # 获取当前
        brower.switch_to.window(all_handles[-1])  # 切换当前窗口
        # time.sleep(2)
        xuhao = brower.find_element(By.CSS_SELECTOR, '.top250-no').text
        c.append(xuhao)
        # print(xuhao)
        name = brower.find_element(By.CSS_SELECTOR, 'h1').text
        c.append(name)
        # print(name)
        try:
            genduo = brower.find_element(By.CSS_SELECTOR, '.more-actor').click()
        except Exception as e:
            print("没有更多")
        yanyuan = brower.find_element(By.CSS_SELECTOR, 'div #info').text
        c.append(yanyuan)
        # print(yanyuan)
        pinglun = brower.find_element(By.CSS_SELECTOR, 'p .short').text
        c.append(pinglun)
        # print(pinglun)
        print(c)
        a = a + 1
        wb.save('text.xls')
        brower.close()
        brower.switch_to.window(now_handles)
    brower.find_element(By.CSS_SELECTOR, '.next').click()
a=0


