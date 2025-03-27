import requests
import json
from config import LLM_CONFIG

class ReportGenerator:
    def __init__(self):
        self.api_key = LLM_CONFIG['api_key']
        self.endpoint = LLM_CONFIG['endpoint']
        self.model = LLM_CONFIG['model']
        
    def generate_report(self, data, analysis_type):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        prompt = self._build_prompt(data, analysis_type)
        
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        
        response = requests.post(self.endpoint, headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content']
    
    def _build_prompt(self, data, analysis_type):
        # 构建结构化提示模板
        return f"""
        请基于以下业务数据生成{analysis_type}分析报告：
        {json.dumps(data, indent=2, ensure_ascii=False)}
        
        报告要求：
        1. 使用中文撰写
        2. 包含关键趋势分析
        3. 提出3条可执行的业务建议
        4. 使用Markdown格式输出
        """