import re
import urllib.parse
from bs4 import BeautifulSoup
class html_parser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            print("page_url or html_cont is empty")
            return None
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    # 返回soup匹配到的urls的集合
    def _get_new_urls(self, page_url,soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/.*"))
        for link in links:
            new_url = link['href']  # 得到相对路径
            new_full_url = urllib.parse.urljoin(page_url, new_url)  # 得到绝对路径
            new_urls.add(new_full_url)
        return new_urls

    # 返回soup匹配到的标题与简介字典
    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()   # 获得标题
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()   # 获得简介
        return res_data








