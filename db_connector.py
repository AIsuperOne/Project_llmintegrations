import mysql.connector
from config import DB_CONFIG

class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(**DB_CONFIG)
        
    def execute_query(self, query):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def save_report(self, content, analysis_type):
        query = """
        INSERT INTO analysis_reports 
        (generated_time, report_content, analysis_type)
        VALUES (NOW(), %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (content, analysis_type))
        self.connection.commit()
        cursor.close()
        