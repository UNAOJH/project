import datetime
import requests
from lxml import etree
from bs4 import BeautifulSoup


def coming():
    url = "https://movie.douban.com/coming"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 "
                      "Safari/537.36"
    }
    print("\n" + "抓取网址为: " + url)

    get = requests.get(url, headers=headers)
    etree_html = etree.HTML(get.text)

    html_content = '''
    <table>
        <thead>
            <tr>
                <th href="?sequence=desc" class="arrU">上映日期</th>
                <th>片名</th>
                <th width="140">类型</th>
                <th width="100">制片国家 / 地区</th>
                <th  href="?sortby=wish&sequence=desc" class="arrN">想看</th>
            </tr>
        </thead>
    </table>
    '''
    # 加载 HTML 内容
    tops = etree.HTML(html_content)

    # 使用 XPath 提取所有 <th> 元素中的文本
    top = tops.xpath('//thead/tr/th/text()')
    # print(top)
    # 输出提取的表头信息
    headers = [header.strip() for header in top]  # 去掉多余的空白
    # print("表头信息:", headers)
    Filename = "即将上演"
    with open(f"{Filename}.txt", 'a', encoding="utf-8") as f:
        f.write("抓取网址为: " + url)
        time_width = 20
        name_width = 40
        type_width = 20
        region_width = 15
        look_width = 10
        nowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        length = time_width + name_width + str(nowTime).__len__() + time_width + name_width

        top = f"{headers[0]:<{time_width}} {headers[1]:<{name_width}} {headers[2]:<{type_width}} {headers[3]:<{region_width}} {headers[4]}"  # 只展示前两列
        G = '-' * length  # 打印分隔线
        print(top)
        print(G)
        f.write(
            "\n" + '/' * (time_width + name_width) + nowTime + '\\' * (time_width + name_width) + "\n")
        f.write(top + "\n")
        f.write(G + "\n")
        trs = etree_html.xpath('//*[@id="content"]/div/div[1]/table/tbody/tr')

        i = 0
        for tr in trs:
            # 提取文本
            time_list = tr.xpath('./td[1]/text()')
            time = ' '.join(
                [t.strip() for t in time_list if t.strip()])  # 使用列表推导式和 strip() 方法去掉多余的空白)   # 这里将列表中的所有文本连接起来，处理换行符
            name = tr.xpath('./td[2]/a/text()')[0]
            Type_list = tr.xpath("./td[3]/text()")
            Type = ' '.join([t.strip() for t in Type_list if t.strip()])
            region_list = tr.xpath('./td[4]/text()')
            region = ' '.join([t.strip() for t in region_list if t.strip()])
            look_list = tr.xpath('./td[5]/text()')
            look = ' '.join([t.strip() for t in look_list if t.strip()])

            # 处理长片名，添加省略号
            if len(name) > name_width:
                name = name[:name_width - 3] + '...'  # 截取片名并添加省略号

            result = f"{time:<{time_width}} {name:<{name_width}} {Type:<{type_width}} {region:<{region_width}}{look:<{look_width}}"
            print(result)
            f.write(result + "\n")
            i += 1
            # print(i)
            # break
        print('=' * (time_width + name_width) + f"获取到 {i} 条数据" + '=' * (time_width + name_width))
        print(f"抓取资源已放置程序执行目录下,文件名为: {Filename}")
    with open("即将上演.txt", 'a', encoding="utf-8") as f:
        f.write('=' * (time_width + name_width) + f"获取到 {i} 条数据" + '=' * (
                time_width + name_width) + "\n")  # 确保数据条数也能够新起一行
    get.close()


def now():
    url = "https://movie.douban.com/cinema/nowplaying/changde/"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 "
                      "Safari/537.36"
    }
    requests_get = requests.get(url, headers=headers)
    page = BeautifulSoup(requests_get.text, "html.parser")
    A = page.find("ul", class_="lists").find_all("img")
    # B = A.find("a", class_="ticket-btn").find_all("title")
    # print(A)
    Sum = 0
    for a in A:
        Sum += 1
        # print("++++++++++++++++++")
        name = a.get("alt")
        # if name:  # 只处理非空的 title
        #     texts.append(name)  # 添加有效的 title 到 texts
        print(name)
    print(Sum)
    # print(texts)
    requests_get.close()


if __name__ == '__main__':
    v = False
    while not v:
        In = input("请输入获取的资源：\n1:查询即将上演电影\n2:获取当前热映电影")
        if In == "1":
            coming()
            v = True
            input("按任意键退出")
        elif In == "2":
            now()
            v = True
        else:
            print("选项有误，请重新输入" + "\n\n")
