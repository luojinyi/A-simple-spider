# 将得到的信息以一个网页的形式展现出来
class html_outputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            print("数据为空！")
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding="utf-8")
        try:
            fout.write("<html>")
            fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
            fout.write("<body>")
            fout.write("<table>")

            for data in self.datas:
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['url'])
                fout.write("<td>%s</td>" % data['title'])
                fout.write("<td>%s</td>" % data['summary'])
                fout.write("</tr>")

            fout.write("</table>")
            fout.write("</body>")
            fout.write("</html>")
        except Exception as e:
            print(e)
            print("文件写入失败！")
        finally:
            fout.close()

