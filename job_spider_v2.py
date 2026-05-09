from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# 1. 设置Edge浏览器驱动路径（当前文件夹下）
# 下载解压后的文件名为 msedgedriver.exe，不是 chromedriver.exe
service = Service("./msedgedriver.exe")

# 2. 启动 Edge 浏览器
driver = webdriver.Edge(service=service)

# 3. 目标网址
url = "https://www.shixiseng.com/interns?keyword=Java%E5%AE%9E%E4%B9%A0&city=%E5%85%A8%E5%9B%BD&type=intern"
print(f"正在用 Edge 打开浏览器访问：{url}")
driver.get(url)

# 4. 等待页面加载（等5秒让数据渲染完）
time.sleep(5)

# 5. 尝试获取页面中所有的岗位名称
print("\n正在提取岗位信息...")
job_cards = driver.find_elements(By.CSS_SELECTOR, ".intern-wrap .job-name")
if job_cards:
    print(f"找到 {len(job_cards)} 个岗位：")
    for i, job in enumerate(job_cards[:5]):  # 只打印前5个
        print(f"  {i+1}. {job.text}")
else:
    print("没有找到岗位卡片，可能需要调整选择器。打印部分页面文本以供分析：")
    print(driver.find_element(By.TAG_NAME, "body").text[:500])

# 6. 关闭浏览器
print("\n任务完成，关闭浏览器。")
driver.quit()