from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
import pandas as pd

# 1. 启动 Edge 浏览器
service = Service("./msedgedriver.exe")
driver = webdriver.Edge(service=service)

base_url = "https://www.shixiseng.com/interns?keyword=Java%E5%AE%9E%E4%B9%A0&city=%E5%85%A8%E5%9B%BD&type=intern"
print(f"正在用 Edge 打开浏览器访问：{base_url}")
driver.get(base_url)
print("等待页面稳定（15秒）...")
time.sleep(15)

all_jobs = []

# 2. 使用XPath模糊匹配，找所有包含“实习”或“开发”的链接
job_links = driver.find_elements(By.XPATH, "//a[contains(text(),'实习') or contains(text(),'开发')]")

print(f"在页面找到 {len(job_links)} 个可能的岗位链接。")

for link in job_links:
    try:
        title = link.text.strip()
        # 跳过头部的导航链接，只处理字数正常的岗位名
        if not title or len(title) < 4 or len(title) > 30:
            continue

        # 提取公司名：用XPath找上一级的父元素里包含“公司”的链接
        try:
            parent = link.find_element(By.XPATH, "..")
            company_elem = parent.find_element(By.XPATH,
                                               ".//a[contains(text(),'公司') or contains(text(),'科技') or contains(text(),'传媒')]")
            company = company_elem.text.strip()
        except:
            company = ""

        # 提取薪资：用XPath在卡片中找“/天”结尾的文本
        try:
            salary_elem = parent.find_element(By.XPATH, ".//*[contains(text(),'/天')]")
            salary = salary_elem.text.strip()
        except:
            salary = ""

        # 提取详情链接
        link_url = link.get_attribute("href")

        all_jobs.append({
            "岗位名称": title,
            "公司": company,
            "薪资": salary,
            "详情链接": link_url
        })
        print(f"已抓取: {title} | {company} | {salary}")

    except Exception as e:
        print(f"解析某链接时出错: {e}")
        continue

# 3. 关闭浏览器
print("\n任务完成，关闭浏览器。")
driver.quit()

# 4. 数据保存为CSV
print(f"\n共获取 {len(all_jobs)} 条岗位信息")
if all_jobs:
    df = pd.DataFrame(all_jobs)
    df.to_csv("java_intern_jobs.csv", index=False, encoding="utf_8_sig")
    print("✅ 数据已保存到 java_intern_jobs.csv")
else:
    print("❌ 未爬取到数据，请检查页面结构。")