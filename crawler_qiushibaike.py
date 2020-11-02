# author: join 
# time: 10/31/2020

import requests
import re
import os

'''
# download image

url = 'https://pic.qiushibaike.com/article/image/K765ALIOWP16XANB.jpg'
image_data = requests.get(url = url).content
with open('./demo.jpg','wb') as fp:
    fp.write(image_data)
'''

''' image restore format
<div class="thumb">

<a href="/article/123735881" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12373/123735881/medium/Q0SD0M6R39DE3YG5.jpg" alt="糗事#123735881" class="illustration" width="100%" height="auto">
</a>
</div>

reg: ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
'''

if __name__ == "__main__":
    if not os.path.exists('./qiutu'):
        os.makedirs('qiutu')

    ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'

    headers = {
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51'
    }

    for page in range(10):
        url = f'https://www.qiushibaike.com/imgrank/page/%d/' % page
        page_text = requests.get(url=url, headers=headers).text
        # print(page_text)

        #regex
        image_src_list = re.findall(ex, page_text, re.S)

        for src in image_src_list:
            src = 'https:' + src
            image_data = requests.get(src).content
            image_name = src.split('/')[-1]
            image_path = './qiutu/' + image_name

            with open(image_path, 'wb') as fp:
                fp.write(image_data)
