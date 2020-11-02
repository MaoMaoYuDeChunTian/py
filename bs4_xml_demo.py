# author: join 
# time: 10/31/2020

import requests
from bs4 import BeautifulSoup

'''
soup.tagName 第一次出现的tagname 
soup.find('tagName') 标签定位
soup.find(tagName,class_='className') 属性定位
soup.find_all() 返回find结果的列表
soup.select('tagname | id | class')
层级选择器 .className > ul > li a  其中>表示一个层级 空格表示多个层级

获取文本内容：.text get_text()---标签下的所有文本  .string--标签下的直系文本 
'''

if __name__ == '__main__':
    url = 'https://xiaoshuo.sogou.com/list/13146766242'
    url_home = 'https://xiaoshuo.sogou.com'
    headers = {
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51'
    }
    list_content = requests.get(url=url, headers=headers).text
    list_bs = BeautifulSoup(list_content, 'lxml')
    list_element = list_bs.find_all('li', class_='c3')

    fp = open('./linktext.text', 'w', encoding='utf-8')

    for element in list_element:
        url_suffix = element.a.get('href')
        category_title = element.a.string
        print(url_suffix)

        url_content = url_home + url_suffix
        print(url_content)
