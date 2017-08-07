# bcz2txt

##### author:pinko

### 功能：自动登录百词斩，爬取已经学过的单词，生成一个txt，可以上传到欧路词典后台作为复习课本，然后就可以用欧路词典进行复习。欧路词典单词复习课本地址:https://my.eudic.net/recite/userbooks

### Usage: 修改下面的配置参数运行即可，不需要参数
### Dependency: Python2.7,requests,BeautifulSoup,json

#百词斩的登录邮箱
USERNAME = "****@foxmail.com"
#百词斩的登录密码
PASSWORD = "****"
#想要生成的txt的文件名
WORD_LIST_NAME = "word_done.txt"
#生成的复习书是否随机排列，如果字母排列改成False
IS_RANDOM = True
