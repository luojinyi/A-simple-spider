# 管理url
class url_manager(object):

    # 新建两个存储url的集合，一个存放未解析的，一个存放已经解析的
    def __init__(self):
        self.new_urls = set()
        self.crawled_urls = set()

    # 将传进来的新的url添加到new_urls集合
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.crawled_urls:
            self.new_urls.add(url)

    # 将传进来的urls一个个存放到new_urls
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)


    # 判断new_urls是否还含有未解析的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 将解析了的url移入crawled_urls
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.crawled_urls.add(new_url)
        return new_url
