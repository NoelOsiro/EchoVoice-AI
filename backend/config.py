import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
VECTOR_DB_ENDPOINT = os.getenv('VECTOR_DB_ENDPOINT')
VECTOR_DB_API_KEY = os.getenv('VECTOR_DB_API_KEY')
DELIVERY_PROVIDER_API_KEY = os.getenv('DELIVERY_PROVIDER_API_KEY')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
