import os
import time
import requests
import xlwt
from selenium import webdriver
from selenium.webdriver.common.by import By
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}
global i #全局变量
global j
i=0
j=0
type_list = []
type_list1 = []
type_list2 = []
type_list3 = []

browser = webdriver.Chrome()
wb = xlwt.Workbook('utf-8')#创建表格
sh = wb.add_sheet('doubanshipin')
sh.write(0, 0, '排名')
sh.write(0, 1, '电影名')
sh.write(0, 2, '参演人员')
sh.write(0, 3, '首评')
browser.get('https://movie.douban.com/top250')
time.sleep(1)
d = browser.find_elements(By.CSS_SELECTOR, 'body div div div div ol li div div div a')
for type_ in d[0:]:
   type_list.append(type_.get_attribute("href"))
   print(type_.get_attribute("href"))
#
for t in type_list:
    i = i+1
    j = 0
    try:
        browser.find_element(By.CSS_SELECTOR, ".more-actor").click()#无更多处理方法
        browser.find_element(By.CSS_SELECTOR, ".expand").click()
    except Exception as e:
        print()
    time.sleep(1)
    browser.get(t)
    paiming = browser.find_element(By.CSS_SELECTOR, ".top250-no").text
    paiming2 = browser.find_element(By.CSS_SELECTOR, ".top250-link a").text
    mingzi = browser.find_element(By.CSS_SELECTOR, "h1 span").text
    renyuan = browser.find_element(By.CSS_SELECTOR, 'div #info').text
    pinglun = browser.find_element(By.CSS_SELECTOR, 'p .short').text
    print(paiming)
    print(paiming2)
    print(mingzi)
    print(renyuan)
    print(pinglun)
    sh.write(i, j,  paiming+paiming2)
    j = j + 1
    sh.write(i, j, mingzi)
    j = j + 1
    sh.write(i, j, renyuan)
    j = j + 1
    sh.write(i, j,  pinglun)
    j=j+1
    wb.save('text.xls')

input()
