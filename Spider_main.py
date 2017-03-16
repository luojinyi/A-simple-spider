from imooc_spider import url_manager, html_downloader, html_outputer, html_parse

# 爬虫的主函数
class Crawler(object):
    def __init__(self):
        # 初始化所需要的对象,包括url管理器，网页下载器，网页解析器，输出器
        # 来提供给craw（）使用
        # 来提供给craw（）使用
        self.urls = url_manager.url_manager()
        self.downloader = html_downloader.html_downloader()
        self.parser = html_parse.html_parser()
        self.outputer = html_outputer.html_outputer()

    def craw(self, root_url, url_amount):
        count = 1
        # 添加根url
        self.urls.add_new_url(root_url)
        # 开始解析
        while self.urls.has_new_url():
            try:
                # 获取url
                new_url = self.urls.get_new_url()
                print('crawling URL %d ... : %s' % (count, new_url))
                # 将url对应的页面内容进行下载
                html_cont = self.downloader.download(new_url)
                # 对下载下来的页面进行解析,将解析出来的数据进行保存
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将解析出来的urls添加到url_manager
                self.urls.add_new_urls(new_urls)
                # 将数据进行收集
                self.outputer.collect_data(new_data)

                if count == url_amount:
                    print("恭喜爬取完成！")
                    break
                count += 1
            except Exception as e:
                print(e)
                print("爬取失败！")
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    url_amount = 10
    obj_Crawler = Crawler()
    obj_Crawler.craw(root_url, url_amount)



