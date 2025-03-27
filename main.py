from db_connector import DatabaseManager
from data_processor import BusinessAnalyzer
from llm_integration import ReportGenerator

def main():
    # 初始化组件
    db = DatabaseManager()
    analyzer = BusinessAnalyzer(db)
    llm = ReportGenerator()
    
    # 业务数据处理
    sales_data = analyzer.get_sales_summary(days=90)
    
    # 生成分析报告
    report = llm.generate_report(sales_data, "季度销售")
    
    # 存储报告
    db.save_report(report, "sales_analysis")
    
    # 输出报告
    print("生成报告成功！\n")
    print(report)

if __name__ == "__main__":
    main()