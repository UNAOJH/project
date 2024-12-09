# Movie Scraper  

Movie Scraper 是一个基于 Python 的爬虫程序，用于抓取豆瓣电影即将上映和当前热映的电影信息，并生成可读的报告文件。  

## 功能  

- **即将上映电影**  
  - 抓取豆瓣电影即将上映的电影信息，包括上映日期、片名、类型、制片国家/地区和想看人数。  
  - 数据保存为 `即将上演.txt` 文件。  

- **当前热映电影**  
  - 抓取当前热映电影的名称和评分。  
  - 数据保存为 `热映电影评分报告.txt` 文件。  

## 依赖  

运行该项目需要以下 Python 第三方库：  

- `requests`  
- `lxml`  
- `BeautifulSoup4`  

您可以通过以下命令安装这些依赖：  

```bash
pip install requests lxml beautifulsoup4
```  

## 使用方法  

1. 克隆本仓库到本地：  
   ```bash
   git clone https://github.com/yourusername/movie-scraper.git
   cd movie-scraper
   ```  

2. 运行主程序：  
   ```bash
   python movie_scraper.py
   ```  

3. 根据提示输入选项：  
   - 输入 `1` 查询即将上映电影。  
   - 输入 `2` 获取当前热映电影及其评分。  
   - 输入 `3` 退出程序。  

## 日志  

程序运行过程中，如果发生异常，会记录在 `movie_scraper.log` 文件中，便于排查问题。  

## 文件结构  

```
movie-scraper/
│
├── movie_scraper.py       # 主程序代码
├── movie_scraper.log      # 日志文件
├── 即将上演.txt          # 即将上映电影报告
├── 热映电影评分报告.txt  # 当前热映电影报告
└── README.md              # 使用说明文件
```  

## 注意事项  

1. 该程序使用的豆瓣电影数据需遵守相关网站的服务条款和法律法规，请勿滥用。  
2. 部分数据获取可能因网站结构变动或网络问题而失败。  

## 免责声明  

1. 本项目仅用于学习和研究用途，严禁将本项目用于商业用途或任何违反法律法规的行为。  
2. 本项目获取的数据来源于公开网络，本人对数据的准确性和合法性不承担任何责任。  
3. 如因使用本项目导致任何直接或间接的损失，开发者概不负责。  

## 联系方式  

如果您有任何问题、建议或合作意向，可以通过以下方式联系我：  
- **邮箱**: [unaojh@google.com](mailto:unaojh@google.com)  
- **GitHub**: [UNAOJH](https://github.com/UNAOJH)  

## 贡献  

欢迎提交问题和功能请求，您也可以通过 Fork 并提交 Pull Request 的方式贡献代码。  

## 许可证  

本项目基于 MIT 许可证开源，详情请参见 [LICENSE](LICENSE) 文件。  
