import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': 'newdbone'
}

LLM_CONFIG = {
    'api_key': os.getenv('LLM_API_KEY'),
    'endpoint': 'https://api.siliconflow.cn/v1/chat/completions',
    'model': 'Pro/deepseek-ai/DeepSeek-R1'
}