# 主要就是把传进去的url的网页内容下载下来
from urllib import request

class html_downloader(object):

    def download(self, url):
        if url is None:
            return None
        response = request.urlopen(url)
        if response.getcode() != 200:
            print(response.getcode)
        return response.read()
