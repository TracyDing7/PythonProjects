from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = "https://en.wikipedia.org"
his =  ["/wiki/Web_crawler"]

for i in range(10): #为什么是10层？100000不好吗？ 百度百科有那么多层？
    try:
        url = base_url + his[-1]
        html = urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(html, features='lxml')
        h1 = soup.find('h1').get_text()  # 读取h1标题
        print(h1)
        sub_urls = soup.find_all("a", {"href": re.compile("/wiki/(.)+")})  # 将+后面的$删除了
        if len(sub_urls) != 0:
            res = random.sample(sub_urls, 1)[0]
            if res not in his:
                his.append(res['href'])
                print(i, h1, '    url: ', his[-1])


        else:  # 这个else和谁对应？len(sub_urls) != 0  如果能走到这里，说明已经是= 0，是最终页面，没有（广告和干扰不算）可用链接了
            his.pop()
    except:  # 如果有问题，比如网络问题或者其他不可控因素造成的失败，直接跳出本次循环，执行下一次。
        continue
        print('error')