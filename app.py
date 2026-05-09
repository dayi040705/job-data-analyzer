from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    # 1. 读取数据
    df = pd.read_csv("java_intern_jobs.csv")

    # 2. 生成原始数据表格
    table_html = df.to_html(index=False, classes='table')

    # 3. 生成统计分析表格（公司排名、薪资分布）
    company_counts = df['公司'].value_counts().head(10).reset_index()
    company_counts.columns = ['公司', '岗位数']
    company_table = company_counts.to_html(index=False, classes='table')

    salary_counts = df['薪资'].value_counts().head(10).reset_index()
    salary_counts.columns = ['薪资', '岗位数']
    salary_table = salary_counts.to_html(index=False, classes='table')

    # 4. 组合成美观的 HTML 页面
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Java实习岗位分析报告</title>
        <style>
            body {{ font-family: 'Microsoft YaHei', Arial; margin: 40px; background-color: #f5f5f5; }}
            .container {{ max-width: 1200px; margin: 0 auto; }}
            .card {{ background: white; padding: 20px; margin: 20px 0; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
            .table {{ border-collapse: collapse; width: 100%; margin-top: 10px; }}
            .table th, .table td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            .table th {{ background-color: #4CAF50; color: white; }}
            h1 {{ color: #333; text-align: center; }}
            h2 {{ color: #555; border-bottom: 2px solid #4CAF50; padding-bottom: 5px; }}
            .stats {{ background: #e8f5e9; padding: 15px; border-radius: 5px; margin: 10px 0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Java 实习岗位数据分析报告</h1>

            <div class="card">
                <div class="stats">
                    <strong>数据概览：</strong>共抓取 <strong>{len(df)}</strong> 条岗位信息，涉及 <strong>{df['公司'].nunique()}</strong> 家公司。
                </div>
            </div>

            <div class="card">
                <h2>🏢 公司招聘活跃度 TOP 10</h2>
                {company_table}
            </div>

            <div class="card">
                <h2>💰 薪资分布 TOP 10</h2>
                {salary_table}
            </div>

            <div class="card">
                <h2>📋 全部岗位数据（共{len(df)}条）</h2>
                {table_html}
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)


if __name__ == '__main__':
    app.run(debug=True, port=5000)