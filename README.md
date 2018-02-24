# bcz2txt

##### author:pinko


```
2018.02.24
有老铁向我反映说无法使用
我发现登录功能一切正常，就是百词斩家的在线背单词功能目前无法使用，无法使用浏览器背单词，并且接口ok但是不返回任何单词。
既然是斩家问题就等待他们的工程师小哥哥解决了之后再重新适配吧~
```

---
### Introduction

自动登录百词斩，爬取已经学过的单词，生成一个txt，可以上传到欧路词典后台作为复习课本，然后就可以用欧路词典进行复习。

*欧路词典单词复习课本地址:https://my.eudic.net/recite/userbooks*

---
### Usage

修改下面的配置参数运行即可，不需要参数

```

#百词斩的登录邮箱
USERNAME = "****@foxmail.com"
#百词斩的登录密码
PASSWORD = "****"
#想要生成的txt的文件名
WORD_LIST_NAME = "word_done.txt"
#生成的复习书是否随机排列，如果字母排列改成False
IS_RANDOM = True

```

---
### Dependency

Python2.7, requests, BeautifulSoup, json

---
### Pictures

![example](https://github.com/pinkomeo/bcz2txt/blob/master/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20170807170332.png)


