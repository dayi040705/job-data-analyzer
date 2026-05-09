import pandas as pd

# 读取数据
df = pd.read_csv("java_intern_jobs.csv")

print(f"共读取 {len(df)} 条数据\n")
print("===== 前 5 行 =====")
print(df.head(), "\n")

# 去重后的公司数量
print(f"公司数量：{df['公司'].nunique()}")
print(f"岗位数量：{len(df)}\n")

# 薪资分布（如果薪资格式统一的话，先原样统计）
print("===== 薪资 TOP 10 =====")
print(df['薪资'].value_counts().head(10), "\n")

# 导出统计数据
company_counts = df['公司'].value_counts().head(10)
company_counts.to_csv("company_ranking.csv", encoding="utf_8_sig")
print("✅ 公司排名已保存到 company_ranking.csv")