from datetime import datetime, timedelta

class BusinessAnalyzer:
    def __init__(self, db_manager):
        self.db = db_manager
        
    def get_sales_summary(self, days=30):
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        query = f"""
        SELECT 
            region,
            product,
            SUM(sales_amount) as total_sales,
            COUNT(*) as transactions
        FROM sales_data
        WHERE transaction_date BETWEEN '{start_date}' AND '{end_date}'
        GROUP BY region, product
        """
        
        raw_data = self.db.execute_query(query)
        return self._format_analysis(raw_data)
    
    def _format_analysis(self, data):
        # 结构化数据处理示例
        summary = {
            'total_sales': sum(item['total_sales'] for item in data),
            'top_products': sorted(data, key=lambda x: x['total_sales'], reverse=True)[:3],
            'region_distribution': {item['region']: item['total_sales'] for item in data}
        }
        return summary