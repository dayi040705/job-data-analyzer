import requests
from bs4 import BeautifulSoup

# 1. 伪装成浏览器，设置请求头（User-Agent）
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 2. 目标网址
url = 'https://www.shixiseng.com/interns?keyword=Java%E5%AE%9E%E4%B9%A0&city=%E5%85%A8%E5%9B%BD&type=intern'

# 3. 发送请求
print(f'正在发送请求到: {url}')
response = requests.get(url, headers=headers, timeout=10)

# 4. 检查请求是否成功
if response.status_code == 200:
    print('请求成功，开始解析网页结构...\n')
    soup = BeautifulSoup(response.text, 'html.parser')

    # 打印网页的标题
    print(f'网页标题: {soup.title.string}\n')

    # 尝试提取所有链接的文本内容
    print('正在尝试提取链接和文本片段:')
    for i, link in enumerate(soup.find_all('a')):
        text = link.get_text(strip=True)
        if text and i < 5:  # 只打印前5个有效文本
            print(f'  - {text}')

    # 检查页面中是否包含“Java”等关键词
    if 'Java' in response.text:
        print('\n✅ 分析：页面包含关键词"Java"，基础内容可访问。')
    else:
        print('\n分析：页面未包含关键词"Java"，内容可能是动态加载的。')

else:
    print(f'❌ 请求失败，状态码: {response.status_code}')