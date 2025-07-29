import os
from dotenv import load_dotenv

load_dotenv()

# AZURE
AGENT_ENDPOINT = os.getenv('AGENT_ENDPOINT')
AGENT_KEY = os.getenv('AGENT_KEY')
AGENT_NAME = os.getenv('AGENT_NAME')

# CHAT EN PRUEBA
URL = os.getenv("URL")

# ARCHIVOS UTILIZADOS
INPUT_FILE_PATH = os.getenv('INPUT_FILE_PATH')

# variables
## output ejemplo
sets = '''
        {
            "question": "como hacer una torta",
            "expected_answer": "para hacer una torta vas a tener que"
        },
        {
            "question": "content of the second question",
            "expected_answer": "the expected answer to this question"
    }
'''


