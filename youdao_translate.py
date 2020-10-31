# -*- coding:utf-8 -*-
import requests
import json
import re
import os
import time
import sys

def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        # 然后相应的结果
        return response.text
    else:
        print("trans--"+ word +"---fail..")
        return None

def main():
    print("本程序调用有道词典的API进行翻译，可达到以下效果：")
    print("外文-->中文")

    r1 = input("请输入翻译文件路径：")
    if r1 == '':
        r1 = r"C:\Users\Administrator\Desktop\node_name.txt"

    r2 = r"keyword_dst.txt"

    with open(r1, 'r+', encoding="utf-8") as f1, open(r2, 'w+', encoding="utf-8") as f2:

        while True:
            text = f1.readline()
            if not text:
                return

            f2.write(text)

            if "msgid" in text:
                res = re.match(r'msgid "(.+)"', text.strip(), re.M | re.I)
                word = res.group(1)
                
                word = word.replace('\\n','').replace('\\t','')#防止待翻译文中存在\n\t使翻译结果不符合预期
                
                #print(translate(word))
                response = translate(word)
                result = json.loads(response)
                trans = result['translateResult'][0][0]['tgt']

                npos = f1.readline().find('m')
                f2.write("msgstr \"" + trans + "\"\n")
                print(word + '>>>>' + trans)                



if __name__ == '__main__':
    main()
