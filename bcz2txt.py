#-*- coding:utf-8 -*-
#author:pinko

import requests
from bs4 import BeautifulSoup
import json
import random

# 自动登录百词斩，爬取已经学过的单词，生成一个txt，可以上传到欧路词典后台作为复习课本，然后就可以用欧路词典进行复习。欧路词典单词复习课本地址:https://my.eudic.net/recite/userbooks

# Usage: 修改下面的配置参数运行即可，不需要参数
# Dependency: Python2.7,requests,BeautifulSoup,json

#百词斩的登录邮箱
USERNAME = "****@foxmail.com"
#百词斩的登录密码
PASSWORD = "****"
#想要生成的txt的文件名
WORD_LIST_NAME = "word_done.txt"
#生成的复习书是否随机排列，如果字母排列改成False
IS_RANDOM = True


def test_code(code):
    if code == 200:
        print "[+] Done. "
    else:
        print code
        print "[+] Network Error "
        quit()

url = "http://www.baicizhan.com/login"
UA = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"

headers = {
    "User-Agent" : UA,
    "Referer": "http://www.baicizhan.com/login"
    }

print "[=] Prepare Login ..."

login_sess = requests.Session()
re = login_sess.get(url, headers=headers)

#print re.status_code
test_code(re.status_code)

soup = BeautifulSoup(re.content,"html.parser")
utf8 = soup.find('input',{'name':'utf8'})['value']
authenticity_token = soup.find('input',{'name':'authenticity_token'})['value']
#print utf8
print "[=] Token: "+str(authenticity_token)

data = {
    "email" : USERNAME,
    "raw_pwd" : PASSWORD,
    "utf8" : utf8,
    "authenticity_token" : authenticity_token
}

re = login_sess.post(url, headers=headers, data=data)

print "[=] Login ..."
#print re.status_code
test_code(re.status_code)
#print re.content

word_url = "http://www.baicizhan.com/user/all_done_words_list?page=1"

re = login_sess.get(word_url, headers=headers)

print "[=] Searching Infomation ... "
#print re.status_code
test_code(re.status_code)
#print re.content
info = json.loads(str(re.content))
#print info

page_num = info["total_page"]
#print page_num

word_num = info["total_count"]
#print word_num

print "[=] Page:"+str(page_num)+" / Word:"+str(word_num)
print "[=] Now Start Crawling ..."

word_list = []
for i in range(1,int(page_num)+1):
    word_list_url = "http://www.baicizhan.com/user/all_done_words_list?page="+str(i)
    print "[=] Getting Page "+str(i)+"/"+str(int(page_num))+" ..."
    re = login_sess.get(word_list_url, headers=headers)
    #print re.status_code
    test_code(re.status_code)
    #print re.content
    info = json.loads(str(re.content))
    #print info["list"]
    word_list = word_list + info["list"]


#print word_list
print len(word_list)
list_len = len(word_list)

raw_word = []
for j in range(0,list_len):
    raw_word.append(word_list[j]["word"].encode("utf-8"))

#print raw_word

if IS_RANDOM:
    random.shuffle(raw_word)

f=open(WORD_LIST_NAME,"w")
f.write("\n".join(raw_word))
f.close()



