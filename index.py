from flask import (Flask, request, Response, render_template)
from dotenv import load_dotenv

load_dotenv()
#openai.api_key = os.environ.get('GPT_API_KEY')

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World - part 2'
