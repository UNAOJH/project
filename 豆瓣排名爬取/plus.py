import datetime
import logging

import requests
from lxml import etree
from bs4 import BeautifulSoup


LogName = "movie_scraper.log"
# 配置日志
logging.basicConfig(
    filename=LogName,  # 日志文件名
    level=logging.ERROR,  # 设置日志级别
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def coming():
    try:
        url = "https://movie.douban.com/coming/"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 "
                          "Safari/537.36"
        }
        print("\n" + "抓取网址为: " + url)

        get = requests.get(url, headers=headers)
        etree_html = etree.HTML(get.text)
        print("请求完成,等待获取...")
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
                "\n\n\n" + "=" * (time_width + name_width) + nowTime + '=' * (time_width + name_width) + "\n")
            f.write(top + "\n")
            f.write(G + "\n")
            trs = etree_html.xpath('//*[@id="content"]/div/div[1]/table/tbody/tr')

            i = 0
            for tr in trs:
                # 提取文本
                time_list = tr.xpath('./td[1]/text()')
                time = ' '.join(
                    [t.strip() for t in time_list if
                     t.strip()])  # 使用列表推导式和 strip() 方法去掉多余的空白)   # 这里将列表中的所有文本连接起来，处理换行符
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
            print('-' * (time_width + name_width) + f"获取到 {i} 条数据" + '-' * (time_width + name_width))
            print(f"抓取资源已放置程序执行目录下,文件名为: {Filename}")
        with open("即将上演.txt", 'a', encoding="utf-8") as f:
            f.write('=' * (time_width + name_width) + f"获取到 {i} 条数据" + '=' * (
                    time_width + name_width) + "\n")  # 确保数据条数也能够新起一行
        get.close()
        if i == 0:
            print("获取异常,请联系开发人员")
            print(f"异常日志文件:{LogName}")
    except Exception as e:
        print("获取异常,请联系开发人员")
        print(f"异常日志文件:{LogName}")
        logging.error("出现异常: %s", str(e))


def now():
    try:
        global name, score, endScore
        url = "https://movie.douban.com/cinema/nowplaying/changde/"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 "
                          "Safari/537.36"
        }
        requests_get = requests.get(url, headers=headers)
        page = BeautifulSoup(requests_get.text, "html.parser")

        GetName = page.find("ul", class_="lists").find_all("img")
        # B = GetName.find("a", class_="ticket-btn").find_all("title")
        # print(GetName)
        Scores = page.find("ul", class_="lists").find_all("li", class_='srating')
        # print("=================")
        # print(Scores)
        # print("=================")
        # print(Scores.find('span', class_='subject-rate').text)
        print("请求完成,等待获取...")
        Sum = 0
        MovieNameList = []
        # 获取电影名
        for Name in GetName:
            Sum += 1
            name = Name.get("alt")
            if name:  # 只处理非空的 title
                MovieNameList.append(name)  # 添加有效的 title 到 texts

        # 获取电影评分
        ssum = 0
        scoreList = []
        for Score in Scores:
            # print("-------------")
            # print(Score)
            # print("·····························")
            score = Score.text
            scoreList.append(score)
            # print(score)
            ssum += 1
        # 对评分格式化
        endScores = [score.strip() for score in scoreList]
        FileName = "热映电影评分报告"  # 使用列表推导式去除空格
        with open(f"{FileName}.txt", "a", encoding="utf-8") as f:
            nowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n\n电影评分报告,生成时间{nowTime}\n\n")
            # f.write("=" * 30 + "\n")
            time_width = 5
            name_width = 5
            f.write('-' * (time_width + name_width) + nowTime + '-' * (time_width + name_width) + "\n")

            # 检查是否有足够的电影名和评分
            if len(MovieNameList) == len(endScores):
                f.write(f"{'电影名':<10} {'评分':<5}\n")  # 格式化列标题
                f.write("-" * 30 + "\n")  # 添加分隔线

                # 拼接并输出电影名和对应评分
                for name, score in zip(MovieNameList, endScores):
                    result = f"{name:<10} {score:<5}\n"
                    print(result)
                    f.write(result)
                print(f"获取到 {Sum} 条热映的电影数据")
                print(f"获取到 {ssum} 个评分")
                f.write(f"获取到 {Sum} 条热映的电影数据" + "\n")
                f.write(f"获取到 {ssum} 个评分" + "\n")
                print(f'抓取资源已放置程序执行目录下,文件名为: "{FileName}"')
            else:
                print("电影名和评分数量不匹配，不能输出。" + "\n")

        # 拼接
        # print(f"电影名: {name}\t评分:{endScore}")
        requests_get.close()
        # print("出现异常,请查看日志")
        # print(f"异常日志文件:{LogName}")
    except Exception as e:
        print("获取异常,请联系开发人员")

        print(f"异常日志文件:{LogName}")
        logging.error("出现异常: %s", str(e))


if __name__ == '__main__':
    v = True
    while v:
        In = input("请输入获取的资源：\n1:查询即将上演电影\n2:获取当前热映电影\n3:退出程序\n")
        if In == "1":
            print("正在请求,请稍后...")
            coming()
            # input("按任意键退出...")
        elif In == "2":
            print("正在请求,请稍后...")
            now()
            # input("按任意键退出...")
        elif In == "3":
            print("退出程序...")
            v = False
        else:
            print("选项有误，请重新输入" + "\n\n")
        if v:  # 如果没有选择退出
            while True:  # 无限循环，直到获得有效输入
                continue_choice = input("是否继续选择？(y/n): ").strip().lower()  # 清除多余的空白并转换为小写
                if continue_choice == 'y':
                    break  # 有效输入，退出循环，继续程序
                elif continue_choice == 'n':
                    v = False  # 设置标志为 False，退出程序
                    print("退出程序...")
                    break  # 也退出循环
                else:
                    print("无效输入，请输入'y'或'n'。")  # 提示用户重新输入
